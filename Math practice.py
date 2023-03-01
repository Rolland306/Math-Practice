# practice simple math questions and get percentage score at the end
# one qsn---done
# optimization: loops for multiple qsns then playing the game multiple times
# to be converted into React calculator
import random


def start_practice():
    print("Enter the type of Math questions you want to practice:")
    choice = menu()  # calling menu function
    if choice == 1:
        addition_module()
    elif choice == 2:
        subtraction_module()
    elif choice == 3:
        multiplication_module()
    else:
        division_module()


def menu():
    print("1 - for addition module")
    print("2 - for subtraction module")
    print("3 - for multiplication module")
    print("4 - for division module")
    user_pick = int(input(
        "Choose one module from the above modules and enter the corresponding number:"))
    return user_pick


def addition_module():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    answer = a + b
    val = int(input("What is "+str(a)+" + "+str(b)+" : "))
    if answer == val:
        print("correct!!!")
    else:
        print("incorrect")


def subtraction_module():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    answer = a - b
    val = int(input("What is "+str(a)+" - "+str(b)+" : "))
    if answer == val:
        print("correct!!!")
    else:
        print("incorrect")


def multiplication_module():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    answer = a * b
    val = int(input("What is "+str(a)+" x "+str(b)+" : "))
    if answer == val:
        print("correct!!!")
    else:
        print("incorrect")


def division_module():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    answer = a / b
    val = int(input("What is "+str(a)+" / "+str(b)+" : "))
    if answer == val:
        print("correct!!!")
    else:
        print("incorrect")


start_practice()
