import random

def drawBoard(board):
    #functia printeaza tabla pe care urmeaza a se juca

    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def imputPlayerLetter():
    #fuctia lasa jucatorul sa aleaga ce litera vrea sa fie
    #returneaza o lista cu litera jucatorului pe prima pozitie si
    # cu litera computerului pe cea de-a doua pozitie

    letter = ''

    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    #functia alege cine face prima miscare

    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):

    board[move] = letter

def isWinner(b, l):
    #functia este responsabila cu recunoasterea unei combinatii castigatoare

    return ((b[1] == l and b[2] == l and b[3] == l) or #linia de sus
            (b[4] == l and b[5] == l and b[6] == l) or #linia din mijloc
            (b[7] == l and b[8] == l and b[9] == l) or #linia de jos
            (b[1] == l and b[4] == l and b[7] == l) or #coloana din stanga
            (b[2] == l and b[5] == l and b[8] == l) or #coloana din mijloc
            (b[3] == l and b[6] == l and b[9] == l) or #coloana din dreapta
            (b[1] == l and b[5] == l and b[9] == l) or #diagonala principala
            (b[3] == l and b[5] == l and b[7] == l))   #diagonala secundara

def getBoardCopy(board):
    #functia face o copie a "tablei" si o returneaza
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    #returneaza True daca miscarea aleasa este libera pe tabla
    return board[move] == ' '

def getPlayerMove(board):
    #functia lasa jucatorul sa isi introduca miscarea

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def choseRandomMoveFromList(board, moveList):
    #functia returneaza o miscare valida de pe tabla dintr-o lista
    #functia returneaza None daca nu exista nicio miscare valida

    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #functia determina unde muta computer-ul si returneaza miscare

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #algoritmul computer-ului:
    #computer-ul verifica daca poate castiga in urmatoarea miscare
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    #computer-ul verifica daca jucatorul poate castiga in urmatoarea miscare
    # si il blocheaza
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    #computer-ul incearca sa mute in unul dintre colturi, daca e liber
    move = choseRandomMoveFromList(board, [1, 2, 7, 9])
    if move != None:
        return move

    #computer-ul incearca sa mute in centru, daca e liber
    if isSpaceFree(board, 5):
        return 5

    #computerul muta pe una dintre laturi
    return choseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #functia returneaza True daca toate spatiile de pe tabla sunt ocupate,
    # in caz contrar returneaza False

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to X & O!')

while True:
    #se reseteaza tabla

    theBoard = [' '] * 10
    playerLetter, computerLetter = imputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #tura jucatorului

            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('It\'s a tie')
                    break
                else:
                    turn = 'computer'

        else:
            #tura computer-ului
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('It\'s a tie')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break