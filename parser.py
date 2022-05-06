from scanner import Scanner
from anytree import Node, RenderTree


class Parser:
    def __init__(self, scanner:Scanner, parse_table):
        self.scanner = scanner
        self.parse_table = parse_table
        self.parse_stack = ['Program']
        self.tree_rules = []
        self.errors = []
        self.tree_root = Node('Program')
        self.tree_stack = [self.tree_root]
        self.get_next_input()


    def parse(self):
        while(len(self.parse_stack) != 0):
            self.proceed()
        self.write_errors()
        self.write_parse_tree()


    def proceed(self):
        # print(self.current_token, self.parse_stack)
        if self.parse_stack[-1] == 'Epsilon':
            working_node = self.tree_stack.pop(0)
            working_node.name = 'epsilon'
            self.accept_epsilon()
        elif self.parse_stack[-1] == self.get_token_value(self.current_token):
            working_node = self.tree_stack.pop(0)
            # print(self.current_token)
            working_node.name = self.current_token
            self.accept_token()
        else:
            if self.parse_stack[-1] not in self.parse_table.keys():
                self.handle_terminal_error()
                return
            states_moves = self.parse_table[self.parse_stack[-1]]
            if self.get_token_value(self.current_token) not in states_moves:
                # print(self.get_token_value(self.current_token))
                self.handle_empty_error()
                return
            move = states_moves[self.get_token_value(self.current_token)]
            if(move == ['Synch']):
                working_node = self.tree_stack.pop(0)
                working_node.parent = None
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
        l = self.tree_stack.pop(0)
        # print(list(reversed(rule_tokens)))
        self.tree_stack = [Node(r, parent=l) for r in list(reversed(rule_tokens))] + self.tree_stack
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
        expected_token = self.parse_stack.pop()
        working_node = self.tree_stack.pop(0)
        working_node.parent = None
        error = (self.scanner.line_no, 'missing ' + str(expected_token))
        self.errors.append(error)


    def handle_empty_error(self):
        print('MPT ERROR')
        error = (self.scanner.line_no, 'illegal ' + str(self.get_token_value(self.current_token)))
        self.errors.append(error)
        self.get_next_input()


    def get_token_value(self, token):
        return token[1] if token[0] in {'KEYWORD', 'SYMBOL', 'EOF'} else token[0]
    

    def write_errors(self):
        file = open('syntax_errors.txt', 'w')
        if self.errors:
            formatted_error = map(lambda error: '#{0} : syntax error, {1}'.format(*error), self.errors)
            file.write("\n".join(formatted_error))
        else:
            file.write("There is no syntax error.")
        file.close()

    def write_parse_tree(self):
        with open('parse_tree.txt', 'w', encoding='utf-8') as f:
            for pre, _, node in RenderTree(self.tree_root):
                f.write(f"{pre}{node.name}\n".replace("\'",""))
