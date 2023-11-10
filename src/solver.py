"""
This module is used to solve an algebraic expression.
The expression must be input as a string, and contain only
integers, spaces, and +-*/ operators.
"""
import sys


def solve(text_equation: str) -> str:
    check_input(text_equation)
    list_parts = text_equation.split(' ')

    while len(list_parts) > 1:
        list_parts = do_step(list_parts)

    result = list_parts[0]
    return proper_format(result)


def check_input(text_equation: str):
    # Check beginning
    if text_equation[0] not in '0123456789':
        raise Exception("Invalid format. Input cannot start with {}. It must "
                        "start with an integer".format(text_equation[0]))
    # Check end
    if text_equation[-1] not in '0123456789':
        raise Exception("Invalid format. Input cannot end with {}. It must "
                        "start with an integer".format(text_equation[-1]))

    permitted_characters = '0123456789+-*/ '
    i = 0
    for character in text_equation:
        if character in '+-*/':
            # Check for spaces around operators
            if text_equation[i - 1] != ' ' and text_equation[i + 1] != ' ':
                raise Exception("Invalid format. {} should be "
                                "surrounded by spaces".format(character))
            # Check for digits following operators
            if text_equation[i + 2] not in '0123456789':
                raise Exception("Invalid format. Expected a digit at index {}"
                                "following {} operator.".format((i + 2),
                                                                character))
        # Check for invalid characters
        if character not in permitted_characters:
            raise Exception("Invalid input detected: {}. Input must contain only"
                            "integers, spaces, and + - * or / operators."
                            .format(character))

        i += 1


def do_step(list_parts: list[str]) -> list[str]:
    # Do a single step of the expression at a time according to PEMDAS,
    # then return the list to the main function.

    # Once the operator is found, the single expression is performed.
    # The result of the operation is then inserted, and the expression
    # is cleared from the list
    for i in range(0, len(list_parts)):
        if list_parts[i] == '*' or list_parts[i] == '/':
            if list_parts[i] == '*':
                product = float(list_parts[i - 1]) * float(list_parts[i + 1])
                list_parts[i] = str(round(product, 2))
                del list_parts[i + 1]
                del list_parts[i - 1]
                return list_parts
            else:
                try:
                    quotient = float(list_parts[i - 1]) / float(list_parts[i + 1])
                    list_parts[i] = str(round(quotient, 2))
                    del list_parts[i + 1]
                    del list_parts[i - 1]
                    return list_parts
                except ZeroDivisionError as e:
                    print('This program detected a {}, the expression is not solvable.'.format(e))
                    expression = ''
                    for part in list_parts:
                        expression += part + ' '
                    print('Current expression'.format(expression[:-1]))
                    sys.exit()

    for i in range(0, len(list_parts)):
        if list_parts[i] == '+' or list_parts[i] == '-':
            if list_parts[i] == '+':
                summation = float(list_parts[i - 1]) + float(list_parts[i + 1])
                list_parts[i] = str(round(summation, 2))
                del list_parts[i + 1]
                del list_parts[i - 1]
                return list_parts
            else:
                difference = float(list_parts[i - 1]) - float(list_parts[i + 1])
                list_parts[i] = str(round(difference, 2))
                del list_parts[i + 1]
                del list_parts[i - 1]
                return list_parts


def proper_format(number: str) -> str:
    result = str(round(float(number), 2))
    if len(result.split('.')[1]) != 2:
        result += '0'

    return result

