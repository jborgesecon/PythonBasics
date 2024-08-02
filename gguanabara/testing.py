# import pandas as pd
# import os
# import random as rd
# import dataValid as dv
# import time


obj = input('Type an expression with parentheses: ')
par = ('(', ')')

ss1 = list()
for i in range(len(obj)):
    if obj[i] in par:
        ss1.append(obj[i])

balanced = False
bal = list()



print(balanced)