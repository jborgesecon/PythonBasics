import random as rd

while True:
    initial_list = list()

    for i in range(9):
        initial_list.append(rd.randint(0, 9))

    o = 1
    n = 0
    value = 0
    for i in range(len(initial_list)):
        n -= 1
        o += 1
        value += initial_list[n] * o
        print(value)

    digito1 = value % 11

    if digito1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - digito1

    initial_list.append(digito1)

    o = 1
    n = 0
    value = 0
    for i in range(len(initial_list)):
        n -= 1
        o += 1
        value += initial_list[n] * o
        print(value)


    digito2 = value % 11
    if digito2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - digito2

    initial_list.append(digito2)

    print('\n')
    print(initial_list)
    # print(value)
    print('\n')
    for i in range(9):
        print(initial_list[i], end='')
        if i == 2 or i == 5:
            print('.', end='')
    print('-', end='')
    print(initial_list[9], end='')
    print(initial_list[10])    
    print('\n')

    obj = input('Do you want to generate another CPF? (y/n): ')
    if obj == 'n':
        break
    else:
        continue