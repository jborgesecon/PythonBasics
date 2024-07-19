import menu_gguanabara as mg
import pandas as pd
import dataValid as dv


error_msg = 'Type a value within the range!'
exit = '0 -> EXIT'
go_back = '0 -> GO BACK'
dv.header('Welcome to the Program!')

while True:
    try:
        dv.sepper(' MAIN MENU ', '.')
        print('\n')

        for i in range(len(mg.dict_n1['lvl zero'])):
            if i < 10:
                print(f'0{i + 1} -> {mg.dict_n1["lvl zero"][i]}')
            else:
                print(f'{i + 1} -> {mg.dict_n1["lvl zero"][i]}')
        print(exit)

        print('\n')
        while True:
            try:
                nav1 = dv.intValid(input('Choose the desired class: '))
                break
            except ValueError:
                print(error_msg)
        if nav1 == 0:
            print('\n')
            print('Thanks for trying this code!')
            print('\n')
            break
        
        print('\n')
        current_mundo = mg.dict_n1['lvl zero'][nav1-1]
        dv.sepper(current_mundo, '.')
        print('\n')

        for i in range(len(mg.dict_n2[f'lvl{nav1}'])):
            if i < 9:
                print(f'0{i + 1} -> ', mg.dict_n2[f'lvl{nav1}'][i])
            else:
                print(f'{i + 1} -> ', mg.dict_n2[f'lvl{nav1}'][i])
        print(go_back)
        print('\n')

        while True:
            try:
                nav2 = dv.intValid(input('Choose the desired Episode: '))
                break
            except ValueError:
                print(error_msg)
        
        while True:
            if nav2 != 0:    
                current_ep = mg.dict_n2[f'lvl{nav1}'][nav2 - 1]
                dv.sepper(current_ep, '.')
                print('\n')

                current_tasks_list = list(mg.Main[current_mundo][current_ep].keys())
                while True:
                    try:
                        o = 1
                        for i in current_tasks_list:
                            if o < 10:
                                print(f'0{o} -> {i}')
                                o += 1
                            else:
                                print(f'{o} -> {i}')
                                o += 1
                        print(go_back)

                        print('\n')

                        while True:
                            try:
                                nav3 = dv.intValid(input('What task do you want to try: '))
                                break
                            except ValueError:
                                print(error_msg)

                        if nav3 == 0 :
                            break

                        else:
                            print('\n')
                            chosen = mg.Main[current_mundo][current_ep][current_tasks_list[nav3-1]]

                            while True:
                                if callable:
                                    chosen()
                                else:
                                    print(chosen)
                                print('\n')
                                nav4 = dv.yn_valid(input('Want to try this task again? [y/n]: '))
                                if nav4 == 'n':
                                    break
                            print('\n')
                            print('this code is working so far')

                            break
                    except ValueError:
                        print(error_msg)
                if nav3 == 0 :
                    break
            else:
                break
    except ValueError:
        print(error_msg)

