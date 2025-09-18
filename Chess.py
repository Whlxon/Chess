'''
Chess Class

There is the signification of all piece on the grid

1: piont
2: tour
3: cavalier
4: fou
5: roi
6: reine

'''

class ChessGame:
    def __init__(self):
        self.grid = [
            [2, 3, 4, 6, 5, 4, 3, 2],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [2, 3, 4, 6, 5, 4, 3, 2],
        ]

        self.checkMate = False
    
    def legalMove(self, piece):
        match piece:
            case "":
                pass
            case "":
                pass
    
    def transformGrid(self):
        pass

    