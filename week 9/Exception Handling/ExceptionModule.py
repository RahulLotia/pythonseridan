#user-defined exceptions

class Error(Exception):
    pass

class NumberTooSmallError(Error):
    def __str__(self):
        return 'The number you guessed is too small'

class NumberTooHighError(Error):
    def __str__(self):
        return 'The number you guessed is too high'