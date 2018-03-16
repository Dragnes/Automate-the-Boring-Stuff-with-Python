#Lesson 15 pages 89-92

'Method is similar to function, except it is "called on" a value.'

# Finding a Value in a List with the index() Method
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
spam.index('heyas')

# Adding Values to a List using append() and insert() Methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam.insert(2, 'chicken')

# Remove Values from Lists with remove() Method
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')

# Sorting the Values in a List with the sort() Method
# Increasing order
spam = [2, 5, 3.14, 1, -7]
spam.sort()

spam = ['ants', 'dogs', 'baggers', 'elephants', 'cats']
spam.sort()
# Decreasing order
spam = [2, 5, 3.14, 1, -7]
spam.sort(reverse = True)

spam = ['ants', 'dogs', 'baggers', 'elephants', 'cats']
spam.sort(reverse = True)

# Integers and Strinigs can't be sorted, due to silliness python
spam = [1, 2, 3, 4, 'Alice', 'in', 'land']
spam.sort()

# Caps vs non-Caps
spam = ['Alice', 'ants', 'AAbob', 'Bob', 'baggers','Carol', 'AABob', 'cats']
spam.sort()

spam = ['A', 'Z', 'a', 'z']
spam.sort(key = str.lower)
