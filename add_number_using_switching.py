numberOne = int(input("enter you number"))
numberTwo = int(input("enter your number"))
choice_number =input("enter your choice 1 for addition 2 for subtraction 3 for multipuliction")
match choice_number:
    case "1" :
        print = numberOne+numberTwo
    case "2" :
        print = numberOne-numberTwo
    case "3" :
        print = numberOne*numberTwo
    case _:
        print("invalid operation")
