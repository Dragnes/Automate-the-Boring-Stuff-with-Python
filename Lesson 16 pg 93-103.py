#Lesson 16 pages 93-103

list('Hello')
name = 'DHRUG'
name[0]
name[1:4]
name[-2]
'DH' in name    # Case sensitive
'dh' in name
'xxx' not in name
'xxx' in name
for letter in name:
    print(letter)

for i in name:
    print('****'+i+'****')
  
# Mutable and Immutable Data Types
'List value is mutable, Strings are immutable'
name = 'Thor the cat'
name[5]
name[5] = 'X'   # doesn't work

name = 'Thor a cat'
newName =  name[0:5] + 'Da' + name[6:10]

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'


import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42


# Practice Questions
spam = ['a', 'b', 'c', 'd']
spam[int(int('3'*2) // 11)]
spam[-1]
spam[:2]

bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')
bacon.append(99)
bacon.remove('cat')




