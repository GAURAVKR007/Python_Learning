import utility 

def calc(num1,num2,operator):
    match operator:
        case '+':
            return utility.add(num1,num2)
        case '-':
            return utility.sub(num1,num2)
        case '*':
            return utility.mul(num1,num2)
        case '/':
            if (num2 == 0):
                return "Undefined"
            return utility.div(num1,num2)
        case default:
            return "Invalid Input"

while True: 

    try:
        num1 = int(input("Enter the 1st no => "))
        num2 = int(input("Enter the 2nd no => "))
        operator = input("Enter the Operator (+,-,*,/) => ")
    except ValueError as err :
        print(f"\nSomething Went Wrong, Error => {err}\n")
    else:
        break


result = calc(num1,num2,operator)
print(f'The Result is {result}')

