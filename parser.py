from scanner import Scanner


class Parser:
    def __init__(self, scanner:Scanner, parse_table):
        self.scanner = scanner
        self.parse_table = parse_table
        self.parse_stack = ['Program']
        self.tree_rules = []
        self.get_next_input()

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
        terminal = self.parse_stack.pop()
        self.tree_rules.append(self.current_token[1])
        print(self.current_token)
        self.get_next_input()

    def proceed(self):
        # print('__________________________________________________________________________')
        print(self.current_token, self.parse_stack)
        # print(self.current_token[0])
        # print(self.parse_table[self.current_token[0]])
        # print('__________________________________________________________________________')
        if(self.current_token[0] == self.parse_stack[-1]):
            self.accept_token()
        elif self.parse_stack[-1] == 'Epsilon':
            self.parse_stack.pop()
        else:
            move = self.parse_table[self.current_token[0]][self.parse_stack[-1]]
            if(move):
                self.apply_rule(move[::-1])
            else:
                raise Exception()

    def parse(self):
        while(len(self.parse_stack) is not 0 and self.current_token[0] is not 'EOF'):
            self.proceed()
