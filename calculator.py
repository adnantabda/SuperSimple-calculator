def addition (number1,number2):
    return (number1 + number2)

def subtraction (number1,number2):
    return (number1 - number2)

def multiplication (number1,number2):
    return (number1 * number2)

def division (number1,number2):
    return (number1 / number2)

print ("This is Simple Calculator! ")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(number1, "+", number2, "=", addition(number1, number2))

        elif choice == '2':
            print(number1, "-", number2, "=", subtraction(number1, number2))

        elif choice == '3':
            print(number1, "*", number2, "=", multiplication(number1, number2))

        elif choice == '4':
            print(number1, "/", number2, "=", division(number1, number2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

