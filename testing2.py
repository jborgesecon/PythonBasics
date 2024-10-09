from gguanabara import dataValid as dv


pos = [0,1,2]

matrix = [[],[],[]]

for i in pos:
    for ii in pos:
        value = dv.intValid(input(f'Type the value for position [{i}, {ii}] -> '))
        matrix[i].append(value)

print('\n')
for iii in range(len(matrix)):
    print(f'[{matrix[iii][0]}] [{matrix[iii][1]}] [{matrix[iii][2]}]')