'''
While condition:
    statement

'''
# # Example of While loop
# i = 0
# while i<5:
#     print(i)
#     i=i+1
# print("Pokhara")

# Example 2 of while loop
# password = input("Enter your password : ")

# while password != "password123":
#     print("Wrong password, Enter right password!")
#     break

# print("Welcome to our system.")

# # Example 3 of while loop
# password = input("Enter your password: ")
# while password == "password123":
#     print("Welcome to our system")
#     break


# # Example 4 of while loop
# password = input("enter your password :")

# while True:
#     if password == "password123":
#         print("Welcome to our system!")
#         break  # if you don't add break here it goes in the infinite loop
#     else:
#         print("Wrong passord")
#         password = input("enter your password :")
#         continue  # its takes you back to while True loop again

# # Example of using "break" and "continue"
# # if i becomes 5 then don't print else it should print
# i = 1
# while i<=10:
#     if i != 5:
#         print(i)
#     i= i+1

i = 1
while i<=10:
    if i == 5:
        i=i
    else:
        print(i)
    i= i+1