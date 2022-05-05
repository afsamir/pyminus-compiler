from exceptions import InvalidInputException, InvalidNumberException, UnclosedCommentException, UnmatchedCommentException


WHITESPACES = {' ', '\n', '\r' ,'\t', '\v', '\f'}
NUMERALS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
SYMBOLS = {'(', ')', '[',']',',',';',':','+','-','<',}
EOF = '$'
KEYWORDS = ['break', 'continue', 'def', 'else', 'if', 'return', 'while']
ALPHABET = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

 # when to accept and raise error, facing an irrelevant input?

class Scanner:
    def __init__(self, address):
        self.line_no = 1
        self.position = 0
        self.tokens = {}
        self.symbols = list(KEYWORDS)
        self.errors = {}
        self.eof = False
        self.text = open(address, "r").read()

    def parse(self):
        while not self.eof:
            try:
                type, token = self.get_next_token()
                if type not in ['WHITESPACE', 'COMMENT', 'EOF']:
                    self.add_to_token_list(type, token)
                if type in {'ID'}:
                    self.add_to_symbol_table(token)
            except Exception as error:
                self.add_to_error_list(error.message, error.expression)
                # print("{0}:  in line {2} '{1}'".format(error.message, error.expression, self.line_no))
                pass
        self.print_tokens(self.tokens, 'tokens.txt')
        self.print_errors(self.errors, 'lexical_errors.txt')
        self.print_string_table(self.symbols, 'symbol_table.txt')


    def get_next_character(self):
        if self.position >= len(self.text):
            self.eof = True
            return EOF
        next = self.text[self.position]
        self.position = self.position + 1
        if next is '\n':
            self.line_no = self.line_no + 1
        # print(next)
        return next

    def go_back(self):
        self.position = self.position - 1
        if self.text[self.position] is '\n':
            self.line_no = self.line_no - 1


    def get_next_token(self):
        next = self.get_next_character()
        if next in NUMERALS:
            return self.number_state(next)
        if next in ALPHABET:
            return self.id_state(next)
        if next in '#':
            return self.single_comment_state(next)
        if next in '/':
            return self.slash_comment_state(next)
        if next in SYMBOLS:
            return ("SYMBOL", next)
        if next is '*':
            return self.star_state()
        if next is '=':
            return self.equal_state()
        if next in WHITESPACES:
            return ("WHITESPACE", next)
        if next is EOF:
            return ("EOF", EOF)
        else:
            raise InvalidInputException(next)

    def number_state(self, current):
        next = self.get_next_character()
        if next in NUMERALS:
            return self.number_state(current + next)
        if next is '.':
            return self.half_float_state(current + next)
        if next in WHITESPACES: 
            return ('NUM', current)
        if next is EOF: 
            return ('NUM', current)
        if next in ALPHABET: 
            raise InvalidNumberException(current + next)
        if next in {*SYMBOLS, '#', '/', '*', '='}: 
            self.go_back()
            return ('NUM', current)
        else:
            raise InvalidNumberException(current + next)


    def half_float_state(self, current):
        next = self.get_next_character()
        if next in NUMERALS:
            return self.float_state(current + next)
        else:
            raise InvalidInputException(current + next)


    def float_state(self, current):
        next = self.get_next_character()
        if next in NUMERALS:
            return self.float_state(current + next)
        if next in WHITESPACES: 
            return ('NUM', current)
        if next is EOF: 
            return ('NUM', current)
        if next in ALPHABET: 
            raise InvalidNumberException(current = next)
        if next in {*SYMBOLS, '#', '/', '*', '='}: 
            self.go_back()
            return ('NUM', current)
        else:
            raise InvalidNumberException(current + next)
   
        
    def id_state(self, current):
        next = self.get_next_character()
        if next in ALPHABET:
            return self.id_state(current + next)
        if next in NUMERALS:
            return self.id_state(current + next)
        if next in WHITESPACES: 
            self.go_back()
            return self.id_or_keyword(current)
        if next is EOF: 
            return self.id_or_keyword(current)
        if next in SYMBOLS: 
            self.go_back()
            return self.id_or_keyword(current)
        if next in {'#', '/', '=', '*'}: 
            self.go_back()
            return self.id_or_keyword(current)
        else:
            raise InvalidInputException(current + next)

    def single_comment_state(self, current):
        next = self.get_next_character()
        if next is '\n':
            return ("COMMENT", current)
        if next is EOF:
            return ("COMMENT", current)
        else:
            return self.single_comment_state(current + next) 

    def slash_comment_state(self, current):
        next = self.get_next_character()
        if next is "*":
            self.comment_start_line = self.line_no
            return self.half_comment_state(current + next)
        else:
            self.go_back()
            raise InvalidInputException(current)

    def half_comment_state(self, current):
        next = self.get_next_character()
        if next is "*":
            return self.multi_comment_state(current + next)
        if next is EOF:
            raise UnclosedCommentException(current + next)
        else:
            return self.half_comment_state(current + next)

    def multi_comment_state(self, current):
        next = self.get_next_character()
        if next is "/":
            return ("COMMENT", current + next)
        else:
            return self.half_comment_state(current + next)
    
    def star_state(self):
        next = self.get_next_character()
        if next is '*':
            return ("SYMBOL", '**')
        if next is '/':
            raise UnmatchedCommentException()
        if next in {*WHITESPACES, *ALPHABET, *NUMERALS, *SYMBOLS, '#', '/', '='}:
            self.go_back()
            return ("SYMBOL", '*')
        else:
            raise InvalidInputException('*' + next)
        
    def equal_state(self):
        next = self.get_next_character()
        if next is '=':
            return ("SYMBOL", '==')
        if next in {*WHITESPACES, *ALPHABET, *NUMERALS, *SYMBOLS, '#', '/', '*'}:
            self.go_back()
            return ("SYMBOL", '=')
        else:
            raise InvalidInputException('=' + next)

    def id_or_keyword(self, token):
        if token in KEYWORDS:
            return ("KEYWORD", token)
        elif(token is ''):
            return ("EOF", token)
        else:
            return ("ID", token)

    def add_to_token_list(self, type, token):
        try:
            self.tokens[self.line_no]
        except KeyError:
            self.tokens[self.line_no] = []
        self.tokens[self.line_no].append((type, token))
        
    def add_to_symbol_table(self, token):
        if self.symbols.count(token) is 0:
            self.symbols.append(token)

    def add_to_error_list(self, error, exp):
        if error == 'Unclosed comment':
            err_line = self.comment_start_line
        else:
            err_line = self.line_no
        try:
            self.errors[err_line]
        except KeyError:
            self.errors[err_line] = []
        self.errors[err_line].append((exp, error))
 

    def print_tokens(self, table, filename):
        lines = []
        for line in table:
            lines.append(str(line) + ".\t" + " ".join(map(lambda x: '({0}, {1})'.format(x[0], x[1]),table[line])))
        file = open(filename, 'w')
        file.write("\n".join(lines))
        file.close()

    def print_errors(self, table, filename):
        file = open(filename, 'w')
        if len(table) is 0:
            file.write('There is no lexical error.')
        else:
            lines = []
            for line in table:
                lines.append(str(line) + ".\t" + " ".join(map(lambda x: '({0}, {1})'.format(x[0], x[1]),table[line])))
            file.write("\n".join(lines))
        file.close()


    def print_string_table(self, table, filename):
        lines = []
        line_no = 1
        for string in table:
            lines.append(str(line_no) + ".\t" + string)
            line_no = line_no + 1
        file = open(filename, 'w')
        file.write("\n".join(lines))
        file.close()
