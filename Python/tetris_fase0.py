'''
Copyright (C) 2025 Antonio de Andrés Lema

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox

class Square():
    '''
    Clase que implementa un cadrado do xogo do Tetris
    '''
    # Coordenadas do cadrado no panel do xogo
    __x:int
    __y:int
    # Etiqueta que mostra o cadrado no panel
    __lblSquare:QLabel
    # Código en forma de texto coa cor do cadrado
    __fillColor:str

    def getX(self) -> int:
        '''
        Obtén a coordenada x do cadrado
        '''
        return self.__x
    
    def setX(self, x:int) -> None:
        '''
        Establece a coordenada x do cadrado
        '''
        self.__x = x
        self.__lblSquare.setGeometry(QtCore.QRect(self.__x, self.__y, Game.SQUARE_SIDE, Game.SQUARE_SIDE))
    
    def getY(self) -> int:
        '''
        Obtén a coordenada y do cadrado
        '''
        return self.__y
    
    def setY(self, y:int) -> None:
        '''
        Establece a coordenada y do cadrado
        '''
        self.__y = y
        self.__lblSquare.setGeometry(QtCore.QRect(self.__x, self.__y, Game.SQUARE_SIDE, Game.SQUARE_SIDE))
        
    def getCoordinates(self) -> str:
        '''
        Obtén a representación das coordenadas x, y do cadrado en forma de String
        '''
        return str(self.__x) + ',' + str(self.__y)
    
    def getLblSquare(self) -> QLabel:
        '''
        Obtén a referenza á etiqueta que representa graficamente o cadrado
        '''
        return self.__lblSquare

    def getFillColor(self) -> str:
        '''
        Cor de recheo do cadrado
        '''
        return self.__fillColor
    
    def setFillColor(self, fillColor:str) -> None:
        '''
        Establece a cor do cadrado
        '''
        self.__fillColor = fillColor
        self.__lblSquare.setStyleSheet("background-color: " + fillColor + ";\n"
                                "border: 1px solid black;")

    def __init__(self, x:int, y:int, fillColor:str, game:'Game') -> None:
        '''
        Crea un cadrado establecendo as súas coordenadas, cor e referenza ao xogo
        '''
        # Almacenamos os valores dos parámetros nos atributos
        self.__x = x
        self.__y = y
        self.__fillColor = fillColor
        # Creamos a etiqueta que representa o cadrado e establecemos as súas propidades
        self.__lblSquare = QLabel()
        self.__lblSquare.setGeometry(QtCore.QRect(x, y, Game.SQUARE_SIDE, Game.SQUARE_SIDE))
        self.__lblSquare.setStyleSheet('background-color: ' + fillColor + ';\n'
                                'border: 1px solid black;')
        # Chamamos á ventá principal do xogo para pintar o cadrado no panel
        game.mainWindow.drawSquare(self.__lblSquare)

class Piece():
    '''
    Clase que implementa a peza cadrada do xogo do Tetris
    '''
    # Referenza ao obxecto xogo
    game:'Game'
    # Referenzas aos 4 cadrados que forman a peza
    # 1.4 edit
    a:Square
    b:Square
    c:Square
    d:Square

    # si en python no hay get y set entonces usar __ en el constructor
    # si hay get y set entonces arriban van sin __ (ejm:square)
    def __init__(self, game:'Game') -> None:
        '''
        Crea unha peza cadrada cos 4 cadrados
        '''
        self.__game = game
        self.__a = Square(Game.MAX_X//2 - Game.SQUARE_SIDE, 0, 'rgb(0,0,255)', game)
        self.__b = Square(Game.MAX_X//2, 0, 'rgb(0,0,255)', game)
        self.__c = Square(Game.MAX_X//2 - Game.SQUARE_SIDE, Game.SQUARE_SIDE, 'rgb(0,0,255)', game)
        self.__d = Square(Game.MAX_X//2, Game.SQUARE_SIDE, 'pink', game)

    def moveRight(self) -> bool:
        '''
        Move a ficha á dereita se é posible
        Devolve True se o movemento da ficha é posible, se non False
        '''
        # Se os cadrados b ou d se saen pola dereita do panel do xogo, o
        # movemento non é posible
        # si el mayor de las x de los squares es igual a max -

        x_coords = [self.__a.getX(), self.__b.getX(), self.__c.getX(), self.__d.getX()]
    
        # Calcular la mayor coordenada x
        bigger_x = max(x_coords)

        # calcula ese x añadiendo la distancia a recorrer
        new_x = bigger_x + Game.SQUARE_SIDE

        if not Game.isValidPosition(Game,new_x,self.__a.getY()):
            return False  # no mover

        # mover todos los cuadrados a la derecha
        self.__a.setX(self.__a.getX() + Game.SQUARE_SIDE)
        self.__b.setX(self.__b.getX() + Game.SQUARE_SIDE)
        self.__c.setX(self.__c.getX() + Game.SQUARE_SIDE)
        self.__d.setX(self.__d.getX() + Game.SQUARE_SIDE)

        return True
    
    def moveLeft(self) -> bool:
        '''
        Move a ficha á esquerda se é posible
        Devolve True se o movemento da ficha é posible, se non False
        '''

        x_coords = [self.__a.getX(), self.__b.getX(), self.__c.getX(), self.__d.getX()]
    
        # Calcular la mayor coordenada x
        smaller_x = min(x_coords)

        # calcula ese x añadiendo la distancia a recorrer
        new_x = smaller_x - Game.SQUARE_SIDE

        if not Game.isValidPosition(Game,new_x,self.__a.getY()):
            return False  # no mover

        # mover todos los cuadrados a la izq
        self.__a.setX(self.__a.getX() - Game.SQUARE_SIDE)
        self.__b.setX(self.__b.getX() - Game.SQUARE_SIDE)
        self.__c.setX(self.__c.getX() - Game.SQUARE_SIDE)
        self.__d.setX(self.__d.getX() - Game.SQUARE_SIDE)

        return True
    
    def moveDown(self) -> bool:
        '''
        Move a ficha abaixo se é posible
        Devolve True se o movemento da ficha é posible, se non False
        '''
        y_coords = [self.__a.getY(), self.__b.getY(), self.__c.getY(), self.__d.getY()]
    
        # Calcular la mayor coordenada 
        bigger_y = max(y_coords)

        # calcula ese  añadiendo la distancia a recorrer
        new_y = bigger_y + Game.SQUARE_SIDE

        if not Game.isValidPosition(Game,0, new_y):
            return False  # no mover

        # mover todos los cuadrados
        self.__a.setY(self.__a.getY() + Game.SQUARE_SIDE)
        self.__b.setY(self.__b.getY() + Game.SQUARE_SIDE)
        self.__c.setY(self.__c.getY() + Game.SQUARE_SIDE)
        self.__d.setY(self.__d.getY() + Game.SQUARE_SIDE)

        return True
    

    # rotar 180deg
    def rotate(self) -> bool:
        '''
        Rota a ficha se é posible
        Devolve True se o movemento da ficha é posible, se non False
        '''
        # A rotación da ficha cadrada non supón ningunha variación na ficha,
        # por iso simplemente devolvemos true

        # 
        
        return True


# class PieceL(Piece):
#     # Referenza ao obxecto xogo
#     game:'Game'
#     # Referenzas aos 4 cadrados que forman a peza
#     # 1.4 
#     a:Square
#     b:Square
#     c:Square
#     d:Square

    
#     def __init__(self, game:'Game') -> None:
#         '''
#         Crea unha peza L
#         '''
#         self.__game = game
#         self.__a = Square(Game.MAX_X//2 - (Game.SQUARE_SIDE*2), 0, 'rgb(0,0,255)', game)
#         self.__b = Square(Game.MAX_X//2 - (Game.SQUARE_SIDE*2), Game.SQUARE_SIDE, 'rgb(0,0,255)', game)
#         self.__c = Square(Game.MAX_X//2 - Game.SQUARE_SIDE, Game.SQUARE_SIDE, 'rgb(0,0,255)', game)
#         self.__d = Square(Game.MAX_X//2, Game.SQUARE_SIDE, 'rgb(0,0,255)', game)
      

#     def moveRight(self) -> bool:
#         Piece.moveRight(self)
    
#     def moveLeft(self) -> bool:
#         Piece.moveLeft(self)
    
#     def moveDown(self) -> bool:
#         Piece.moveDown(self)
    
#     def rotate(self) -> bool:
#         Piece.rotate(self)


class Game():
    '''
    Clase que implementa o comportamento do xogo do Tetris
    '''
    # Constante que define o tamaño en pixels do lado dun cadrado
    SQUARE_SIDE:int = 20
    # Constante que define o valor máximo da coordenada x no panel de cadrados
    MAX_X:int = 160
    # Referenza á peza actual do xogo, que é a única que se pode mover
    __currentPiece:Piece
    # Referenza á ventá principal do xogo
    mainWindow:'MainWindow'
    # Flag que indica se o xogo está en pausa ou non
    paused:bool
    # Número de liñas feitas no xogo
    numberOfLines:int

    def __init__(self, mainWindow:'MainWindow') -> None:
        '''
        Inicializa unha nova partida, cunha peza inicial
        '''
        self.paused = False
        self.numberOfLines = 0
        self.mainWindow = mainWindow
        self.__createNewPiece() 
    
    def movePieceRight(self) -> None:
        '''
        Move a ficha actual á dereita, se o xogo non está pausado
        '''
        if not self.paused:
            self.__currentPiece.moveRight()
    
    def movePieceLeft(self) -> None:
        '''
        Move a ficha actual á esquerda, se o xogo non está pausado
        '''
        if not self.paused:
            self.__currentPiece.moveLeft()
    
    def rotatePiece(self) -> None:
        '''
        Rota a ficha actual, se o xogo non está pausado
        '''
        if not self.paused:
            self.__currentPiece.rotate()
    
    def movePieceDown(self) -> None:
        '''
        Move a peza actual abaixo, se o xogo non está pausado Se a peza choca
        con algo e xa non pode baixar, pasa a formar parte do chan e créase unha
        nova peza
        '''
        if not self.paused and not self.__currentPiece.moveDown():
            self.__addPieceToGround()
            self.__createNewPiece()
            if self.__hitPieceTheGround():
                self.mainWindow.showGameOver()
    
    # dejar como está
    def isValidPosition(self, x:int, y:int) -> bool:
        '''
        Método que permite saber se unha posición x,y é válida para un cadrado
        '''
        print('hiiiiiiii')
        if x == Game.MAX_X or x < 0 or y == 200:
            return False
        return True
    
    def __createNewPiece(self) -> None:
        '''
        Crea unha nova peza e a establece como peza actual do xogo
        '''
        self.__currentPiece = Piece(self)
        # self.__currentPiece = PieceL(self)
        # pass

    def __addPieceToGround(self) -> None:
        '''
        Engade unha peza ao chan
        '''
        # Engadimos os cadrados da peza ao chan

        # Chamamos ao método que borra as liñas do chan que estean completas
        self.__deleteCompletedLines()
        
    def __deleteCompletedLines(self) -> None:
        '''
        Se os cadrados que están forman unha liña completa, bórranse eses
        cadrados do chan e súmase unha nova liña no número de liñas realizadas
        '''
        pass

    def __deleteLine(self, y:int) -> None:
        '''
        Borra todos os cadrados que se atopan na liña indicada pola coordenada y,
        e baixa todos os cadrados que estean situados por enriba unha posición
        cara abaixo
        '''
        pass

    def __hitPieceTheGround(self) -> bool:
        '''
        Comproba se a peza actual choca cos cadrados do chan
        '''
        # Polo momento, non facemos nada

        #borrador..
        # if not self.__currentPiece.moveDown():
        #     return True
        # a = self.__currentPiece.a.getCoordinates()
        return False

class MainWindow(QMainWindow):
    '''
    Clase que implementa a ventá principal do xogo do Tetris
    '''
    # Referenza ao obxecto do xogo actual
    __game:Game|None

    def __init__(self) -> None:
        '''
        Inicializa unha nova ventá principal
        '''
        super().__init__()
        # Establecemos o xogo a nulo
        self.__game = None
    
    def drawSquare(self, lblSquare:QLabel) -> None:
        '''
        Pinta un cadrado no panel do xogo
        '''
        lblSquare.setParent(self.pnlGame)
        lblSquare.show()
    
    def deleteSquare(self, lblSquare:QLabel) -> None:
        '''
        Borra un cadrado do panel do xogo
        '''
        self.pnlGame.children().remove(lblSquare)
        lblSquare.deleteLater()

    def showNumberOfLines(self, numberOfLines:int) -> None:
        '''
        Actualiza na ventá o número de liñas que van feitas no xogo
        USAR CUANDO DESAPAREZCA 1 LINEA
        '''
        self.lblNumberOfLines.setText(str(numberOfLines))
    
    def showGameOver(self) -> None:
        '''
        Mostra unha mensaxe informando ao usuario do final do xogo
        '''
        self.__game = None
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Fin')
        dlg.setText('Fin do xogo')
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        dlg.exec()
    
    def __startGame(self) -> None:
        '''
        Inicia un novo xogo
        '''
        # Limpamos todo o que puidese haber pintado no panel do xogo
        for label in self.pnlGame.children():
            self.pnlGame.children().remove(label)
            label.deleteLater()
        # Creamos un novo obxecto xogo
        self.__game = Game(self)
        # Desactivamos o botón de pausa
        self.btnPause.setChecked(False)
        # Establecemos o número de liñas que se mostran na ventá a cero
        self.lblNumberOfLines.setText('0')

    def setupUi(self, MainWindow:'MainWindow'):
        '''
        Método que configura os compoñentes da ventá, xerado con QT Designer
        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(200, 380))
        MainWindow.setMaximumSize(QtCore.QSize(200, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnNewGame = QtWidgets.QPushButton(self.centralwidget)
        self.btnNewGame.setGeometry(QtCore.QRect(10, 10, 111, 27))
        self.btnNewGame.setObjectName("btnNewGame")
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        self.btnPause.setGeometry(QtCore.QRect(130, 10, 61, 27))
        self.btnPause.setCheckable(True)
        self.btnPause.setObjectName("btnPause")
        self.pnlGame = QtWidgets.QWidget(self.centralwidget)
        self.pnlGame.setGeometry(QtCore.QRect(20, 80, 160, 200)) #left, top, w, h
        self.pnlGame.setStyleSheet("background-color: pink;")
        self.pnlGame.setObjectName("pnlGame")
        self.lblLines = QtWidgets.QLabel(self.centralwidget)
        self.lblLines.setGeometry(QtCore.QRect(10, 50, 51, 19))
        self.lblLines.setObjectName("lblLines")
        self.lblNumberOfLines = QtWidgets.QLabel(self.centralwidget)
        self.lblNumberOfLines.setGeometry(QtCore.QRect(110, 50, 76, 19))
        self.lblNumberOfLines.setText("")
        self.lblNumberOfLines.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNumberOfLines.setObjectName("lblNumberOfLines")
        self.btnRotate = QtWidgets.QPushButton(self.centralwidget)
        self.btnRotate.setGeometry(QtCore.QRect(50, 290, 100, 27))
        self.btnRotate.setObjectName("btnRotate")
        self.btnLeft = QtWidgets.QPushButton(self.centralwidget)
        self.btnLeft.setGeometry(QtCore.QRect(10, 320, 91, 27))
        self.btnLeft.setObjectName("btnLeft")
        self.btnRight = QtWidgets.QPushButton(self.centralwidget)
        self.btnRight.setGeometry(QtCore.QRect(110, 320, 81, 27))
        self.btnRight.setObjectName("btnRight")
        self.btnDown = QtWidgets.QPushButton(self.centralwidget)
        self.btnDown.setGeometry(QtCore.QRect(50, 350, 100, 27))
        self.btnDown.setObjectName("btnDown")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Conectamos os sinais cos slots
        self.btnNewGame.pressed.connect(self.__btnNewGamePressed)
        self.btnPause.pressed.connect(self.__btnPausePressed)
        self.btnRotate.pressed.connect(self.__btnRotatePressed)
        self.btnLeft.pressed.connect(self.__btnLeftPressed)
        self.btnRight.pressed.connect(self.__btnRightPressed)
        self.btnDown.pressed.connect(self.__btnDownPressed)

    def retranslateUi(self, MainWindow:'MainWindow'):
        '''
        Método que configura os textos da ventá, xerado con QT Designer
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tetris"))
        self.btnNewGame.setText(_translate("MainWindow", "Nova partida"))
        self.btnPause.setText(_translate("MainWindow", "Pausa"))
        self.lblLines.setText(_translate("MainWindow", "Liñas:"))
        self.btnRotate.setText(_translate("MainWindow", "Rotar"))
        self.btnLeft.setText(_translate("MainWindow", "Esquerda"))
        self.btnRight.setText(_translate("MainWindow", "Dereita"))
        self.btnDown.setText(_translate("MainWindow", "Abaixo"))

    # Slots para a captura de eventos
    def __btnNewGamePressed(self) -> None:
        # Ao picar no botón de "Nova partida", invocamos ao método privado 
        # que inicia un novo xogo
        self.__startGame()

    def __btnPausePressed(self) -> None:
        # Ao picar no botón de "Pausa", chamamos ao obxecto xogo para 
        # establecer o atributo de pausa no estado do botón
        if self.__game is not None:
            self.__game.paused = not self.btnPause.isChecked()

    def __btnRotatePressed(self) -> None:
        # Ao picar no botón de "Rotar", chamamos ao obxecto xogo para que 
        # rote a peza actual
        if self.__game is not None:
            self.__game.rotatePiece()

    def __btnLeftPressed(self) -> None:
        # Ao picar no botón de "Esquerda", chamamos ao obxecto xogo para que
        # se mova a peza actual á esquerda
        if self.__game is not None:
            self.__game.movePieceLeft()

    def __btnRightPressed(self) -> None:
        # Ao picar no botón de "Dereita", chamamos ao obxecto xogo para que
        # se mova a peza actual á dereita
        if self.__game is not None:
            self.__game.movePieceRight()

    def __btnDownPressed(self) -> None:
        # Ao picar no botón de "Abaixo", chamamos ao obxecto xogo para que
        # se mova a peza actual cara abaixo
        if self.__game is not None:
            self.__game.movePieceDown()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())
