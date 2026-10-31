""""
Calculator using python
8 September 2026

"""
while True:
    print("1. Addition")
    print("2. Substration")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Percent")
    print("7. Remainder")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    if choice < 1 or choice > 8:
        print("Invalid choice, please choose number from 1 to 8 ")
        continue        # it prevents to go all way if choice is wrong and takes back to start again. 

    if choice == 1:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
        continue
    elif choice == 2:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1 - num2
        print(f"The substration from {num1} to {num2} is {result}")
        continue
    elif choice == 3:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1 * num2
        print(f"The multiplication of {num1} and {num2} is {result}")
        continue
    elif choice == 4:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1 / num2
        print(f"The division of {num1} by {num2} is {result}")
        continue
    
    elif choice == 5:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1 ** num2
        print(f"The power of {num1} by {num2} is {result}")
        continue

    elif choice == 6:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = (num1/ num2)*100  # percent
        print(f"The percent is {result} of {num1} by  {num2} ")
        continue

    elif choice == 7:
        num1 = float(input("Enter a first number :"))
        num2 = float(input("enter a second number: "))
        result = num1% num2  # modulus
        print(f"The remainder by dividing {num1} by  {num2} is {result}")
        continue

    else:
        break 
        # print("My name is Akash")