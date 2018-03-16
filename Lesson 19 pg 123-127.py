# Lesson 19 pages 123-127

#Error   'This is Kristy's cat.' 
"This is Kristy's cat."   # solved by Double Quotes
'This is Krisyt\'s cat.'  # solved by Escape Characters

print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw Strings
r'Hello'
print(r'This is Kristy\'s cat.')

# Multiline Strings
print(''' cats cats
      cat cat cattsssts cats''')
print(""" cats cats
      cats cat cat casttsss cats""")
print(len(""" cats cats
      cats cat cat casttsss cats"""))

# Indexing and Slicing Strings
spam = 'Hello World!'
spam[0]
spam[4]
spam[-1]
spam[1:5]
spam[:5]
spam[6:]

# in and not in Operators with Strings
'Hello' in 'Hello World!'
'x' in 'Hello World!'

