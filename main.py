#List items are enclosed in brackets (thats how you identify them)
#Lists are ordered in sequence
#Lists are mutable
#List elements do not need to be unique (it acceots dupe's so you have to be careful when writing out code
#List can be of different data typees i.e. numbers, names

#List =[]
#List =[1,2,3]
#List =['orange', 'apple', 'pear', 'banana']
#List =[1, 'Hello',5.0]
#print(List)
#example of list above

'''
List Indexing
'''
#fruits =['orange', 'apple', 'pear', 'banana']
#print(fruits[-0])
#Try reference an index that is out of range and see what you get

#fruit =['orange', 'blueberry', ['apple', 'pear', 'banana']]
#print(fruit[2][1])
#A list within a list


'''
How to slice Lists in Python
'''
#slicing is going through a list and slicing things/obtining info out of the list

#fruit =['orange', 'blueberry', 'apple', 'pear', 'banana']
#print(fruit[:])
#This is also a way using a copy:
#print(fruit[2:5])
#This is getting index 2(pear) to index 5 (banana) hence slicing
#print(fruit[-2:5])
#Go from the back (pear) and remove the last 3
#print(fruit[:3])
#No index up above, we are using positon only
#print(fruit[2:])
#read backwards from the index starting at 0

#print(fruit[::2])
#Gives us every other value

#print(fruit[::-1])
#Reading it in reverse (reversing a list)

'''
Add Elements to a List
'''
#fruit =['orange', 'blueberry', 'apple', 'pear', 'banana']

#fruit [0] = 'Berries'
#print(fruit)
#That changes, makes it mutable
#fruit[1:4] = ['Mandarins', 'Peaches', 'Plums']

#Using slicing to mutate the elements
#fruit.append('Lines")')
#print(fruit)




'''
Remove or Delete List Items
'''


#fruit =['orange', 'blueberry', 'apple', 'pear', 'banana']

#del fruit[0]
#Deletes the first index fruit which is orange

#del fruit[1:5]
#print(fruit)

#Using slicing to pull data out and deleting other information (only orange is left)

#del fruit
#print(fruit)
#That wont work because you need to point to an index

'''
Python List Methods
'''
#This allows you to list all the sttributes
#print(help(dir))

#print(dir(list))
#print(help(list.count))
#print(dir(list.index))

#print(dir(set))

#fruit =['orange', 'blueberry', 'apple', 'pear', 'banana']
#fruit.append('cashew')


#fruit.insert(3, 'guava')
#print(fruit)
#Its not replacing, its inserting before index (insert a zero)

#fruit.clear()
#print(fruit)
#Just literally clears everything

#fruit.pop(1)
#print(fruit)

#print(fruit.index('pear'))
#print(fruit)
#Tells you where the named fruit is in the index

#pos = fruit.index('banana')
#fruit.pop(pos)
#print(fruit)

#fruit =['orange', 'blueberry', 'apple', 'pear', 'banana']

#print(fruit.count('pear'))
#How to count objects within a list
#add fruits to the code

#fruit =['orange', 'blueberry', 'apple', 'pear', 'banana', 'banana']
#print(fruit.count('banana'))
#result = {}
#for x in fruit:
#   result[x] = fruit.count(x)

#print(result)
   #This gives a value of each item plus name data structure dictionary

#from collections import Counter

#print(Counter(fruit))

#An easier way of doing that, faster, same as the example above it but just quicker

'''
List Membership Test
'''

#fruit =['orange', 'blueberry', 'apple', 'pear', 'banana', 'banana']
#print("orange" in fruit)
#Asking if a certain item is in the list

#print("orange" not in fruit)
#Not in the list