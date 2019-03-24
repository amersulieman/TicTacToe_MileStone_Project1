layOutOftheGame = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
boardinAction = [' ']*9
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
player1Symbol = None
player2Symbol = None

def displayRules():
    print("\t\tWelcome to Tic Tac Toe Game\t\t")
    print("The rules are simple...")
    print("~~First player will choose what symbole he/she wants: X or O")
    print("~~The Board Layout will be shown to you with numbers")
    print("At each turn:")
    print("\t1. Pick a grid number to place your symbol")
    print("\t2. keep playing until your symbol had made a straight line across the grids")
    print("\t3. Have Fun\n\n")

def displayBoard(board):
    print("This is your Grid Layout ")
    print("\t{} | {} | {}".format(board[0],board[1],board[2]))
    print("\t" +"-"*9)
    print("\t{} | {} | {}".format(board[3],board[4],board[5]))
    print("\t" +"-"*9)
    print("\t{} | {} | {}".format(board[6],board[7],board[8]))

def getUserSymbol():
    global player1Symbol
    global player2Symbol
    player1Symbol = input("Player 1: would you like to be X or O ? ").capitalize()
    if player1Symbol.lower()== "x" :
        player2Symbol = "O"
    else:
        player2Symbol ="X"

<<<<<<< Updated upstream
def takeTurn(gameboard):
    player1Gridchoice = input("Player 1: which grid would you choose: ")
    #player1gridchoice -1 because our array starts at 0
    gameboard[int(player1Gridchoice)-1]=player1Symbol
    
    player2Gridchoice = input("Player 2: which grid would you choose: ")
    #player2gridchoice -1 because our array starts at 0
    gameboard[int(player2Gridchoice)-1]=player2Symbol
=======
def userGridChoice(theboard=boardinAction, theplayer = "Player1",theplayerSymbol="X"):
    displayBoard(theboard)
    userchoice = input(theplayer+" which grid you choose? ")
    theboard[int(userchoice)-1] = theplayerSymbol

def winChecks(gameboard,playerNumber,theplayerSymbol):
    if gameboard[0]==theplayerSymbol and  gameboard[1]== theplayerSymbol and gameboard[2]== theplayerSymbol:
        print(playerNumber + " Won")
        return True
    elif gameboard[3]==theplayerSymbol and  gameboard[4]== theplayerSymbol and gameboard[5]== theplayerSymbol:
        print(playerNumber + " Won")
        return True
    elif gameboard[6]==theplayerSymbol and  gameboard[7]== theplayerSymbol and gameboard[8]== theplayerSymbol:
        print(playerNumber + " Won")
        return True
    elif gameboard[0]==theplayerSymbol and  gameboard[3]== theplayerSymbol and gameboard[6]== theplayerSymbol:
        print(playerNumber + " Won")
        return True
    elif gameboard[1]==theplayerSymbol and  gameboard[4]== theplayerSymbol and gameboard[7]== theplayerSymbol:
        print(playerNumber + " Won")
        return True
    elif gameboard[2]==theplayerSymbol and  gameboard[5]== theplayerSymbol and gameboard[8]== theplayerSymbol:
        print(playerNumber + " Won")
        return True   
    elif gameboard[0]==theplayerSymbol and  gameboard[4]== theplayerSymbol and gameboard[8]== theplayerSymbol:
        print(playerNumber + " Won")
        return True     
    else:
        return False
>>>>>>> Stashed changes


displayRules()
displayBoard(layOutOftheGame)
getUserSymbol()
<<<<<<< Updated upstream
takeTurn(boardinAction)
displayBoard(boardinAction)
=======

numOfPlays = 0
while numOfPlays<9:
    userGridChoice()
    numOfPlays+=1
    if winChecks(boardinAction,"Player1",player1Symbol):
        displayBoard(boardinAction)
        break
    userGridChoice(boardinAction,"Player2",player2Symbol)
    if winChecks(boardinAction,"Player2",player2Symbol):
        displayBoard(boardinAction)
        break

>>>>>>> Stashed changes
