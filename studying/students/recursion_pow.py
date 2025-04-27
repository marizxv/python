
def recursion_degree(number, degree):
    if degree == 0:
        return 1
    elif degree < 0:
        return 1 / number * recursion_degree(number, degree + 1)
    else:
        #for better readability it is better to wrap to a new line
        return number * recursion_degree(number, degree - 1)

x = input('Input number: ')
while True: #added not to re-run the code manually every time – was easier for me to test;
    n = input('Input degree: ')
    if n == '':
        break
    result = recursion_degree(number = int(x), degree = int(n)) #x|n replaced to int(x)|int(n) to handle empty input above
    print('Result:', result)

 # I replaced 'x' with 'number' – suggested that 'x' was meant to be the 'number';
 ## I don't see a replacement
 # no idea why it worked with 'x' – did function accept it from the input, i.e. the global scope?
 ## I corrected it so that it would be clearly visible why it works (line 16)
 ## the function does not expect the variable `number`,
 ## whatever comes to it as the first value will be perceived as `number`
 # Isn't it normally a bad practice?
 ## I don't know why, but python considers the same variable names in a function and outside of it as bad practice

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