# This is a challenge intended for senior developers. If you do not recognize the syntax here, please
# do not attempt this unless you really want to. You will learn about this later.

# Function Recursion

# A recursive function is one that defined, calls itself directly or indirectly.
# Recursion can be incredibly useful when working on mathematical problems.

# When creating a recursive function you need a base case, or a situation in which the function will return, unrolling
# the stack. Imagine a function calling itself five times. It's path from the original point in the file where it was
# called would be like this:
#
# 0           | origin
# 1  (call)   | origin --> func()
# 2  (call)   | origin --- func() --> func()
# 3  (call)   | origin --- func() --- func() --> func()
# 4  (call)   | origin --- func() --- func() --- func() --> func()
# 5  (call)   | origin --- func() --- func() --- func() --- func() --> func() (now we return after hitting base case)
# 6  (return) | origin --- func() --- func() --- func() --- func() <-- func()
# 7  (return) | origin --- func() --- func() --- func() <-- func()
# 8  (return) | origin --- func() --- func() <-- func()
# 9  (return) | origin --- func() <-- func()
# 10 (return) | origin <-- func()
# 11          | origin

# If you wanted to computer the power of a number without using the the built-in exponentiation functions,
#   you could use a loop like so (integer exponents only):


def power(base, exponent):
    result = 1

    if exponent >= 0:
        for i in range(exponent):
            result *= base
    else:
        for i in range(abs(exponent)):
            result /= base

    return result


flag = False
while not flag:
    try:
        num1 = int(input('>> number    | '))
        num2 = int(input('>> exponent  | '))
        print('\n', power(num1, num2), sep='', end='\n\n')
        flag = True

    except ValueError:
        print('>> please enter a number\n')


# This could be accomplished via a recursive function:

# Note, I have added print functions to showcase the traversal of the recursion.

def power_recursive(base, exponent):
    # base case, if the exponent
    if exponent == 0:
        print('\n>> base case, returning...\n')
        return 1
    else:
        # the exponent is positive, so multiply
        if exponent >= 0:
            print(f'>> calling power_recursive({base, exponent - 1})...')
            result = power_recursive(base, exponent - 1)
            print(f'>> returned from power_recursive({base, exponent - 1})...')
            print(f'>> returning {result} * {base}, or {result * base}')
            return result * base
        else:
            print(f'>> calling power_recursive({base, exponent - 1})...')
            result = power_recursive(base, exponent + 1)
            print(f'>> returned from power_recursive({base, exponent - 1})...')
            print(f'>> returning {result} / {base}, or {result / base}')
            return result / base


flag = False
while not flag:
    try:
        num1 = int(input('>> number    | '))
        num2 = int(input('>> exponent  | '))
        print()
        print('\n', power_recursive(num1, num2), sep='')
        flag = True

    except ValueError:
        print('>> please enter a number\n')


# Notice in the output how it unrolls after reaching the base case. Without it, we would recurse forever, and that's
# going to make the program crash.

# Define a recursive function that will calculate n!, or n factorial.
#   n! = n * n - 1 * n - 2 * ... * 1
#
#   Example: 5! = 5 * 4 * 3 * 2 * 1

# Try doing it in a loop first, you may find that helpful.


def factorial_recursive():
    pass
