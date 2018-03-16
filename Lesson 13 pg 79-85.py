# Lesson 13 pages 79- 85

# chapter 2    Lists

['cat', 'bat', 'rat', 'elephant']
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1]   # access an item in the list

spam = [['cat', 'bat', 'rat' 'elephant'], [10, 20, 30, 40]]
spam[0]
spam[0][1]
spam[1][2]

'Slicing'
spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2]
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:2] #up to 2 but not including 2
spam[1:]


'Changing Values in a List with Indexes', 'Deleting'
spam = 'ant'
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'ant'   #replacing an index
del spam[1]
spam

len('Hello')
len([1, 2, 3])
list('hello')

'howdy' in ['hello', 'hi', 'howdy', 'yo'] #returns true of false
'howdy' not in ['hello', 'hi', 'howdy', 'yo']
