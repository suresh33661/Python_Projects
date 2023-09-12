# Tic toe game 
# It is played between two players
# either two humans or human and computer


import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
player = "x"
winner = None
gamerun = True

def printboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def playerin(board):
    p = int(input("Enter a number 1 - 9: "))
    if 1 <= p <= 9 and board[p - 1] == "_":
        board[p - 1] = player
    else:
        print("Invalid input or position already taken. Try again.")

def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
    return False

def checktie(board):
    global gamerun
    if "_" not in board:
        printboard(board)
        print("It's a tie!")
        gamerun = False

def switchplayer():
    global player
    if player == "x":
        player = "o"
    else:
        player = "x"

def checkwin():
    if checkdiagonal(board) or checkhori(board) or checkrow(board):
        printboard(board)
        print(f"The winner is {winner}!")
        global gamerun
        gamerun = False

def computer(board):
    while player == "o":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "o"
            switchplayer()

while gamerun:
    printboard(board)
    playerin(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)
