from cmath import log
from scanner import Scanner


class Parser:
    def __init__(self, scanner:Scanner, parse_table):
        self.scanner = scanner
        self.parse_table = parse_table
        self.parse_stack = ['Program']
        self.tree_rules = []
        self.errors = []
        self.get_next_input()


    def parse(self):
        while(len(self.parse_stack) is not 0 and self.get_value(self.current_token) is not '$'):
            self.proceed()
        print(self.errors)


    def proceed(self):
        print(self.current_token, self.parse_stack)
        if self.parse_stack[-1] == 'Epsilon':
            self.accept_epsilon()
        elif self.parse_stack[-1] == self.get_value(self.current_token):
            self.accept_token()
        else:
            if self.parse_stack[-1] not in self.parse_table.keys():
                self.handle_terminal_error()
                return
            states_moves = self.parse_table[self.parse_stack[-1]]
            if self.get_value(self.current_token) not in states_moves:
                print(self.get_value(self.current_token))
                self.handle_empty_error()
                return
            move = states_moves[self.get_value(self.current_token)]
            if(move == 'Synch'):
                self.handle_synch_error()
            else:
                self.apply_rule(move[::-1])


    def get_next_input(self):
        token = self.scanner.get_next_token()
        while token[0] in {'WHITESPACE', 'COMMENT'}:
            token = self.scanner.get_next_token()
        self.current_token = token

    def apply_rule(self, rule_tokens):
        self.parse_stack.pop()
        self.parse_stack = self.parse_stack + rule_tokens
        self.tree_rules.append(rule_tokens[::-1])

    def accept_token(self):
        self.parse_stack.pop()
        self.tree_rules.append(self.current_token[1])
        self.get_next_input()

    def accept_epsilon(self):
        self.parse_stack.pop()
        self.tree_rules.append('epsilon')

    def handle_synch_error(self):
        print('SYNCH ERROR')

        term = self.parse_stack.pop()
        error = (self.scanner.line_no, 'missing ' + str(term))
        self.errors.append(error)

    def handle_terminal_error(self):
        print('TERM ERROR')
        expected_token = self.parse_stack[::-1][0]
        error = (self.scanner.line_no, 'missing ', str(expected_token))
        self.errors.append(error)
        self.parse_stack.pop()

    def handle_empty_error(self):
        print('MPT ERROR')

        error = (self.scanner.line_no, 'illegal ' + str(self.current_token[0]))
        self.errors.append(error)
        self.get_next_input()

    def get_value(self, token):
        return token[1] if token[0] in {'KEYWORD', 'SYMBOL', 'EOF'} else token[0]
            
        