import random

class TicTacToe:

    def __init__(self):
        """Initialize with empty board"""
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def show(self):
        """Format and print board"""
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def clearBoard(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def whoWon(self):
        if self.checkWin() == "X":
            return "X"
        elif self.checkWin() == "O":
            return "O"
        elif self.gameOver() == True:
            return "Nobody"

    def availableMoves(self):
        """Return empty spaces on the board"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def getMoves(self, player):
        """Get all moves made by a given player"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    def makeMove(self, position, player):
        """Make a move on the board"""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        elif self.board[position] != " " and player is " " :
            self.board[position] = player
            return True
        else:
            print("Invalid Move")
            return False

    def checkWin(self):
        """Return the player that wins the game"""
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMoves(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        """Return True if X wins, O wins, or draw, else return False"""
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    #DoWorkHere
    def minimax(self, board, depth, player):
        #First I will Check Base Case
        #Lw Game Over
        #Return Elly Ksb w Score
        #Use checkWin Deh Return X Aw O Aw None==Tie
        if self.gameOver():
            winner= self.checkWin()
            if winner==None:
                return 0
            elif winner=="X":
                return -1
            else:
                return 1

        if depth%2 == 0:
            Current_Score = -5#El Score Elly Hnsah :(
            #OtherWise Play
            validPalys = self.availableMoves()
            for slot in validPalys:
                self.makeMove(slot,player)
                Current_Score=max(self.minimax(board,depth+1,changePlayer(player)),Current_Score)
                #board[slot]=" "
                self.makeMove(slot," ")

                #Hn3ml Min Max
                #Hnreturn Min Or Max 7sb Player
                #Undo Step
            return Current_Score
        else :
            Current_Score = 5  # El Score Elly Hnsah :(
            # OtherWise Play
            validPalys = self.availableMoves()
            for slot in validPalys:
                self.makeMove(slot, player)
                Current_Score = min(self.minimax(board, depth + 1, changePlayer(player)), Current_Score)
                self.makeMove(slot," ")
                # Hn3ml Min Max
                # Hnreturn Min Or Max 7sb Player
                # Undo Step
            return Current_Score

        #pass
        #Return Score Aw3a Tnsaaaaa



def changePlayer(player):
    """Returns the opposite player given any player"""
    if player == "X":
        return "O"
    else:
        return "X"

#DoWorkHere
def make_best_move(board, depth, player):
    #Iterate All over all Avaliable Postions
    #Return The Poisition With Highest Score From MinMax
    #Nagibooooo
    ourGame=TicTacToe()
    ourGame.board=board.board
    Current_Score = -5

    #ourGame.availableMoves()
    for ValidPosition in ourGame.availableMoves():
        #print(ValidPosition)
        #Fill Place
        ourGame.makeMove(ValidPosition,player)
        #Call Algo and Best Score
        score=ourGame.minimax(ourGame.board,depth+1,"X")
        #Undo Yacta
        #ourGame.board[ValidPosition]=" "
        ourGame.makeMove(ValidPosition, " ")

        #check Score
        if score>Current_Score:
            Current_Score=score
            bestMove=ValidPosition

    """
    Controllor function to initialize minimax and keep track of optimal move choices
    board - what board to calculate best move for
    depth - how far down the tree to go
    player - who to calculate best move for (Works ONLY for "O" right now)
    """
    return bestMove

# TestGame=TicTacToe()
# TestGame.board=      ["X", "O", "X",
#                       "X", "O", "O",
#                       "O", "X", "O"]
# print("Nagibo")
# if TestGame.checkWin()==None:
#     print("Nagibo Tie")

# Actual game
if __name__ == '__main__':
    game = TicTacToe()
    game.show()
    #x=game.availableMoves()
    # print("nagibo")
    # print(x)
    while game.gameOver() == False:

        isValid = False
        while not isValid:
            person_move = int(input("You are X: Choose number from 1-9: "))
            isValid =  game.makeMove(person_move - 1, "X")
        game.show()

        if game.gameOver() == True:
            break

        print("Computer choosing move...")
        ai_move = make_best_move(game, -1, "O")
        game.makeMove(ai_move, "O")
        game.show()

print("Game Over. " + game.whoWon() + " Wins")


# Implement the following 2 functions:
# make_best_move
# minimax
