# Lesson 18 pg 112-117

# Data Structures
cat = {'name': 'Thor', 'age': 7, 'color': 'gray'}
allCats = []
allCats.append({'name': 'Mhandi', 'age': 6, 'color': 'white'})
allCats.append({'name': 'Thor', 'age': 5, 'color': 'gray'})
allCats.append({'name': '???', 'age': 4, 'color': 'gray'})
allCats

# Tic-Tac-Toe

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
import pprint
pprint.pprint(theBoard)
#theBoard['mid-M'] = 'X'
#theBoard['top-L'] = 'O'
#theBoard['top-R'] = 'X'
#theBoard['low-L'] = 'O'
#pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for '+ turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

