## working with strings

print('my name is sampson')

#sting length
law = ("happy birthday my love")
print(len (law))

# check string in/not (true or false)
law = ("many people are in class today learning python programming language")
print('azubi' in law)

#b = "beautiful day"
#print(b [2:3])

# modify strings
b = "Beautiful day"
print(b.upper())

# string concatenation
a = 'beautiful'
b = 'day'
c = a + " " + b 
print(c)

# List
myfruit = ['banana', 'apple', 'mango', 'cherry']
print(myfruit)

# Access list items
myfruit= ['apple', 'orange', 'banana', 'cherry']
print(myfruit[0])

#Range of indexes
fruit = ['apple', "banana", 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(fruit[2:5])

#change list items
fruit = ['mango', 'banana', 'cherry']
fruit[1] = 'organe'
print(fruit)

# insert items
fruit = ['apple', 'banana', 'cherry']
fruit.insert (2, 'watermelon')
print(fruit)

#add list items
fruit = ['apple', 'banana', 'cherry']
fruit.append('orange')
print(fruit)

# extend list
fruit1 = ['apple', 'banana', 'cherry']
fruit2 = ['mango', 'pineaple', 'papaya']
fruit1.extend(fruit2)
print(fruit1)