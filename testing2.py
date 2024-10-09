from gguanabara import dataValid as dv


rows = 3
cols = 3

matrix = list()
sep = [
    [], # evens
    []  # odds
]

for row in range(rows):
    n_row = []
    matrix.append(n_row)
    for col in range(cols):
        o = dv.intValid(input(f'Type a number for position [{row}, {col}] -> '))
        matrix[row].append(o)

for row in range(rows):
    for col in range(cols):
        print(f'[ {matrix[row][col]} ] ', end='')
    print('')

for row in range(rows):
    for col in range(cols):
        result = matrix[row][col] % 2
        if result == 0: # even
            call = 0
        else:   # odd
            call = 1
        
        value = matrix[row][col]
        position = str([row, col])
        n_sep = [value, position]
        sep[call].append(n_sep)

print('\n')

print(f'The evens are: ')
print('\n')
total_evens = 0
for evens in sep[0]:
    print(f'value: {evens[0]}; position: {evens[1]}')
    total_evens+=evens[0]
print('\n')
print(f'Sum of Evens = {total_evens}')
print('\n')
print(f'row 1 = {matrix[0]}')
print(f'Sum of row 1 = {sum(matrix[0])}')
print('\n')

row3 = 0
print(f'col 3 = ', end='')
for i in range(len(matrix)):
    print(f'[{matrix[i][2]}] ', end='')
    row3+=matrix[i][2]
print('')
print(f'Sum of colum 3 = {row3}')
print('\n')

# sum of evens
# sum of col 3
# avg of row 1
# highest val of row 2

# print(matrix[0][1])
# print(matrix[1][2])
# print(matrix[2][0])

# So, we have the matrix, now we have to acess it to gather the needed information via algorithm
