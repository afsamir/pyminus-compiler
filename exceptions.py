class InvalidInputException(Exception):
    def __init__(self, expression=''):
        super().__init__()
        self.message = "Invalid input"
        self.expression = expression

class UnclosedCommentException(Exception):
    def __init__(self, expression=''):
        super().__init__()
        self.message = "Unclosed comment"
        self.expression = expression[:10] + '...'

class UnmatchedCommentException(Exception):
    def __init__(self, expression='*/'):
        super().__init__()
        self.message = "Unmatched comment"
        self.expression = expression

class InvalidNumberException(Exception):
    def __init__(self, expression=''):
        super().__init__()
        self.message = "Invalid number"
        self.expression = expression
        