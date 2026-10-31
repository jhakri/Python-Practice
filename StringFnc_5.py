"""
1. upper()
2. lower()
3. split()
4. replace()
5. capitalize()
"""
# # Exercise
# text = "Akash Kumar Das"
# print(text.upper())
# print(text.lower())
# print(text.replace("Das", "Udas"))
# print(text.capitalize())
# print(text.split()) # converstion into a list with every term by splitting them.
# print("Ram Krishna Nepali". split())
# print(text.count("a"))
# print("     Akash".strip())  # remove pre starting space or following spaces.
# print("akash      ".strip())
# print("   akash".upper().strip())
# print(text.islower())
# y = 5
# print(y.isdigit())  # not working


# # input function
# name = input("Enter your name :")   # input always accept as a string unless you mentioned the typecast
# print(name)
# print("hello", name)

# number=input("enter a number: ")
# print(number)
# print(type(number))

# number = int(input("enter a number:"))
# print(number)
# print(type(number))

# number =float(input("Enter a float number: "))
# print(number)
# print(type(number))

# #concatenate two string, +, f-string

# a = 3
# b = 4
# print(a+b)

# a = "3"
# b = "4"
# print(a+b)

# a="Ram"
# b = "Nepal"
# print(a+b)
# print(a+""+b)
# print(a, b)
# print(a, " ", b)


first_name =input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(first_name, last_name)

# using format string "f"

print(f"My first name is", first_name)
print(f"My last name is", last_name.upper())

#print(f"My firstname is {first_name} and last name is {last_name}.upper()") #this line does not work
#print(f"My firstname is {first_name} and last name is upper({last_name})") #this line does not work.
print(f"My firstname is {first_name} and last name is {last_name}")

#Escape character or Escape Sequence it always starts with backslash (\)
"""
\t tab
\n line break
\\ add slash
\a bell

"""