# Lesson 12  pages 74-76

# This is a guess the number game.
import random

print('Hello, what is your name?')
name = input()
print('Well ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)
#print('I am thinking of a number between 1 and 20.')

#  Ask the player to guess 6 times.

for guessesTaken in range(1, 7):
    print('Take a guess. ')
    guess = int(input())
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break   #This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking was ' + str(secretNumber))
    
    
    
# The Collatz Sequence   
    
def collatz_sequence(num):
    if num % 2 == 0:
        print(num // 2)
        return (num // 2)
    else:
        num % 2 == 1
        print(3 * num + 1)
        return(3 * num + 1)
            
n = input('Give me a number: ')
while n != 1:
    n = collatz_sequence(int(n))
    

def collatz(n):
    seq = [n]
    while n > 1:
        if n%2 == 1:
            n = n*3 + 1
            seq.append(n)
        else:
            n = n/2
            seq.append(n)
    return seq
                   
print (collatz(7))
