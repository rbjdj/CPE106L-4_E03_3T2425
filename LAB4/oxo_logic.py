''' This is the main logic for a Tic-tac-toe game.
It is not optimised for a quality game it simply
generates random moves and checks the results of
a move for a winning line. Exposed functions are:
newGame()
saveGame()
restoreGame()
userMove()
computerMove()
'''
 
import os, random
import oxo_data
 
class Game:
    def __init__(self):
        self.board = list(" " * 9)
 
    def saveGame(self):
        ' save game to disk '
        oxo_data.saveGame(self.board)
    def restoreGame(self):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            self.board = oxo_data.restoreGame()
            if len(self.board) == 9:
                return
            else:
                self.board = list(" " * 9)
        except IOError:
            self.board = list(" " * 9)
    def _generateMove(self):
        ''' generate a random cell from those available.
            If all cells are used return -1'''
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1
    def _isWinningMove(self):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))
 
        for a,b,c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False
 
    def userMove(self,cell):
        if self.board[cell]!= ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
        if self._isWinningMove():
            return 'X'
        else:
            return ""
 
    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._isWinningMove():
            return 'O'
        else:
            return ""
 
def test():
    result = ""
    game = Game()
    while not result:
        print(game.board)
        try:
            result = game.userMove(game._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computerMove()
        if not result: continue
        elif result == 'D':
            print("Its a draw")
        else:
            print("Winner is:", result)
        print(game.board)
 
if __name__ == "__main__":
    test()
 
            
