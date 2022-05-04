### author_name, student_no = 'Amir Afsari', 96105575

from scanner import Scanner 
from parser_component import Parser

parse_table = {
            '$': {'Program': ['Statements'], 'Statements': ['Epsilon']},
            ';': {'Statements': ['Epsilon'], 'Return_Value': ['Epsilon'],
                  'Else_block': ['Epsilon'], 'Expression_Prime': ['Epsilon'],
                  'Term_Prime': ['Epsilon'], 'Power': ['Primary'], 'Primary': ['Epsilon']},
            'break': {'Program': ['Statements'], 'Statements': ['Statement', ';', 'Statements'],
                      'Statement': ['Simple_stmt'], 'Simple_stmt': ['break']},
            'continue': {'Program': ['Statements'], 'Statements': ['Statement', ';', 'Statements'],
                         'Statement': ['Simple_stmt'], 'Simple_stmt': ['continue']},
            'ID': {'Program': ['Statements'], 'Statements': ['Statement', ';', 'Statements'],
                   'Statement': ['Simple_stmt'], 'Simple_stmt': ['Assignment_Call'],
                   'Assignment_Call': ['ID', 'B'], 'C': ['Expression'], 'Return_Value': ['Expression'],
                   'Params': ['ID', 'Params_Prime'], 'Relational_Expression': ['Expression', 'Relop', 'Expression'],
                   'Expression': ['Term', 'Expression_Prime'], 'Term': ['Factor', 'Term_Prime'],
                   'Factor': ['Atom', 'Power'], 'Arguments': ['Expression', 'Arguments_Prime'], 'Atom': ['ID']},
            '=': {'B': ['=', 'C']},
            '[': {'B': ['[', 'Expression', ']', '=', 'C'], 'C': ['[', 'Expression', 'List_Rest', ']'],
                  'Power': ['Primary'], 'Primary': ['[', 'Expression', ']', 'Primary']},
            ']': {'List_Rest': ['Epsilon'], 'Expression_Prime': ['Epsilon'], 'Term_Prime': ['Epsilon'],
                  'Power': ['Primary'], 'Primary': ['Epsilon']},
            '(': {'B': ['(', 'Arguments', ')'], 'Power': ['Primary'], 'Primary': ['(', 'Arguments', ')', 'Primary']},
            ')': {'Params': ['Epsilon'], 'Params_Prime': ['Epsilon'], 'Expression_Prime': ['Epsilon'],
                  'Term_Prime': ['Epsilon'], 'Power': ['Primary'], 'Primary': ['Epsilon'], 'Arguments': ['Epsilon'],
                  'Arguments_Prime': ['Epsilon']},
            ',': {'List_Rest': [',', 'Expression', 'List_Rest'], 'Params_Prime': [',', 'ID', 'Params_Prime'],
                  'Expression_Prime': ['Epsilon'], 'Term_Prime': ['Epsilon'], 'Power': ['Primary'],
                  'Primary': ['Epsilon'], 'Arguments_Prime': [',', 'Expression', 'Arguments_Prime']},
            'return': {'Program': ['Statements'], 'Statements': ['Statement', ';', 'Statements'],
                       'Statement': ['Simple_stmt'], 'Simple_stmt': ['Return_stmt'],
                       'Return_stmt': ['return', 'Return_Value']},
            'global': {'Program': ['Statements'], 'Statements': ['Statement', ';', 'Statements'],
                       'Statement': ['Simple_stmt'], 'Simple_stmt': ['Global_stmt'], 'Global_stmt': ['global', 'ID']},
            'def': {'Program': ['Statements'], 'Statements': ['Statement', ';', 'Statements'],
                    'Statement': ['Compound_stmt'], 'Compound_stmt': ['Function_def'],
                    'Function_def': ['def', 'ID', '(', 'Params', ')', ':', 'Statements']},
            ':': {'Expression_Prime': ['Epsilon'], 'Term_Prime': ['Epsilon'], 'Power': ['Primary'],
                  'Primary': ['Epsilon']},
            'if': {'Program': ['Statements'], 'Statements': ['Statement', ';', 'Statements'],
                   'Statement': ['Compound_stmt'], 'Compound_stmt': ['If_stmt'],
                   'If_stmt': ['if', 'Relational_Expression', ':', 'Statements', 'Else_block']},
            'else': {'Statements': ['Epsilon'], 'Else_block': ['else', ':', 'Statements']},
            'while': {'Program': ['Statements'], 'Statements': ['Statement', ';', 'Statements'],
                      'Statement': ['Compound_stmt'], 'Compound_stmt': ['Iteration_stmt'],
                      'Iteration_stmt': ['while', '(', 'Relational_Expression', ')', 'Statements']},
            '==': {'Relop': ['=='], 'Expression_Prime': ['Epsilon'], 'Term_Prime': ['Epsilon'],
                   'Power': ['Primary'], 'Primary': ['Epsilon']},
            '+': {'Expression_Prime': ['+', 'Term', 'Expression_Prime'], 'Term_Prime': ['Epsilon'],
                  'Power': ['Primary'], 'Primary': ['Epsilon']},
            '-': {'Expression_Prime': ['-', 'Term', 'Expression_Prime'], 'Term_Prime': ['Epsilon'],
                  'Power': ['Primary'], 'Primary': ['Epsilon']},
            '*': {'Term_Prime': ['*', 'Factor', 'Term_Prime'], 'Power': ['Primary'], 'Primary': ['Epsilon']},
            '**': {'Power': ['**', 'Factor']},
            'NUM': {'C': ['Expression'], 'Return_Value': ['Expression'],
                    'Relational_Expression': ['Expression', 'Relop', 'Expression'],
                    'Expression': ['Term', 'Expression_Prime'],
                    'Term': ['Factor', 'Term_Prime'], 'Factor': ['Atom', 'Power'],
                    'Arguments': ['Expression', 'Arguments_Prime'], 'Atom': ['NUM']}
        }


scanner = Scanner("input.txt")
parser = Parser(scanner, parse_table)

parser.parse()
