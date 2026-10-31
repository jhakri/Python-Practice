""""
Mini Student Management System
new student add
store their record which is another database
in our project we use list to store data.
we should be able to view them
remove/delete
pass fail  check
we use dictionary within a list so that we can obtain every dictionary's information.
we will induce match ... case..
"""
student_details=[]  # empty list

print("1. Add Student\n 2. View Student\n 3. Passed\n 5. Remove")

choice=int(input("Enter your choice form 1 to 6"))
match choice:
    case 1:
        id = int(input("Enter student Id: "))
        name = input("Enter name: ")
        mark = float(input("Enter mark :"))
        studentadd ={
            "id": id,
            "name": name,
            "mark":mark
        }
        student_details.append(studentadd)
        print("One record is added successfully.")

    case 2:
        pass
    case 3:
        pass
    case 4:
        pass
    case 5:
        pass
    case 6:
        print("Thank you for using the student management.")
