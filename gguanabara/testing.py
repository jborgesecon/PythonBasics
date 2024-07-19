import pandas as pd
import os
import random as rd
import dataValid as dv
import time


m_list = list()
par = ['(', ')']
obj = input('Type any expression containing parentheses: ')
for i in range(len(obj)):
    if obj[i] in par:
        m_list.append(obj[i])
print('Extracting parentheses:', '\n', m_list)
openning = list()
closing = list()

for i in range(len(m_list)):
    if m_list[i] == par[0]:
        openning.append(m_list[i])
    elif m_list[i] == par[1]:
        closing.append(m_list[i])
    else:
        print('Error!')

print('Opening Parentheses:', openning)
print('Closing Parentheses:', closing)
print('\n')
print('Checking if balanced...')

for i in range(6):
    print('.')
    time.sleep(1)

print('\n')

if len(openning) != len(closing):
    print('Unbalanced!')
elif m_list[0] == par[1]:
    print('Unbalanced!')
elif m_list[-1] == par[0]:
    print('Unbalanced!')


m_list2 = '(())()' #(()(()))(()(()))(()()(())()()())()())))(()()()))))))(((((())('
balanced = list()
o = False
for i in len(m_list2):
    if o:
        print('unbalanced')
        break
    elif not balanced:
        if m_list2[i] == par[1]:
            o = True
            break
    #     else:
    #         balanced.append(m_list2[i])
    # elif m_list2[i]:

# ((())()(()(()))(()(()))(()()(())()()())()())))(()()()))))))(((((())(

# adiciona primeiro parenteses
# checa segundo parenteses, se abre, adiciona, se fecha remove 1, se não pode remover por estar vazio, unbalanced, 
# se no final não estiver vazia, unbalanced

