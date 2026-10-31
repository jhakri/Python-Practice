""""
Data Structure
We have common four types data structure

1. List:
2. Tuple:
3. Set:
4. Dictionary:

the data structure is required to store data in an organized way.  so that we can fetch or work out in effecient way
"""
# List: Ordered, changeable, duplicable, 
# syntax  name=[, ,]
# Exaple 1
print("Example 1")
number = [1,2,3,4,5,6,7,8]
print(number)

# Example 2
print("Example 2")
number = [1,2,3,4,5,6,7,8]
print(number[2])  # its start with index 0 and 2 means 3 will be printed.

# Example 3
print("Example 3")
number = [1,2,3,4,5,6,7,8,]
for i in number:
    print(i)


#Example 4
print("Example 4")
name =["Akash","Bikash", "12", 5,"Hari"]
for i in name:
    print(i)
print(type(name))

#Example 5
print("Example 5")
name =["Ram", "Syam", "Mohan", 'Krishna']
name.append("Sagar")  # appending one element in the last
name.insert(1,"Laxman") #inserting Laxman in the second sequence
name.remove("Sagar") # remove Sagar from the list
name.pop()  # pop helps to remove the last element of the list
for n in name:
    print(n)
del name[0] # delete the first item of the list.
print(name.index("Syam")) # shows the index location that indicates to Syam
name.extend(["Pkr","Bgl","Ktm"])  # add another list into a list
for n in name:
    print(n)

print(name.sort())  # Asecending order
print(name.sort(reverse=True)) # Descending order
name.clear() # clear the list.
print(name)