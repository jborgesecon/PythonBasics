user_response = input('Type an expression with parentheses: ')
parentheses = ('(', ')')
alter = True

cleaned_response = list()
for char in user_response:
    if char in parentheses:
        cleaned_response.append(char)

if cleaned_response[0] == parentheses[1] or cleaned_response[-1] == parentheses[0]:
    alter = False
else:
    stack = []


if alter:
    print('balanced')
else:
    print('unbalanced')

