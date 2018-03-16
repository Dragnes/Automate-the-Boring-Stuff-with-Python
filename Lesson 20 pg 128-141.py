# Lesson 20 pg 128-141

# upper(), lower() Methods
spam = 'Hello World'
spam.upper()
spam.lower()

print('How are you?')
feeling = input()
if feeling.lower() == 'great' or 'good':
    print('I am feeling the same too!.')
else:
    print('I hope the rest of your day goes well!')
    
# isupper(), islower() Methods

spam = 'Hello World!'
spam.islower()
spam.isupper()
'HELLO'.isupper()
'abc12345'.islower()
'12345'.islower()
'12345'.islower()

'Hello'.upper()
'Hello'.upper().lower()
'Hello'.upper().lower().upper()
'HELLO'.lower()
'HELLO'.lower().islower()


# the is(XYZ) String Methods

'hello'.isalpha()
'hello12345'.isalpha()
'hello123'.isalnum()
'hello'.isalnum()
'1234'.isdecimal()
'     '.isspace()
'This Is Title Case'.istitle()
'This Is not Title case'.istitle()
'This Is Title Case 1234'.istitle()

#The startswith() and endswith() String Methods
'Hello world!'.startswith('Hello')
'Hello world!'.endswith('world!')
'abc1234'.startswith('bc')
'abc1234'.startswith('1234')
'Hello world!'.startswith('Hello world!')
'Hello world!'.endswith('Hello world!')

# The join()
','.join(['cats', 'rats', 'bats'])
' '.join(['My', 'name', 'is', 'Dhrug'])
':'.join(['My', 'name', 'is', 'Dhrug'])
'\n\n'.join(['My', 'name', 'is', 'Dhrug'])
print('\n\n'.join(['My', 'name', 'is', 'Dhrug']))

# The slpit()
'My name is Dhrug'.split()
'My name is Dhrug'.split('m')

# The rjust(), ljust() String Methods   
'Hello'.rjust(10)
'Hello'.ljust(10)

'Hello'.rjust(20, '*')
'Hello'.ljust(20, '*')

# The center() String Method
'Hello'.center(10)
'Hello'.center(10, '=')
'Hello'.center(15, '=')

# Removeing Whitespace with strip(), rstrip(), and lstrip() String Method
spam = 'Hello'.rjust(10)
spam.strip()
'   x   '.strip()
'   x   '.rstrip()
'   x   '.lstrip()

'SpamSpamBaconSpamEggsSpamSpam'.strip('Spam')
'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')

# The replace() String Method
spam = 'Hello There!'
spam.replace('e', 'XYZ')

