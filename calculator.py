i = 0
while i < 1 :
    equation = input('')
    if '+' in equation :
        midle = equation.find('+')
        num1 = float(equation[0:midle])
        num2 = float(equation[midle + 1:len(equation)])
        print('')
        print(num1 + num2)

    if '-' in equation :
        midle = equation.find('-')
        num1 = float(equation[0:midle])
        num2 = float(equation[midle + 1:len(equation)])
        print('')
        print(num1 - num2)

    if '*' in equation :
        midle = equation.find('*')
        num1 = float(equation[0:midle])
        num2 = float(equation[midle + 1:len(equation)])
        print('')
        print(num1 * num2)

    if '/' in equation :
        midle = equation.find('/')
        num1 = float(equation[0:midle])
        num2 = float(equation[midle + 1:len(equation)])
        print(' ')
        print(num1 / num2)

    if '^' in equation :
        midle = equation.find('^')
        num1 = float(equation[0:midle])
        num2 = float(equation[midle + 1:len(equation)])
        print('')
        print(num1 ** num2)

    print('--------------------------------------------')
