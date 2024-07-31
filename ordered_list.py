import random as rd


list1 = list()
len1 = int(input("Enter the length of the list: "))

while len(list1) < len1:
    num = rd.randint(1, len1)
    if not list1:
        list1.append(num)
        print(list1)
    elif num in list1:
        print("Already in the list, will not be added!")
    elif num > list1[-1]:
        list1.append(num)
        print(list1)
    else:
        for i in range(len(list1)):
            if num in list1:
                break
            elif num < list1[i]:
                list1.insert(i, num)
                print(list1)
                break

print("\nThe End!\n")