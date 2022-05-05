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
        while(len(self.parse_stack) is not 0 and self.current_token[0] is not '$'):
            self.proceed()


    def proceed(self):
        print(self.current_token, self.parse_stack)
        if(self.current_token[0] == self.parse_stack[-1]):
            self.accept_token()
        elif self.parse_stack[-1] == 'Epsilon':
            self.parse_stack.pop()
        else:
            try:
                move = self.parse_table[self.parse_stack[-1]][self.current_token[0]]
                if(move):
                    if(move == 'Synch'):
                        self.handle_synch_error()
                    else:
                        self.apply_rule(move[::-1])
            except :
                self.handle_empty_error()


    def get_next_input(self):
        token = self.scanner.get_next_token()
        while token[0] in {'WHITESPACE', 'COMMENT'}:
            token = self.scanner.get_next_token()
        if token[0] in {'KEYWORD', 'SYMBOL', 'EOF'}:
            token = token[1], token[1]
        self.current_token = token

    def apply_rule(self, rule_tokens):
        self.parse_stack.pop()
        self.parse_stack = self.parse_stack + rule_tokens
        self.tree_rules.append(rule_tokens[::-1])

    def accept_token(self):
        self.parse_stack.pop()
        self.tree_rules.append(self.current_token[1])
        print(self.current_token)
        self.get_next_input()

    def handle_synch_error(self):
        term = self.parse_stack.pop()
        error = (self.scanner.line_no, 'missing' + str(term))
        self.errors.append(error)

    def handle_empty_error(self):
        error = (self.scanner.line_no, 'missing')
        self.errors.append(error)
        self.get_next_input()

