parse_table = {
    'Program': {
        '$': ['Statements'],
        'break': ['Statements'],
        'continue': ['Statements'],
        'ID': ['Statements'],
        'return': ['Statements'],
        'global': ['Statements'],
        'def': ['Statements'],
        'if': ['Statements'],
        'while': ['Statements'],
        },
    'Statements': {
        '$': ['Epsilon'],
        ';': ['Epsilon'],
        'break': ['Statement', ';', 'Statements'],
        'continue': ['Statement', ';', 'Statements'],
        'ID': ['Statement', ';', 'Statements'],
        'return': ['Statement', ';', 'Statements'],
        'global': ['Statement', ';', 'Statements'],
        'def': ['Statement', ';', 'Statements'],
        'if': ['Statement', ';', 'Statements'],
        'else': ['Epsilon'],
        'while': ['Statement', ';', 'Statements'],
        },
    'Statement': {
        ';': ['Synch'],
        'break': ['Simple_stmt'],
        'continue': ['Simple_stmt'],
        'ID': ['Simple_stmt'],
        'return': ['Simple_stmt'],
        'global': ['Simple_stmt'],
        'def': ['Compound_stmt'],
        'if': ['Compound_stmt'],
        'while': ['Compound_stmt'],
        },
    'Simple_stmt': {
        ';': ['Synch'],
        'break': ['break'],
        'continue': ['continue'],
        'ID': ['Assignment_Call'],
        'return': ['Return_stmt'],
        'global': ['Global_stmt'],
        },
    'Compound_stmt': {
        ';': ['Synch'],
        'def': ['Function_def'],
        'if': ['If_stmt'],
        'while': ['Iteration_stmt'],
        },
    'Assignment_Call': {';': ['Synch'], 'ID': ['ID', 'B']},
    'B': {
        ';': ['Synch'],
        '=': ['=', 'C'],
        '[': ['[', 'Expression', ']', '=', 'C'],
        '(': ['(', 'Arguments', ')'],
        },
    'C': {
        ';': ['Synch'],
        'ID': ['Expression'],
        '[': ['[', 'Expression', 'List_Rest', ']'],
        'NUM': ['Expression'],
        },
    'Return_stmt': {';': ['Synch'], 'return': ['return', 'Return_Value'
                    ]},
    'Global_stmt': {';': ['Synch'], 'global': ['global', 'ID']},
    'Function_def': {';': ['Synch'], 'def': [
        'def',
        'ID',
        '(',
        'Params',
        ')',
        ':',
        'Statements',
        ]},
    'If_stmt': {';': ['Synch'], 'if': ['if', 'Relational_Expression',
                ':', 'Statements', 'Else_block']},
    'Iteration_stmt': {';': ['Synch'], 'while': ['while', '(',
                       'Relational_Expression', ')', 'Statements']},
    'Expression': {
        ';': ['Synch'],
        'ID': ['Term', 'Expression_Prime'],
        ']': ['Synch'],
        ')': ['Synch'],
        ',': ['Synch'],
        ':': ['Synch'],
        '==': ['Synch'],
        '<': ['Synch'],
        'NUM': ['Term', 'Expression_Prime'],
        },
    'Term': {
        ';': ['Synch'],
        'ID': ['Factor', 'Term_Prime'],
        ']': ['Synch'],
        ')': ['Synch'],
        ',': ['Synch'],
        ':': ['Synch'],
        '==': ['Synch'],
        '<': ['Synch'],
        '+': ['Synch'],
        '-': ['Synch'],
        'NUM': ['Factor', 'Term_Prime'],
        },
    'Factor': {
        ';': ['Synch'],
        'ID': ['Atom', 'Power'],
        ']': ['Synch'],
        ')': ['Synch'],
        ',': ['Synch'],
        ':': ['Synch'],
        '==': ['Synch'],
        '<': ['Synch'],
        '+': ['Synch'],
        '-': ['Synch'],
        '*': ['Synch'],
        'NUM': ['Atom', 'Power'],
        },
    'Atom': {
        ';': ['Synch'],
        'ID': ['ID'],
        '[': ['Synch'],
        ']': ['Synch'],
        '(': ['Synch'],
        ')': ['Synch'],
        ',': ['Synch'],
        ':': ['Synch'],
        '==': ['Synch'],
        '<': ['Synch'],
        '+': ['Synch'],
        '-': ['Synch'],
        '*': ['Synch'],
        '**': ['Synch'],
        'NUM': ['NUM'],
        },
    'Return_Value': {';': ['Epsilon'], 'ID': ['Expression'],
                     'NUM': ['Expression']},
    'Else_block': {';': ['Epsilon'], 'else': ['else', ':', 'Statements'
                   ]},
    'Expression_Prime': {
        ';': ['Epsilon'],
        ']': ['Epsilon'],
        ')': ['Epsilon'],
        ',': ['Epsilon'],
        ':': ['Epsilon'],
        '==': ['Epsilon'],
        '<': ['Epsilon'],
        '+': ['+', 'Term', 'Expression_Prime'],
        '-': ['-', 'Term', 'Expression_Prime'],
        },
    'Term_Prime': {
        ';': ['Epsilon'],
        ']': ['Epsilon'],
        ')': ['Epsilon'],
        ',': ['Epsilon'],
        ':': ['Epsilon'],
        '==': ['Epsilon'],
        '<': ['Epsilon'],
        '+': ['Epsilon'],
        '-': ['Epsilon'],
        '*': ['*', 'Factor', 'Term_Prime'],
        },
    'Power': {
        ';': ['Primary'],
        '[': ['Primary'],
        ']': ['Primary'],
        '(': ['Primary'],
        ')': ['Primary'],
        ',': ['Primary'],
        ':': ['Primary'],
        '==': ['Primary'],
        '<': ['Primary'],
        '+': ['Primary'],
        '-': ['Primary'],
        '*': ['Primary'],
        '**': ['**', 'Factor'],
        },
    'Primary': {
        ';': ['Epsilon'],
        '[': ['[', 'Expression', ']', 'Primary'],
        ']': ['Epsilon'],
        '(': ['(', 'Arguments', ')', 'Primary'],
        ')': ['Epsilon'],
        ',': ['Epsilon'],
        ':': ['Epsilon'],
        '==': ['Epsilon'],
        '<': ['Epsilon'],
        '+': ['Epsilon'],
        '-': ['Epsilon'],
        '*': ['Epsilon'],
        },
    'Params': {'ID': ['ID', 'Params_Prime'], ')': ['Epsilon']},
    'Relational_Expression': {'ID': ['Expression', 'Relop', 'Expression'
                              ], ')': ['Synch'], 'NUM': ['Expression',
                              'Relop', 'Expression']},
    'Relop': {
        'ID': ['Synch'],
        '==': ['=='],
        '<': ['<'],
        'NUM': ['Synch'],
        },
    'Arguments': {'ID': ['Expression', 'Arguments_Prime'], ')': ['Epsilon'
                  ], 'NUM': ['Expression', 'Arguments_Prime']},
    'List_Rest': {']': ['Epsilon'], ',': [',', 'Expression', 'List_Rest'
                  ]},
    'Params_Prime': {')': ['Epsilon'], ',': [',', 'ID', 'Params_Prime'
                     ]},
    'Arguments_Prime': {')': ['Epsilon'], ',': [',', 'Expression',
                        'Arguments_Prime']},
    }
