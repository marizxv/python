
def recursion_degree(number, degree):
    if degree == 0:
        return 1
    return x * recursion_degree(number, degree - 1)

x = int(input('Input number: '))
n = int(input('Input degree: '))
result = recursion_degree(x, n)
print('Result:', result)