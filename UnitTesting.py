import os, random
import oxo_data
import doctest, unittest
class Game():
    def __init__(self):
        self.board = list(" " * 9)
 
    def save(self, game):
        ' save game to disk '
        oxo_data.saveGame(self.board)
 
    def restore(self):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            self.board = oxo_data.restoreGame()
            if len(self.board) != 9:
                self.board = list(" " * 9)
                return self.board
        except IOError:
            self.board = list(" " * 9)
            return self.board
 
    def _generateMove(self):
        ''' generate a random cell from thiose available.
            If all cells are used return -1'''
        options = [i for i in range(len(self.board)) if  self.board[i] == " "]
        if options:
           return random.choice(options)
        else: return -1
 
    def _isWinningMove(self):
        """ Return the winning combination
>>> wins = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)))
>>> for a,b,c in wins:
        ...     chars = game[a] + game[b] + game[c]
        ...     if chars == 'XXX' or chars == 'OOO':
        ...         return True
        ... return False
        True
>>> wins = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)))
>>> for a,b,c in wins:
        ...     chars = game[a] + game[b] + game[c]
        ...     if chars == 'XXX' or chars == 'OOO':
        ...         return True
        ... return False
        False
        """
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))
        game = self.board
        for a,b,c in wins:
            chars = game[a] + game[b] + game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False
 
    def userMove(self,cell):
        if self.board[cell] != ' ':
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
    """ Return the result of the game.
>>> result = ""
>>> game = Game()
>>> while not result:
    ...    print(game)
    ...    try:
    ...       result = game.userMove(game, _generateMove(game))
    ...    except ValueError:
    ...        print("Oops, that shouldn't happen")
    ...    if not result:
    ...        result = game.computerMove(game)
    ...    if not result: continue
    ...    elif result == 'D':
    ...        print("Its a draw")
    ...    else:
    ...        print("Winner is:", result)
    ...    return result
    'X'
>>> result = ""
>>> game = Game()
>>> while not result:
    ...    print(game)
    ...    try:
    ...       result = game.userMove(game, _generateMove(game))
    ...    except ValueError:
    ...        print("Oops, that shouldn't happen")
    ...    if not result:
    ...        result = game.computerMove(game)
    ...    if not result: continue
    ...    elif result == 'D':
    ...        print("Its a draw")
    ...    else:
    ...        print("Winner is:", result)
    ... return result
    'O'
>>> result = ""
>>> game = Game()
>>> while not result:
    ...    print(game)
    ...    try:
    ...       result = game.userMove(game, _generateMove(game))
    ...    except ValueError:
    ...        print("Oops, that shouldn't happen")
    ...    if not result:
    ...        result = game.computerMove(game)
    ...    if not result: continue
    ...    elif result == 'D':
    ...        print("Its a draw")
    ...    else:
    ...        print("Winner is:", result)
    ...    return result
    'D'
    """
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
        return result
class TestMyCode(unittest.TestCase):
    def unitTest(self):
        result = test()
        if result == 'X':
            self.assertEqual(result,'X')
        elif result == 'O':
            self.assertEqual(result,'O')
        else:
            self.assertEqual(result,'D')
        return
if __name__ == "__main__":
    test()
    print("\n\nTesting using the doctest function")
    doctest.testmod()
 
    print("\n\nTesting using the unitTest function")
    unittest.main()
