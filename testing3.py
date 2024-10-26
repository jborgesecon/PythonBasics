from gguanabara import dataValid as dv
import random as rd
from faker import Faker
import numpy as np


fake = Faker()

student_class = []
print('\n')
students = dv.intValid(input('Type the amount of students: '))

for i in range(students):
    grade = []
    name = fake.name()
    print(f"The student's name is {name}")
    print('\n')
    for ii in range(1,3):
        while True:
            score = dv.floatValid(input(f"Type the {ii}° {name}'s score -> "))
            if score >= 0 and score <=10:
                break
            else:
                print('Type a value between 0 and 10', '\n')
            grade.append(score)
    adding = [name, grade]
    student_class.append(adding)
    print('\n')

print(30*'-')
msg = 'STUDENTS GRADES'
print(f'{msg:^30}')
print(30*'-')
print('\n')

grade = [
    ['Tony', [6.3, 4.8]],
    ['Amanda', [2.1, 9.8]]
]

titles = ['No.', 'Name', 'Final Score']
print(f'{titles[0]:<}', f'{titles[1]:^}', f'{titles[2]:>}')#, limit=30)
print(30*'-')
for std in grade:
    print(f'{grade.index(std):.<30} {std[0]:^7} {np.average(std)}')