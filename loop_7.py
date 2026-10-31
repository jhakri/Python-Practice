"""
loop:
a specific task or procedure must be performed repeatedly unless and untill the condition is true 
There are loops
For loop  : generally it is already understood how many times the repeatition must be carried out
While loop : used when condition clear to be okay to end.
"""
# number = [1,2,3,4,5,6]  # list any enumeration is specified or set is specified in a pair of square bracket is known list

# course = "Python"
# # first example of for loop
# for ch in course:
#     print(ch)
#  # this is an example of using the for loop 
#  #
# # second example of for loop
# for i in range(8):  # range(8) means its starts from 0 to 8-1, means, 0 to 7
#     print(i)

# # third example of for loop
# for i in range(8,10): # this means also starting from 8 to 10-1, means 8, and 9
#     print(i)

# Forth example of for loop
for i in range(1,10,2): # it starts fro 1 until 9 with interval of 2
    print(i)
# Fifth example of for loop
for i in range(10,1,-1):  #it starts from 10 until 1+1, in reverse step.  It means it prints from 10 to 2 in reverse order.
    print(i)

# Sixth example of for loop
for i in range (10,0,-1):
    print(i)


## nested conditional loop
number = 9
if number >0:
    if number%2 == 0:
        print("It is even.")
    else:
        print("it is odd.")
else:
    print("number must be greater than 0.")

## in same way we can use for nested loop too
