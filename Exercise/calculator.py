""""
Calculator using python
8 September 2026

"""
while True:
    print("1. Addition")
    print("2. Substration")
    print("3. Multiplication")
    print("4. Division")
    print("5. To exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")

    elif choice == 2:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1 - num2
        print(f"The substration from {num1} to {num2} is {result}")

    elif choice == 3:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1 * num2
        print(f"The multiplication of {num1} and {num2} is {result}")

    elif choice == 4:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1 / num2
        print(f"The division of {num1} by {num2} is {result}")
    elif choice == 5:
        break    
    else:
        print("Please enter the valid choice1")
        # continue
        