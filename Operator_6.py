"""
Arithmatic Operator
+, -, *. /, // quetient, % (modular - remainder), power ** 

division always gives float answer.
"""
# a = 5
# b = 7
# print('addition')
# print(a+b)
# print('substration')
# print(b-a)
# print('multiplication')
# print(a*b)
# print('Division')
# print(b/a)
# print('Reminder')
# print(b%a)
# print('Quotient')
# print(b//a)
# print('Power')
# print(a**2)
# print('Assignment')
# c = 12
# print(c)

# # increment or decrement
# sum = sum +2
# print(sum)

# # the above increment can be performed using as follows
# sum+=2
# sum-=2
# sum/=3

# comparing 
#== equal
#>=, <=, !=

# Relationational Operator
# and, or, not

# # Conditional Format
# 1. if : if
# 2. else if : elif
# 3. else : else
# every condition will be terminated by  a colon :

#age = 18
# if age>= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

age = int(input("enter your age: "))

if age<16:
    print("Child")
elif age>=16 and age <59:
    print("Young")
else:
    print("old")


number = int(input("Enter a number :"))
if number%2 == 0:
    print("The given number is Even")
else:
    print("The given number is Odd")