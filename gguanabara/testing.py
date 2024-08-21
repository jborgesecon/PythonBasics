# # Chat GPT response

obj = input('Type an expression with parentheses: ')
par = ('(', ')')

def check_balance(expression, parentheses):
    stack = []
    for char in expression:
        if char == parentheses[0]:
            stack.append(char)
        elif char == parentheses[1]:
            if not stack:
                return False
            stack.pop()
    return not stack

if obj[0] == par[1] or obj[-1] == par[0]:
    print('unbalanced')
else:
    if check_balance(obj, par):
        print('balanced')
    else:
        print('unbalanced')

# # My Response:

# obj = input('Type an expression with parentheses: ')
# par = ('(', ')')


# if obj[0] == par[1] or obj[-1] == par[0]:
#     print('unbalanced')

# first_list = list()
# for i in range(len(obj)):
#     if obj[i] in par:
#         first_list.append(obj[i])

# # balanced = False
# opening_parentheses = list()
# for i in first_list:
#     if i == par[1] and not opening_parentheses:
#         balanced = False
#     elif i == par[0]:
#         opening_parentheses.append(i)
#     elif i == par[1]:
#         opening_parentheses.pop()

# if not opening_parentheses:
#     balanced1 = True
# else:
#     balanced1 = False

# if balanced == False and balanced1 == False:
#     print('not balanced')
# else:
#     print('balanced')

