def calculator():
    print("Welcome to the simple Calculator!!")
    num1 = float(input("Enter the First Number: "))
    num2 = float(input("Enter the Second Number: "))
    print("Choose the Operation:")
    print("1. ADDITION (+)")
    print("2. SUBTRACTION (-)")
    print("3. MULTIPLICATION (*)")
    print("4. DIVISION (/)")
    operation = input("Enter the number corresponding to the operation: ")
    if operation == '1':
        result = num1 + num2
        print(f"The Result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The Result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The Result of {num1} * {num2} is: {result}")
    elif operation == '4':
        if num2 != 0:
           result = num1 / num2
           print(f"The Result of {num1} / {num2} is: {result}")
        else:
            print("ERROR!!! Division by 0 is not allowed...")
    else:
        print("Invalid operation choice! Please try again...")
calculator()
