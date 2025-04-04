
def recursion_degree(number, degree):
    if degree == 0:
        return 1
    if degree < 0 :
        return 1 / number * recursion_degree(number, degree + 1)
    else:    return number * recursion_degree(number, degree - 1)

x = int(input('Input number: '))
while True: #added not to re-run the code manually every time – was easier for me to test;
    n = int(input('Input degree: '))
    result = recursion_degree(x, n)
    print('Result:', result)

 # I replaced 'x' with 'number' –  suggested that 'x' was meant to be the 'number';
 # no idea why it worked with 'x' – did function accept it from the input, i.e. the global scope?
 # Isn't it normally a bad practice?

 # For the negative power I needed to use the same method as for the positive one,
 # but with dividing '1' by what would recursion_degree() normally give;
 # in recursion, parameter of the degree decreases (with negative one increases)
 # until it reaches zero, because it's the condition to stop the "digging" process.
 # The 'if degree == 0', aka 'stop' sign, condition would be triggered as soon as
 # power reached '0', leaving this abomination in memory:
 # xn * ( xn-1 * (... x2 * ( x1 * f(0) )...))
 # where f(0) is the most nested function, and it would return '1'.
 # Pretty much it's the 'number' to the power of 0. After that 'number' would be multiplied
 # by itself exactly as many times as the recursion took place – 'degree' times.