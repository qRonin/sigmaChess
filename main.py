from pieces import *

class chessBoard:
    boardArray = [[]]

    def __init__(self):
        self.boardArray = self.__spawnPieces()

    def __createEmptyArray(self):
        hArray = []
        for i in range(8):
            hArray.append([])
            for k in range(8):
                hArray[i].append(None)
        return hArray

    def __spawnPieces(self):
        boardArray = self.__createEmptyArray()
        for i in range(2):
            for k in range(8):
                boardArray[k][i] = piecePawn(k, i)
        return boardArray

    def movePiece(self, pieceToMove, xNew, yNew):
        isAttack = pieceToMove.checkAttack(self.boardArray,coordHorizontal=xNew, coordVert=yNew)
        if isAttack == True:
            self.__move(pieceToMove, xNew, yNew)
            return True
        isLegal = pieceToMove.checkMove(self.boardArray,coordHorizontal=xNew, coordVert=yNew)
        if isLegal == True:
            self.__move(pieceToMove, xNew, yNew)
            return True


    def __move(self,pieceToMove, xNew, yNew):
        xCurrent = pieceToMove.x
        yCurrent = pieceToMove.y
        self.boardArray[xNew][yNew] = pieceToMove
        self.boardArray[xCurrent][yCurrent] = None


    def getPiece(self,coordHorizontal, coordVert):
        return self.boardArray[coordHorizontal][coordVert]

    def PRINTBOARD(self):
        for i in range(8):
            print("\n")
            for j in range(8):
                if type(self.boardArray[j][7 - i]) is piecePawn:
                    print("P", end="")
                else:
                    print("-", end="")