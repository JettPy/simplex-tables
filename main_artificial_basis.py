from ArtificialBasis import ArtificialBasis

variables_count = 0
while True:
    print('Enter count of variables:')
    buffer = input()
    try:
        variables_count = int(buffer)
        if variables_count < 1:
            raise ValueError
        break
    except ValueError:
        print('Enter natural integer')
        continue
equations_count = 0
while True:
    print('Enter count of equations:')
    buffer = input()
    try:
        equations_count = int(buffer)
        if equations_count < 1:
            raise ValueError
        break
    except ValueError:
        print('Enter natural integer')
        continue
matrix_a = []
matrix_b = []
matrix_c = []
signs = []
k = 1
while k <= equations_count:
    print('Enter {} coefficients, equality sign and free term for the equation {}:'.format(variables_count, k))
    buffer = input()
    equation = buffer.split()
    if len(equation) < variables_count + 2:
        print('Too few arguments')
        continue
    elif len(equation) > variables_count + 2:
        print('Too many arguments')
        continue
    matrix_a_row = []
    try:
        for i in range(variables_count):
            a = int(equation[i])
            matrix_a_row.append(a)
    except ValueError:
        print('Enter integers for coefficients')
        matrix_a_row.clear()
        continue
    matrix_a.append(matrix_a_row)
    sign = equation[variables_count]
    if sign != '>=' and sign != '==' and sign != '<=':
        print('Enter ">=", "<=", or "==" for sign')
        continue
    else:
        signs.append(sign)
    try:
        b = int(equation[variables_count + 1])
        matrix_b.append(b)
    except ValueError:
        print('Enter integer for free term')
        continue
    k += 1
while True:
    print('Enter {} coefficients for object function:'.format(variables_count))
    buffer = input()
    equation = buffer.split()
    if len(equation) < variables_count:
        print('Too few arguments')
        continue
    elif len(equation) > variables_count:
        print('Too many arguments')
        continue
    try:
        for i in range(variables_count):
            c = int(equation[i])
            matrix_c.append(c)
    except ValueError:
        print('Enter integers for coefficients')
        continue
    break
is_maximize = None
while True:
    print('Maximize? (y/n)')
    buffer = input()
    if buffer != 'y' and buffer != 'n':
        print('Enter "y" for "yes" or "n" for "no"')
        continue
    elif buffer == 'y':
        is_maximize = True
    else:
        is_maximize = False
    break
for i in range(equations_count):
    if matrix_b[i] < 0:
        for j in range(variables_count):
            matrix_a[i][j] = -matrix_a[i][j]
        matrix_b[i] = -matrix_b[i]
        if signs[i] == '>=':
            signs[i] = '<='
        elif signs[i] == '<=':
            signs[i] = '>='
table = ArtificialBasis(matrix_a, matrix_b, matrix_c, signs, is_maximize)
print('Initial:')
table.print()
count = 1
while table.can_be_iterated():
    print('Step {}:'.format(count))
    table.iterate()
    table.print()
    count += 1
print('Drop G:')
table.drop_artificial_function()
table.print()
while table.can_be_iterated():
    print('Step {}:'.format(count))
    table.iterate()
    table.print()
    count += 1
print('X vector:')
for element in table.get_vector_answer():
    print('{:>6}'.format(str(element)), end=' ')
print()
if is_maximize:
    print('Max Z: {}'.format(str(table.get_function_answer())))
else:
    print('Min Z: {}'.format(str(table.get_function_answer())))
