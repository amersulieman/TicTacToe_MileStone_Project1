gameBoardGridsNumbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
boardinAction = [' ']*9
playersSymbol = {"Player1":"","Player2":""}

def displayRules():
    print("\t"+"**"*32)
    print("\t*\t\t\tWelcome to Tic Tac Toe Game\t\n\t*")
    print("\t*\tThe rules are simple..."
          +"\n\t*\t1)Player1 chooses: X or O"
          +"\n\t*\t2)Player2 gets the other symbol"
          +"\n\t*\t2)Game board will be shown with position numbers "
          +"\n\t*\tAt every turn:"
          +"\n\t*\t   1. Pick a grid number to place your symbol"
          +"\n\t*\t   2) keep playing until your symbols are 3 in a row"
          +"\n\t*\t   3) Have Fun..")
    print("\t"+"**"*32)


def displayGameBoard(board):
    print("\t\t{} | {} | {}".format(board[0],board[1],board[2]))
    print("\t\t" +"-"*9)
    print("\t\t{} | {} | {}".format(board[3],board[4],board[5]))
    print("\t\t" +"-"*9)
    print("\t\t{} | {} | {}".format(board[6],board[7],board[8]))


def getUserSymbol():
    player1Symbol = input("\tPlayer 1:  X or O ? ").lower()
    #ensure player 1 only choose "x" or "O"
    if player1Symbol =="x":
        playersSymbol["Player1"]="X"
        playersSymbol["Player2"]="O"
    elif player1Symbol =="o":
        playersSymbol["Player1"]="O"
        playersSymbol["Player2"]="X"
    #This else is if the input was other than x or o
    else:
        print("\tPLEASE ONLY CHOOSE X or O !!!")
        getUserSymbol()


def takeTurn(gameboard,player):
    playerGridChoice = input("\t"+player+" choose position: ")
    #ensure that the input is between 1 - 9 which are the grids of the game
    if playerGridChoice.isdigit() and int(playerGridChoice) in range(1,10):
        #player1gridchoice -1 because our array starts at 0
        gameboard[int(playerGridChoice)-1]=playersSymbol[player]
        #print game baord at every turn
        displayGameBoard(gameboard)
    else:
        print("\tPlease choose appropriate grid number between 1 - 9 ")
        takeTurn(gameboard,player)

def winChecks(gameboard,player):
    if gameboard[0]==playersSymbol[player] and  gameboard[1]== playersSymbol[player] and gameboard[2]== playersSymbol[player]:
        print(player + " Won")
        return True
    elif gameboard[3]==playersSymbol[player] and  gameboard[4]==playersSymbol[player] and gameboard[5]== playersSymbol[player]:
        print(player + " Won")
        return True
    elif gameboard[6]==playersSymbol[player] and  gameboard[7]== playersSymbol[player] and gameboard[8]== playersSymbol[player]:
        print(player + " Won")
        return True
    elif gameboard[0]==playersSymbol[player] and  gameboard[3]== playersSymbol[player] and gameboard[6]==playersSymbol[player]:
        print(player + " Won")
        return True
    elif gameboard[1]==playersSymbol[player] and  gameboard[4]== playersSymbol[player] and gameboard[7]== playersSymbol[player]:
        print(player + " Won")
        return True
    elif gameboard[2]==playersSymbol[player] and  gameboard[5]== playersSymbol[player] and gameboard[8]== playersSymbol[player]:
        print(player + " Won")
        return True   
    elif gameboard[0]==playersSymbol[player]and  gameboard[4]== playersSymbol[player] and gameboard[8]== playersSymbol[player]:
        print(player + " Won")
        return True     
    else:
        return False


displayRules()
print("\n\tHere is your game board!\n")
displayGameBoard(gameBoardGridsNumbers)
getUserSymbol()

numOfPlays = 0
while numOfPlays<9:
    takeTurn(boardinAction,"Player1")
    numOfPlays+=1
    if winChecks(boardinAction,"Player1"):
        displayGameBoard(boardinAction)
        break
    takeTurn(boardinAction,"Player2")
    numOfPlays+=1
    if winChecks(boardinAction,"Player2"):
        displayGameBoard(boardinAction)
        break
