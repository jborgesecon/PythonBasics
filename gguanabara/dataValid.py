
error1 = "Please enter a valid number"

def sepper(msg, sep):
    print('\n', msg.center(30, sep))

def header(msg):
    print('\n')
    print(30 * '=')
    print(msg.center(30))
    print(30 * '=', '\n')

def intValid(num):
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            print(error1)
            num = input("Enter a number: ")
    return num

def p_intValid(num):
    while True:
        try:
            num = int(num)
            if num < 0:
                print("Please enter a positive number")
                num = input("Enter a number: ")
            else:
                break
        except ValueError:
            print(error1)
            num = input("Enter a number: ")
    return num

def floatValid(num):
    while True:
        try:
            num = float(num)
            break
        except ValueError:
            print(error1)
            num = input("Enter a number: ")
    return num

def yn_valid(txt):
    while True:
        if txt == 'y' or txt == 'n':
            break
        else:
            txt = input("Type 'y' for YES and 'n' for NO: ")
    return txt