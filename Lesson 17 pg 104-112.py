# Lesson 17 pg 104-112

# Dictionary Data Type
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']

'My cat has ' + myCat['color'] + ' fur.'

spam = {12345: 'Combination', 42: 'Answer'}

# Dictionaries vs. Lists
[1, 2, 3] == [3, 2, 1]    # Lists: order MATTERS
                          # Dictionary: order DOESN'T MATTER
cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
othercat = {'disposition': 'loud', 'color': 'gray', 'size': 'fat'}
cat == othercat           # Return True

# keys(), values(), items(): Mthods 
spam = {'color': 'red', 'age': 42, 'style': 'Pimp'}
for key in spam.keys():
    print(key)

for value in spam.values():
    print(value)

for item in spam.items():
    print(item)          #Result is in Tuple Format
    
for k, v in spam.items():
    print(k, v)    

# The get() Method
spam = {'color': 'red', 'age': 42, 'style': 'Pimp'}
spam.get('age', 0)
spam.get('color', '')

picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'    
    
# The setdefault() Method
# if key doesn't exist, we can set it as follows:
spam = {'name': 'Dhrug', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
    
spam = {'name': 'Dhrug', 'age': 5}
spam.setdefault('color', 'black')  
    
# Character count
message = 'It was a bright cold day in April, and the clock were striking thirteen.' 
count = {}
for character in message.upper():   #or .lower()
    count.setdefault(character, 0)
    count[character] += 1
print(count)    
# if we want to print this out neater, use pprint function
import pprint
message = 'It was a bright cold day in April, and the clock were striking thirteen.' 
count = {}
for character in message:   
    count.setdefault(character, 0)
    count[character] += 1
pprint.pprint(count)  



    
    
    
    
    