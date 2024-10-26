from mundo3 import *


# Defining main menu:
Main = {
    'Mundo 1': None,
    'Mundo 2': None,
    'Mundo 3': None
}

# Defining Sublevels:
mundo_1 = {
    'Episode 1': None,
    'Episode 2': None,
    'Episode 3': None,
    'Episode 4': None,
    'Episode 5': None,
    'Episode 6': None,
    'Episode 7': None,
    'Episode 8': None,
    'Episode 9': None,
    'Episode 10': None,
    'Episode 11': None
}

mundo_2 = {
    'Episode 12': None,
    'Episode 13': None,
    'Episode 14': None,
    'Episode 15': None,
}

mundo_3 = {
    'Episode 16': None,
    'Episode 17': None,
    'Episode 18': None,
    'Episode 19': None,
    'Episode 20': None,
    'Episode 21': None,
    'Episode 22': None,
    'Episode 23': None
}


# Defining Episodes:
ep_1 = {
    'generic': generic_print
}

ep_2 = {
    'generic': generic_print
}

ep_3 = {
    'generic': generic_print
}

ep_4 = {
    'generic': generic_print
}

ep_5 = {
    'generic': generic_print
}

ep_6 = {
    'generic': generic_print
}

ep_7 = {
    'generic': generic_print
}

ep_8 = {
    'generic': generic_print
}

ep_9 = {
    'generic': generic_print
}

ep_10 = {
    'generic': generic_print
}

ep_11 = {
    'generic': generic_print
}

ep_12 = {
    'generic': generic_print
}

ep_13 = {
    'generic': generic_print
}

ep_14 = {
    'generic': generic_print
}

ep_15 = {
    'generic': generic_print
}

ep_16 = {
    'Number Names (e72)': number_names,
    'Standings (e73)': standings,
    'Five Random Numbers (e74)': fv_randNums,
    'Tuple Values (e75)': tuple_values,
    'Shopping List (e76)': shopping_list,
    'Finding Vowels (e77)': tuple_vowels
}

ep_17 = {
    'List Values 1 (e78)': list_num_order,
    'Unique Ordered List (e79)': unique_ordered_list,
    'Ordered List 2 (e80)': unlimited_list,
    'Ordered List 3 (e81)': ordered_list_i,
    'Even x Odd list (e82)': even_odd_list,
    'Balanced Parentheses (e83)': checkBalanced
}

ep_18 = {
    'Weigth List (e84)': weigthCheck,
    'Even x Odd 2 (e85)': even_odd_2,
    '3 x 3 Matrix (e86 + e87)': tbt_matrix,
    'Lottery (e88)': lottery_games,
    'Grades (e89)': grades
}

ep_19 = {
    'generic': generic_print
}

ep_20 = {
    'generic': generic_print
}

ep_21 = {
    'generic': generic_print
}

ep_22 = {
    'generic': generic_print
}

ep_23 = {
    'generic': generic_print
}

# Unify all objects:
mundo_1['Episode 1'] = ep_1
mundo_1['Episode 2'] = ep_2
mundo_1['Episode 3'] = ep_3
mundo_1['Episode 4'] = ep_4
mundo_1['Episode 5'] = ep_5
mundo_1['Episode 6'] = ep_6
mundo_1['Episode 7'] = ep_7
mundo_1['Episode 8'] = ep_8
mundo_1['Episode 9'] = ep_9
mundo_1['Episode 10'] = ep_10
mundo_1['Episode 11'] = ep_11

mundo_2['Episode 12'] = ep_12
mundo_2['Episode 13'] = ep_13
mundo_2['Episode 14'] = ep_14
mundo_2['Episode 15'] = ep_15

mundo_3['Episode 16'] = ep_16
mundo_3['Episode 17'] = ep_17
mundo_3['Episode 18'] = ep_18
mundo_3['Episode 19'] = ep_19
mundo_3['Episode 20'] = ep_20
mundo_3['Episode 21'] = ep_21
mundo_3['Episode 22'] = ep_22
mundo_3['Episode 23'] = ep_23

Main['Mundo 1'] = mundo_1
Main['Mundo 2'] = mundo_2
Main['Mundo 3'] = mundo_3

# Create dictionaries for list Navigation:
dict_n1 = {
    'lvl zero': list(Main.keys())
}

dict_n2 = {}
dict_n3 = {}

o = 1
for i, section in enumerate(Main.keys(), start= 1):     
    dict_n2[f'lvl{i}'] = list(Main[section].keys())
    for section2 in Main[section].keys():
        dict_n3[f'lvl{o}'] = list(Main[section][section2].keys())
        o += 1

# Main['Mundo 1']['Episode 1']['Number Names (e1)']()
