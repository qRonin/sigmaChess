from enum import Enum

class factionColor (Enum):
    FACTION_WHITE = 1;
    FACTION_BLACK = 2;

class chessPiece:

    def __init__(self, hX, hY, faction):
        self.x = hX;
        self.y = hY;
        self.faction=faction;

class piecePawn(chessPiece):

    def checkAttack(self, boardArray, attackX, attackY):
        if self.faction == FACTION_WHITE:
            if attackY == self.y + 1 and (abs(attackX - self.x == 1)):
                if boardArray[attackX][attackY] is not None:
                    return True;
            return False;
        else:
            if attackY == self.y - 1 and (abs(attackX - self.x == 1)):
                if boardArray[attackX][attackY] is not None:
                    return True;
            return False;

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        if self.faction == FACTION_WHITE:
            if coordHorizontal == self.x and coordVert == self.y + 1:
                if boardArray[coordHorizontal][coordVert + 1] == None:
                    return True;
            return False;
        else:
            if coordHorizontal == self.x and coordVert == self.y - 1:
                if boardArray[coordHorizontal][coordVert - 1] == None:
                    return True;
            return False;


