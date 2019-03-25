'''
    @author Amer Sulieman
    @version 03/24/2019
    @Description TIC TAC TOE GAME
'''
gameBoardGridsNumbers = list(range(1,10))       #This will be used to check grids in the board that have been used
boardinAction = [' ']*9                         #The actual board that gets updated when user choose the position 
numOfPlays = 0                                  #Number of plays taken in the game because the max is 9
playersSymbol = {"Player1":"","Player2":""}     #DICTIONARY FOR EACH PLAYER AND THEIR SYMBOL

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

#introduces the game to the player and how it is played
def introductionToTheGame():
    displayRules()
    print("\n\tHere is your game board!\n")
    displayGameBoard(gameBoardGridsNumbers)


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
    #if reached here and there had been 9 turns then return because it is a tie, no more turns
    global numOfPlays
    if(numOfPlays==9):
        return
    playerGridChoice = input("\t"+player+" choose position: ")
    #ensure that the input is between 1 - 9 which are the grids of the game
    if validate_player_choice(gameBoardGridsNumbers,playerGridChoice):
        #player1gridchoice -1 because our array starts at 0
        gameboard[int(playerGridChoice)-1]=playersSymbol[player]
        gameBoardGridsNumbers.remove(int(playerGridChoice))
        #print game baord at every turn
        displayGameBoard(gameboard)
    else:
        print("\tPlease choose UNUSED position between 1 and 9!!!")
        takeTurn(gameboard,player)

def validate_player_choice(positionsUsed,positionPicked):
    if positionPicked.isdigit() and int(positionPicked) in range(1,10) and int(positionPicked) in (positionsUsed):
            return True
    else: 
        return False

def winChecks(gameboard,player):
    if gameboard[0]==playersSymbol[player] and  gameboard[1]== playersSymbol[player] and gameboard[2]== playersSymbol[player]:
        return True
    elif gameboard[3]==playersSymbol[player] and  gameboard[4]==playersSymbol[player] and gameboard[5]== playersSymbol[player]:
        return True
    elif gameboard[6]==playersSymbol[player] and  gameboard[7]== playersSymbol[player] and gameboard[8]== playersSymbol[player]:
        return True
    elif gameboard[0]==playersSymbol[player] and  gameboard[3]== playersSymbol[player] and gameboard[6]==playersSymbol[player]:
        return True
    elif gameboard[1]==playersSymbol[player] and  gameboard[4]== playersSymbol[player] and gameboard[7]== playersSymbol[player]:
        return True
    elif gameboard[2]==playersSymbol[player] and  gameboard[5]== playersSymbol[player] and gameboard[8]== playersSymbol[player]:
        return True   
    elif gameboard[0]==playersSymbol[player] and  gameboard[4]== playersSymbol[player] and gameboard[8]== playersSymbol[player]:
        return True
    elif gameboard[2]==playersSymbol[player] and  gameboard[4]== playersSymbol[player] and gameboard[6]== playersSymbol[player]:
        return True          
    else:
        return False

def beginGameLoopForPlayers():
    global numOfPlays
    #max of turns taken is 9 because we have 9 grids, if all filled then it is tie
    while numOfPlays<9:
        takeTurn(boardinAction,"Player1")
        numOfPlays+=1
        if winChecks(boardinAction,"Player1"):
            displayGameBoard(boardinAction)
            print("\tWOHOOOOOOOO Player1 WON!!!!!!!")
            break
        takeTurn(boardinAction,"Player2")
        numOfPlays+=1
        if winChecks(boardinAction,"Player2"):
            displayGameBoard(boardinAction)
            print("\t WOHOOOOOOOO Player2 WON!!!!!!!")
            break
    else:
        print("\tIt's a tie!!!")


def gameDataReset():
    global gameBoardGridsNumbers
    global boardinAction
    global numOfPlays
    #reset number of play
    numOfPlays=0
    #reset grids numbers
    gameBoardGridsNumbers=list(range(1,10))
    #rest the board displayed at each turn
    boardinAction= [" "]*9

def startGame():
    getUserSymbol()
    beginGameLoopForPlayers()

introductionToTheGame()
#first game round
startGame()
#boolean to check if players want to play again
keepPlaying =True
while keepPlaying:
    userChoice = input("\tPress Y to replay...\n\tOr press N to exit... ").lower()
    if userChoice == "n":
        keepPlaying =False
    elif userChoice == "y":
        gameDataReset() #reset game data
        displayGameBoard(gameBoardGridsNumbers) #display the grids
        startGame()     #start game from scratch
    #if user pressed any other input, reensure Y or N
    else:
        print("Please enter Y or N....")
        

         

