"""
tuple =()
it can be immutable

"""
# #Example 1
# name =("ram", "syam", "hari")
# print(name)
# print(type(name))

# # Example 2
# name.append("radha") # you cannot add like in list beccause it is is immutable
# name.remove("syam") # you cannot remove too.

# new_name =list(name)  # converting name tuple to a list called new_name
# print(new_name)
# print(type(new_name))

# new_name.append("radha")
# print(new_name)

# name = tuple(new_name) # you can convert list into tuple.
# print(name)

# Set: like a tuple bt it can be unorder, cannot store duplicate values {}
#name={"ram", "shyam", "hari","sita"}
#print(name{3})  # not applicable.
#print(name.index("shyam")) # not applicable
# #print(name)  # every print it does not give in the same order so it is known as unordered.
# #Example
# name={"ram", "shyam", "hari","sita", "ram"}
# print(name)  # does not give duplicat ram, instead it shows only once. 

# print(type(name))
# name.add("akash")
# print(name)
# name.remove("shyam")  # you can remove but not permitted to append.
# print(name)
# name.update({"radha", "bishes"})
# print(name)
# name.discard("hari")  # like remove.
# print(name)
# name.pop()  # it helps to remove from the last but it does make sure which one because of unordered.
# name.clear()

"""
Although we can define as
list =()
tuple =[]
but 
we cannot say name={} because it indicates to a dictionary
so we have to name =set(), explicitly
"""

# Additional function
# union, intersection,
# Example 1
# var1 = {1,2,3,4,5,6,9,35,565}
# var2 ={8,9,10,54,55}

# Example union 
# print('Union')
# var3 = var1.union(var2)
# print(var3)

# # this is also another way of union but not used often
# print('Union')
# var3 = var1|var2
# print(var3)

# # Example of Intersection   it can be performed using & too.
# print('Intersection')
# var4 = var1.intersection(var2)
# print(var4)

# #Example of Difference
# print('Difference')
# var5 = var1.difference(var2)
# print(var5)

# # Example with many sets
# print("with many sets using union")
# var6={5,6,7,8,10,105,501}
# var7 = var1.union(var2).union(var6)
# print(var7)


# Membership operator
print("membership operator")
a = "Python"
print("g" not in a)
print("g" in a)

print("Identity Operator")
a = 4
b = 8
c = 4
print (a is b)
print (a is c)