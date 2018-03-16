# Lesson 14 pages 86-88

for i in range(4):
    print (i)

range(4)
[0,1,2,3]
for i in [0,1,2,3]:
    print(i)

list(range(4))
list(range(0, 100, 2))  # range(start, stop, jumpby)

supplies = ['pens', 'pencils', 'paper', 'toothpaste']
for i in range(len(supplies)):
    print('Index' + str(i) + ' in supplies is: ' + supplies[i])

# Multiple Assignment Trick
cat = ['fat', 'black', 'loud']
size = cat[0]
colour = cat[1]
disposition = cat[2]

size, color, disposition = cat
size, color, disposition = 'skinny', 'black', 'quite'

# Augmented Assignment Operators
spam = 41
spam = spam + 1
'or'
spam = 41
spam += 1
