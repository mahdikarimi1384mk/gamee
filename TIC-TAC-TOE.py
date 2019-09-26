import random


def drawBoard(board):
    print(board[7] + ' | '    + board[8] +     ' | '   + board[9])
    print('--+--+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+--+--')
    print(board[1] + ' | ' + board[2] +  ' | ' + board[3])


def inputPlayerLetter():
    letter = ''
    while (letter != 'X' or letter != 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']   

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Across the top
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    # Across the middle
   (bo[4] == le and bo[5] == le and bo[6] == le) or 
    # Across the bottom
   (bo[1] == le and bo[2] == le and bo[3] == le) or
    # Down the left side
   (bo[7] == le and bo[4] == le and bo[1] == le) or 
    # Down the middle  
   (bo[8] == le and bo[5] == le and bo[2] == le) or 
    # Down the right side
   (bo[9] == le and bo[6] == le and bo[3] == le) or 
    # Diagonal
   (bo[7] == le and bo[5] == le and bo[3] == le) or 
    # Diagonal
   (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board): 
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == '  '


def getPlayerMove(board):
    move = '  '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []  
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
       

 # Given a board and the computer's letter, determine where to move
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # First, check if we can win in the next move.

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            # print('getcomputermove check win: ', i)
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                 return i
    # Check if the player could win on their next move and block them.          
    for i in range (1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            # print('getcomputermove block: ', i)
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
 
# Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
# Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
# Move on one of the sides.
    move = chooseRandomMoveFromList(board, [2, 4, 6, 8])
    # print('getcomputermove[2,4,6,8]: ', move)
    return move


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def drawBoardBelow(board):
    bc = getBoardCopy(board)
    drawBoard(board)
    for i in range(1,10):
        if isSpaceFree(board, i):
            bc[i] = str(i)
        else:
            bc[i] = '  '
    drawBoard(bc)


def drawBoardBeside(board, bc):
    print(board[7] + ' | '    + board[8] +     ' | '   + board[9] + '                         '+ bc[7] + ' | ' + bc[8] +     ' | ' + bc[9]) 
    print('--+--+--'+ '                         '+'--+--+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6] + '                         '+ bc[4] + ' | ' + bc[5] +     ' | ' + bc[6])
    print('--+--+--'+ '                         '+'--+--+--')
    print(board[1] + ' | ' + board[2] +  ' | ' + board[3] + '                        '+ bc[1] + ' | ' + bc[2] +     ' | ' + bc[3])

def makeBoard(board):
    bc = getBoardCopy(board)
    for i in range(1,10):
        if isSpaceFree(board, i):
            bc[i] = str(i)
        else:
            bc[i] = '  '
    return(bc)


def newGetPlayerMove(board):
    print('plz input your move number: ')
    while True:
        move = input()
        if move not in  '1 2 3 4 5 6 7 8 9'.split():
            print('plz choose your move number between 1...9: ')
        else:
            if isSpaceFree(board, int(move)):
                return int(move)
            else:
                print('This location is occupied. Please select another one according to board: ')

"""
brd = ['  ', 'X', 'O', '  ', '  ', 'X', '  ', '  ', '  ', '  ']
drawBoardBelow(brd)
mv = newGetPlayerMove(brd)
print(mv)
"""
#--------------------------------------------------------------------------------------
print('WELCOME TO TIC-TAC-TOE!')

while True:
#reset the board
    theBoard = ['  '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            bc = makeBoard(theBoard)
            drawBoardBeside(theBoard, bc)
            move = newGetPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                bc = makeBoard(theBoard)
                drawBoardBeside(theBoard, bc)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    bc = makeBoard(theBoard)
                    drawBoardBeside(theBoard, bc)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else: # turn == 'computer'
            move = getComputerMove(theBoard, computerLetter)
            # print('main, turn=compter : ', move)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                bc = makeBoard(theBoard)
                drawBoardBeside(theBoard, bc)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    bc = makeBoard(theBoard)
                    drawBoardBeside(theBoard, bc)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break

