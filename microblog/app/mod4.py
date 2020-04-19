# def l100kmtompg(liters):
#     lTog = liters / 3.785411784
#     kmTom= (100 * 1000) / 1609.344
#     ans = kmTom / lTog
#     return ans

# def mpgtol100km(miles):
#     gToL = 1 * 3.785411784 
#     mTokm = (miles * 1609.344) / (100 / 1000)
#     ans = gToL/ mTokm
#     return ans

# print(l100kmtompg(3.9))
# print(l100kmtompg(7.5))
# print(l100kmtompg(10.))
# print(mpgtol100km(60.3))
# print(mpgtol100km(31.4))
# print(mpgtol100km(23.5))
# schoolClass = {}

# while True:
#     name = input("Enter the student's name (or type exit to stop): ")
#     if name == 'exit':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
    
#     if name in schoolClass:
#         schoolClass[name] += (score,)
#     else:
#         schoolClass[name] = (score,)
        
# for name in sorted(schoolClass.keys()):
#     sum = 0
#     counter = 0
#     for score in schoolClass[name]:
#         sum += score
#         counter += 1
#     print(name, ":", sum / counter)

# tups = ("one",)
# print(type(tups))
from random import randint
boards = 0
freeBox= [
        (1,2,3),
        (4,5,6),
        (7,8,9)
    ]
def DisplayBoard(board):
    # if board == 0:
    displayRecur()
    # else:
    #     print("idk")
# the function accepts one parameter containing the board's current status
# and prints it out to the console

def displayRecur():
    # for row in range(7):
    #     if row % 2 == 0:
    #         for n in range(3):
    #             print('+', end="")
    #             print('------', end="")
    #             if n == 2:
    #                 print('+', end="\n")
    #     else:
    for numRow in range(3):
        for col in range(3):
            print("|",freeBox[numRow][col], sep="     ", end="")
        print('|', end="\n")

def EnterMove(board):
    move = int(input("U:"))
    # move checker
    if move < 10 and move > 0:
        print("box",move) 
    else:
        print("False")
# #
# # the function accepts the board current status, asks the user about their move, 
# # checks the input and updates the board according to the user's decision
# #

def MakeListOfFreeFields(board):
    # for n in range(listBox):
    # 
    newList = list(freeBox)
    print(newList)
# #
# # the function browses the board and builds a list of all the free squares; 
# # the list consists of tuples, while each tuple is a pair of row and column numbers
# #

def VictoryFor(board, sign):
    return False
# #
# # the function analyzes the board status in order to check if 
# # the player using 'O's or 'X's has won the game
# #

def DrawMove(board):
    if board == 0:
        print("x middle")
    else:
        print("C:",randint(1,7))
# #
# # the function draws the computer's move and updates the board
# #
var =1
print(0+2 *3+3*1)
while not VictoryFor(boards,1): #and board still free:
    print("Board num:",boards)
    DrawMove(boards)
    boards += 1

    DisplayBoard(boards)
    if boards % 3 == 0:
        print("User turn:")
        EnterMove(boards)
    else:
        print("Computer turn:")
        DrawMove(boards)
    MakeListOfFreeFields(boards)

de