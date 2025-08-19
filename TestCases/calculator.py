from operator import add, mul, truediv

from reduce import reduce

def calc_eval(exp):
    if type(exp) in (int, float):
        # number evaluates to itself
        return exp
    elif isinstance(exp, Pair):
        # call experssion evaluates to its argument values combined by an operator
        arguments = exp.second.map(calc_eval)
        return calc_apply(exp.first, arguments)
    else:
        raise TypeError(exp + 'is not a valid expression')
    
def calc_apply(operator, args):
    if operator == '+':
        return reduce(add, args, 0)
    if ...:
        pass

def read_eval_print_loop():
    """ run a real-eval-print loop for calculator"""
    while True:
        try:
            src = buffer_input()
            while src.more_on_line:
                expression = scheme_read(src)
                print(calc_eval(expression))
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print('Calculation completed.')
            return 0