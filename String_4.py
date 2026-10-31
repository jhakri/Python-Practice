# print(bool(-8))  # if it is no equal to zero then it is true
# print(bool(0))   # if it is equal to zero then it is false

name = "Akash Kumar Das"
#print(name)

# slicing string
# The given string Akash Kumar Das is counted as 0 from its initial place it counts the white space as well from left to right.

print(name[0]) # it must display the first character of the string
print(name[4]) # it displays h the number what is specified in pair of square is called index value
print(name[0:5])
# while slicing we have to remember the format as
# name[star:End]

# name[star: End, step]  by default step holds positive 1, last index can be len-1
# there is no array in Python
print(name[0:5:2])
print(name[6:11])
print(name[-3::]) # it starts from right to left 3rd character and rest all.
print(name[0:-3]) # it starts from the beginning until the end position 3rd character 
print(name[-6:-2]) 
print(name[-2:-6])