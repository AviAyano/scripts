class FactorialArgumentError(Exception):

    def __init__(self, arg):
        self._arg=arg
    def __str__(self):
        return"Provided argument %s is not a positive interger." %(self._arg)

    def get_arg(self):
        return self._arg

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise FactorialArgumentError(n)

    facto = 1
    for i in range(n, 0, -1):
        facto = facto * i
    return facto


if __name__ == '__main__':
    print(factorial((input('Enter a integer number please: '))))