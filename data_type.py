# working with strings
print("my name is sampson")
# defining your variables
law= ('happy birthday to you all')
print(len(law))
 # moditying strings
b = 'We Are Learning Python Data Types For The Our Session'
print(b.lower())

# string concatenation
a= 'Beautiful'
b = 'Day'
c= a + " " + b
print(c)

# list data type
students = ['Micah', 'Sharon', 'Nasir', 'Mac','Samuel', 'Rahab', 'Brian', 'Jackline']
print(students)

#access list items
students = ['Micah', 'Sharon', 'Nasir', 'Mac','Samuel', 'Rahab', 'Brian', 'Jackline']
print(students [3])

# ranges of list
students = ['Micah', 'Sharon', 'Nasir', 'Mac','Samuel', 'Rahab', 'Brian', 'Jackline']
print(students [4:])

#change list items
students = ['Micah', 'Sharon', 'Nasir', 'Mac','Samuel', 'Rahab', 'Brian', 'Jackline']
students[1] = 'Gustave'
print(students)

# insert items
students = ['Micah', 'Sharon', 'Nasir', 'Mac','Samuel', 'Rahab', 'Brian', 'Jackline']
students.insert (2, 'Caleb')
print(students)

# add to list
students = ['Micah', 'Sharon', 'Nasir', 'Mac','Samuel', 'Rahab', 'Brian', 'Jackline']
students.append('Faith')
print(students)
# remove items
students = ['Micah', 'Sharon', 'Nasir', 'Mac','Samuel', 'Rahab', 'Brian', 'Jackline']
students.remove('Jackline')
print(students)