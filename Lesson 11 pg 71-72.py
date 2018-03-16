#Lesson 11 pages 71-72

'Handeling Error of dividing by zero'

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by Zero.')
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


print('How many cats do you have?')
numCats = input()
try:
    if int (numCats) >= 4:
        print('Thats a lot of cats')
    else:
        print('Thats is not a lot of cats.')
except ValueError:
    print('You did not ender a number')
