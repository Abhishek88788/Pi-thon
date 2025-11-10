marks = [45.4,545.3,234.3,433]
print(marks)
print(type(marks))


#indexing 
#same like array : we will access the elements of lists using index value

# print(marks[3])
# print(len(marks))

# a = marks
# print(a)


#1. differece bitween  C ,C++ array and python's list( advance array)

#list can store diferent types of data (int,str,float,bool,None)
list = ["abhi",18,47.5,True,None]



#2. difference bitween string and list
 
#string is imutable (not change after initialize)
#lists are mutable (can be change )

#list slicing

name = "Abhishek"

print(name[-1:-9:-1])

#list methods

fruits = ["apple", "banana", "cherry"]
num = [5, 2, 9, 1, 5, 6]

fruits.append("orange")  # Adding an element to the end of the list
print(fruits)
fruits.remove("banana")  # Removing an element from the list
print(fruits)
fruits.sort()  # Sorting the list
print(fruits)

# insert method

insert_list = [45,23,67,12]
insert_list.insert(2, 99)  # Insert 99 at index 2 (intex starts from 0)
print(insert_list)

# if we inser at index greater than length of list then it will insert at the end of list
insert_list.insert(13, 100)  # Insert 100 at index 10 (which is greater than length of list)
print(insert_list)

#answer is [45, 23, 99, 67, 12, 100]
#why- because when we try to insert at an index greater than the current length of the list,
# Python automatically appends the element to the end of the list.
# This behavior ensures that the list remains contiguous and avoids creating gaps or undefined elements.
# Thus, the element 100 is added at the end of the list.








# # pop method
# popped_element = insert_list.pop(3)  # Remove and return element at index 3
# print("Popped element:", popped_element)
# print("List after pop:", insert_lisat)

