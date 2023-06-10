from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import sys

class Ui_Slosnost(object):
    def setupUi(self, Slosnost):
        Slosnost.setObjectName("Slosnost")
        Slosnost.resize(500, 800)
        self.label = QtWidgets.QLabel(Slosnost)
        self.label.setGeometry(QtCore.QRect(140, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Btn_GLMenu = QtWidgets.QPushButton(Slosnost)
        self.Btn_GLMenu.setGeometry(QtCore.QRect(0, 0, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Btn_GLMenu.setFont(font)
        self.Btn_GLMenu.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.Btn_GLMenu.setObjectName("Btn_GLMenu")
        self.Btn_Easy = QtWidgets.QPushButton(Slosnost)
        self.Btn_Easy.setGeometry(QtCore.QRect(200, 270, 111, 31))
        self.Btn_Easy.setObjectName("Btn_Easy")
        self.Btn_Medium = QtWidgets.QPushButton(Slosnost)
        self.Btn_Medium.setGeometry(QtCore.QRect(200, 310, 111, 31))
        self.Btn_Medium.setObjectName("Btn_Medium")
        self.Btn_Hard = QtWidgets.QPushButton(Slosnost)
        self.Btn_Hard.setGeometry(QtCore.QRect(200, 350, 111, 31))
        self.Btn_Hard.setObjectName("Btn_Hard")

        self.retranslateUi(Slosnost)
        QtCore.QMetaObject.connectSlotsByName(Slosnost)

    def retranslateUi(self, Slosnost):
        _translate = QtCore.QCoreApplication.translate
        Slosnost.setWindowTitle(_translate("Slosnost", "Кликомания"))
        self.label.setText(_translate("Slosnost", "Сложности игры"))
        self.Btn_GLMenu.setText(_translate("Slosnost", "Назад"))
        self.Btn_Easy.setText(_translate("Slosnost", "Easy"))
        self.Btn_Medium.setText(_translate("Slosnost", "Medium"))
        self.Btn_Hard.setText(_translate("Slosnost", "Hard"))

class Ui_ElUprav(object):
    def setupUi(self, ElUprav):
        ElUprav.setObjectName("ElUprav")
        ElUprav.resize(500, 800)
        self.label = QtWidgets.QLabel(ElUprav)
        self.label.setGeometry(QtCore.QRect(110, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Btn_GLMenu = QtWidgets.QPushButton(ElUprav)
        self.Btn_GLMenu.setGeometry(QtCore.QRect(0, 0, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Btn_GLMenu.setFont(font)
        self.Btn_GLMenu.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.Btn_GLMenu.setObjectName("Btn_GLMenu")
        self.label_2 = QtWidgets.QLabel(ElUprav)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 131, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/home/plombirka17/Новый ОС/Projeck/Proect/Клик мыши.ico"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ElUprav)
        self.label_3.setGeometry(QtCore.QRect(140, 310, 171, 17))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(ElUprav)
        QtCore.QMetaObject.connectSlotsByName(ElUprav)

    def retranslateUi(self, ElUprav):
        _translate = QtCore.QCoreApplication.translate
        ElUprav.setWindowTitle(_translate("ElUprav", "Кликомания"))
        self.label.setText(_translate("ElUprav", "Элементы управления"))
        self.Btn_GLMenu.setText(_translate("ElUprav", "Назад"))
        self.label_3.setText(_translate("ElUprav", "- уничтожение блоков"))

class Ui_Rule_Play(object):
    def setupUi(self, Rule_Play):
        Rule_Play.setObjectName("Rule_Play")
        Rule_Play.resize(500, 800)
        self.label = QtWidgets.QLabel(Rule_Play)
        self.label.setGeometry(QtCore.QRect(160, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Btn_GLMenu = QtWidgets.QPushButton(Rule_Play)
        self.Btn_GLMenu.setGeometry(QtCore.QRect(0, 0, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Btn_GLMenu.setFont(font)
        self.Btn_GLMenu.setStyleSheet("background-color: rgb(237, 51, 59);")
        self.Btn_GLMenu.setObjectName("Btn_GLMenu")
        self.label_2 = QtWidgets.QLabel(Rule_Play)
        self.label_2.setGeometry(QtCore.QRect(30, 270, 441, 261))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Rule_Play)
        QtCore.QMetaObject.connectSlotsByName(Rule_Play)

    def retranslateUi(self, Rule_Play):
        _translate = QtCore.QCoreApplication.translate
        Rule_Play.setWindowTitle(_translate("Rule_Play", "Кликомания"))
        self.label.setText(_translate("Rule_Play", "Правила игры"))
        self.Btn_GLMenu.setText(_translate("Rule_Play", "Назад"))
        self.label_2.setText(_translate("Rule_Play", "Суть игрового процесса заключается в очистке игрового поля, кликая на блоки одинакового цвета. Чем больше блоков вы удалите одним касанием, тем больше получите очков, отчищая поле от блоков игра продолжается на том же уровне сложности до тех пор пока на поле не останутся блоки которые невозможно удалить, после чего счёт очков сбрасывается и игра начинается снова"))

class Ui_GLMenu(object):
    def setupUi(self, GLMenu):
        GLMenu.setObjectName("GLMenu")
        GLMenu.setWindowModality(QtCore.Qt.NonModal)
        GLMenu.resize(500, 800)
        self.label = QtWidgets.QLabel(GLMenu)
        self.label.setGeometry(QtCore.QRect(140, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Btn_Play = QtWidgets.QPushButton(GLMenu)
        self.Btn_Play.setGeometry(QtCore.QRect(160, 240, 181, 41))
        self.Btn_Play.setObjectName("Btn_Play")
        self.Btn_Rule = QtWidgets.QPushButton(GLMenu)
        self.Btn_Rule.setGeometry(QtCore.QRect(160, 290, 181, 41))
        self.Btn_Rule.setObjectName("Btn_Rule")
        self.Btn_ElUprav = QtWidgets.QPushButton(GLMenu)
        self.Btn_ElUprav.setGeometry(QtCore.QRect(160, 340, 181, 41))
        self.Btn_ElUprav.setObjectName("Btn_ElUprav")
        self.Btn_Exit = QtWidgets.QPushButton(GLMenu)
        self.Btn_Exit.setGeometry(QtCore.QRect(160, 390, 181, 41))
        self.Btn_Exit.setStyleSheet("background-color: rgb(237, 51, 59);")
        self.Btn_Exit.setCheckable(False)
        self.Btn_Exit.setChecked(False)
        self.Btn_Exit.setObjectName("Btn_Exit")

        self.retranslateUi(GLMenu)
        QtCore.QMetaObject.connectSlotsByName(GLMenu)

    def retranslateUi(self, GLMenu):
        _translate = QtCore.QCoreApplication.translate
        GLMenu.setWindowTitle(_translate("GLMenu", "Кликомания"))
        self.label.setText(_translate("GLMenu", "Кликомания"))
        self.Btn_Play.setText(_translate("GLMenu", "Играть"))
        self.Btn_Rule.setText(_translate("GLMenu", "Правила"))
        self.Btn_ElUprav.setText(_translate("GLMenu", "Элементы управления"))
        self.Btn_Exit.setText(_translate("GLMenu", "Выход"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GLMenu = QMainWindow()
    GLMenu.setFixedSize(500, 800)
    ui = Ui_GLMenu()
    ui.setupUi(GLMenu)
    GLMenu.show()
    
    def openRulePlay():
        global Rule_Play
        Rule_Play = QMainWindow()
        Rule_Play.setFixedSize(500, 800)
        ui = Ui_Rule_Play()
        ui.setupUi(Rule_Play)
        GLMenu.close()
        Rule_Play.show()

        def returnGLMenu():
            Rule_Play.close()
            GLMenu.show()
        
        ui.Btn_GLMenu.clicked.connect(returnGLMenu)

    def openElUprav():
        global Element_Uprav
        Element_Uprav = QMainWindow()
        Element_Uprav.setFixedSize(500, 800)
        ui = Ui_ElUprav()
        ui.setupUi(Element_Uprav)
        GLMenu.close()
        Element_Uprav.show()

        def returnGLMenu():
            Element_Uprav.close()
            GLMenu.show()

        ui.Btn_GLMenu.clicked.connect(returnGLMenu)
    
    def openPlay():
        global Slosnost
        Slosnost = QMainWindow()
        Slosnost.setFixedSize(500, 800)
        ui = Ui_Slosnost()
        ui.setupUi(Slosnost)
        GLMenu.close()
        Slosnost.show()

        def openPlayEasy():
            Slosnost.close()
            GLMenu.show()
            GLMenu.hide()
            def Play():
                global COLOR_COUNTS
                COLOR_COUNTS = {"red": 54, "green": 53, "blue": 53}
                BLOCK_SIZE = 50
                ROWS = 16
                COLS = 10

                class Block:
                    def __init__(self, canvas, x, y, color):
                        self.canvas = canvas
                        self.id = canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill=color)
                        self.color = color
                    
                    def delete(self):
                        self.canvas.delete(self.id)

                class Clickomania:
                    def __init__(self):
                        global lbl2
                        self.window = tk.Tk()
                        self.window.title("Кликомания")
                        self.canvas = tk.Canvas(self.window, width=COLS*BLOCK_SIZE, height=ROWS*BLOCK_SIZE)
                        self.canvas.pack()
                        self.blocks = []
                        self.score = 0
                        lbl2 = Label(self.window, text=self.score)
                        lbl2.pack(side="bottom")
                        lbl = Label(self.window, text="Score:")
                        lbl.pack(side='bottom')
                        self.create_blocks()
                        self.canvas.bind("<Button-1>", self.on_click)
                        restart_button = Button(self.window, text="Начать снова", command=lambda: self.restart_game(0))
                        restart_button.pack()
                        GLMenu_Btn = Button(self.window, text="Главное меню", command=self.GLmenu)
                        GLMenu_Btn.pack()
                        self.window.mainloop()
                    
                    def GLmenu(self):
                        self.window.destroy()
                    
                    def get_random_color(self):
                        colors = list(COLOR_COUNTS.keys())
                        counts = list(COLOR_COUNTS.values())
                        total_counts = sum(counts)
                        if total_counts == 0:
                            return None
                        rand = random.randint(1, total_counts)
                        for i in range(len(colors)):
                            count = counts[i]
                            if rand <= count:
                                COLOR_COUNTS[colors[i]] -= 1
                                return colors[i]
                            rand -= count
                        return None
                    
                    def create_blocks(self):
                        for row in range(ROWS):
                            for col in range(COLS):
                                color = self.get_random_color()
                                block = Block(self.canvas, col*BLOCK_SIZE, row*BLOCK_SIZE, color)
                                self.blocks.append(block)
                                
                    def on_click(self, event):
                        x = event.x // BLOCK_SIZE
                        y = event.y // BLOCK_SIZE
                        color = self.blocks[y*COLS + x].color
                        to_delete = [(x, y)]
                        self.check_neighbours(x, y, color, to_delete)
                        if len(to_delete) >= 2:
                            self.delete_blocks(to_delete)
                            self.fall_blocks()
                    
                    def check_neighbours(self, x, y, color, to_delete):
                        if x > 0 and (x-1, y) not in to_delete and self.blocks[y*COLS + x-1] is not None and hasattr(self.blocks[y*COLS + x-1], 'color') and self.blocks[y*COLS + x-1].color == color:
                            to_delete.append((x-1, y))
                            self.check_neighbours(x-1, y, color, to_delete)
                        if x < COLS-1 and (x+1, y) not in to_delete and self.blocks[y*COLS + x+1] is not None and hasattr(self.blocks[y*COLS + x+1], 'color') and self.blocks[y*COLS + x+1].color == color:
                            to_delete.append((x+1, y))
                            self.check_neighbours(x+1, y, color, to_delete)
                        if y > 0 and (x, y-1) not in to_delete and self.blocks[(y-1)*COLS + x] is not None and hasattr(self.blocks[(y-1)*COLS + x], 'color') and self.blocks[(y-1)*COLS + x].color == color:
                            to_delete.append((x, y-1))
                            self.check_neighbours(x, y-1, color, to_delete)
                        if y < ROWS-1 and (x, y+1) not in to_delete and self.blocks[(y+1)*COLS + x].color == color:
                            to_delete.append((x, y+1))
                            self.check_neighbours(x, y+1, color, to_delete)
                            
                    def delete_blocks(self, to_delete):
                        global lbl2
                        for x, y in to_delete:
                            self.blocks[y*COLS + x].delete()
                            self.blocks[y*COLS + x] = None
                        self.score += len(to_delete) ** 2
                        lbl2.configure(text=self.score)

                    def fall_blocks(self):
                        for col in range(COLS):
                            empty_space = 0
                            for row in range(ROWS-1, -1, -1):
                                if not self.blocks[row*COLS + col]:
                                    empty_space += 1
                                else:
                                    if empty_space > 0:
                                        self.blocks[(row+empty_space)*COLS + col] = self.blocks[row*COLS + col]
                                        self.blocks[row*COLS + col] = None
                                        self.move_block(self.blocks[(row+empty_space)*COLS + col], col, row+empty_space)
                        for col in range(COLS-1, -1, -1):
                            if all(not self.blocks[row*COLS + col] for row in range(ROWS)):
                                for c in range(col-1, -1, -1):
                                    for r in range(ROWS):
                                        if self.blocks[r*COLS + c]:
                                            self.blocks[r*COLS + c+1] = self.blocks[r*COLS + c]
                                            self.blocks[r*COLS + c] = None
                                            self.move_block(self.blocks[r*COLS + c+1], c+1, r)   
                        self.check_game_lose()
                        self.check_game_win()             
                        self.create_new_blocks()
                                        
                    def create_new_blocks(self):
                        for color, count in COLOR_COUNTS.items():
                            for i in range(count):
                                self.create_new_block(color)

                    def create_new_block(self, color):
                        col = random.randint(0, COLS-1)
                        empty_spaces = [row for row in range(ROWS) if not self.blocks[row * COLS + col]]
                        if empty_spaces:
                            row = max(empty_spaces)
                            block = Block(self.canvas, col * BLOCK_SIZE, row * BLOCK_SIZE, color)
                            self.blocks[row * COLS + col] = block
                            self.move_block(block, col, row)
                        else:
                            pass

                    def move_block(self, block, col, row):
                        x = col * BLOCK_SIZE
                        y = row * BLOCK_SIZE
                        self.canvas.coords(block.id, x, y, x + BLOCK_SIZE, y + BLOCK_SIZE)

                    def check_game_win(self):
                        if all(block is None for block in self.blocks):
                            messagebox.showinfo("Game Over", "Всё поле отчищено, вы победили!\nИгра продолжается на том же уровне сложности")
                            self.restart_game(self.score)

                    def check_game_lose(self):
                        check_block = 0
                        for row in range(ROWS):
                            for col in range(COLS):
                                block = self.blocks[row*COLS + col]
                                if block and hasattr(block, 'color'):
                                    color = block.color
                                    if col > 0 and self.blocks[row*COLS + col-1] is not None and hasattr(self.blocks[row*COLS + col-1], 'color') and self.blocks[row*COLS + col-1].color == color:
                                        check_block += 1
                                    if col < COLS-1 and self.blocks[row*COLS + col+1] is not None and hasattr(self.blocks[row*COLS + col+1], 'color') and self.blocks[row*COLS + col+1].color == color:
                                        check_block += 1
                                    if row > 0 and self.blocks[(row-1)*COLS + col] is not None and hasattr(self.blocks[(row-1)*COLS + col], 'color') and self.blocks[(row-1)*COLS + col].color == color:
                                        check_block += 1
                                    if row < ROWS-1 and self.blocks[(row+1)*COLS + col] is not None and hasattr(self.blocks[(row+1)*COLS + col], 'color') and self.blocks[(row+1)*COLS + col].color == color:
                                        check_block += 1
                        if check_block == 0 and len([block for block in self.blocks if block is not None]) > 0:
                            messagebox.showinfo("Game Over", "На поле остались блоки которые невозможно уничтожить, вы проиграли:(\nВашь счёт:" + str(self.score) + "\nИгра начентся с начала")
                            self.restart_game(0)

                    def get_block_position(self, block):
                        index = self.blocks.index(block)
                        row = index // COLS
                        col = index % COLS
                        return row, col

                    def restart_game(self, score):
                        global COLOR_COUNTS
                        COLOR_COUNTS = {"red": 54, "green": 53, "blue": 53}
                        self.canvas.delete("all")
                        self.blocks = []
                        self.score = score
                        lbl2.configure(text=self.score)
                        self.create_blocks()

                    def start(self):
                        self.window.mainloop()

                game = Clickomania()
                game.start()

            Play()
            GLMenu.show()

        def openPlayMedium():
            Slosnost.close()
            GLMenu.show()
            GLMenu.hide()
            def Play():
                global COLOR_COUNTS
                COLOR_COUNTS = {"red": 40, "green": 40, "blue": 40, "yellow": 40}
                BLOCK_SIZE = 50
                ROWS = 16
                COLS = 10

                class Block:
                    def __init__(self, canvas, x, y, color):
                        self.canvas = canvas
                        self.id = canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill=color)
                        self.color = color
                    
                    def delete(self):
                        self.canvas.delete(self.id)

                class Clickomania:
                    def __init__(self):
                        global lbl2
                        self.window = tk.Tk()
                        self.window.title("Кликомания")
                        self.canvas = tk.Canvas(self.window, width=COLS*BLOCK_SIZE, height=ROWS*BLOCK_SIZE)
                        self.canvas.pack()
                        self.blocks = []
                        self.score = 0
                        lbl2 = Label(self.window, text=self.score)
                        lbl2.pack(side="bottom")
                        lbl = Label(self.window, text="Score:")
                        lbl.pack(side='bottom')
                        self.create_blocks()
                        self.canvas.bind("<Button-1>", self.on_click)
                        restart_button = Button(self.window, text="Начать снова", command=lambda: self.restart_game(0))
                        restart_button.pack()
                        GLMenu_Btn = Button(self.window, text="Главное меню", command=self.GLmenu)
                        GLMenu_Btn.pack()
                        self.window.mainloop()
                    
                    def GLmenu(self):
                        self.window.destroy()
                    
                    def get_random_color(self):
                        colors = list(COLOR_COUNTS.keys())
                        counts = list(COLOR_COUNTS.values())
                        total_counts = sum(counts)
                        if total_counts == 0:
                            return None
                        rand = random.randint(1, total_counts)
                        for i in range(len(colors)):
                            count = counts[i]
                            if rand <= count:
                                COLOR_COUNTS[colors[i]] -= 1
                                return colors[i]
                            rand -= count
                        return None
                    
                    def create_blocks(self):
                        for row in range(ROWS):
                            for col in range(COLS):
                                color = self.get_random_color()
                                block = Block(self.canvas, col*BLOCK_SIZE, row*BLOCK_SIZE, color)
                                self.blocks.append(block)
                                
                    def on_click(self, event):
                        x = event.x // BLOCK_SIZE
                        y = event.y // BLOCK_SIZE
                        color = self.blocks[y*COLS + x].color
                        to_delete = [(x, y)]
                        self.check_neighbours(x, y, color, to_delete)
                        if len(to_delete) >= 2:
                            self.delete_blocks(to_delete)
                            self.fall_blocks()
                    
                    def check_neighbours(self, x, y, color, to_delete):
                        if x > 0 and (x-1, y) not in to_delete and self.blocks[y*COLS + x-1] is not None and hasattr(self.blocks[y*COLS + x-1], 'color') and self.blocks[y*COLS + x-1].color == color:
                            to_delete.append((x-1, y))
                            self.check_neighbours(x-1, y, color, to_delete)
                        if x < COLS-1 and (x+1, y) not in to_delete and self.blocks[y*COLS + x+1] is not None and hasattr(self.blocks[y*COLS + x+1], 'color') and self.blocks[y*COLS + x+1].color == color:
                            to_delete.append((x+1, y))
                            self.check_neighbours(x+1, y, color, to_delete)
                        if y > 0 and (x, y-1) not in to_delete and self.blocks[(y-1)*COLS + x] is not None and hasattr(self.blocks[(y-1)*COLS + x], 'color') and self.blocks[(y-1)*COLS + x].color == color:
                            to_delete.append((x, y-1))
                            self.check_neighbours(x, y-1, color, to_delete)
                        if y < ROWS-1 and (x, y+1) not in to_delete and self.blocks[(y+1)*COLS + x].color == color:
                            to_delete.append((x, y+1))
                            self.check_neighbours(x, y+1, color, to_delete)
                            
                    def delete_blocks(self, to_delete):
                        global lbl2
                        for x, y in to_delete:
                            self.blocks[y*COLS + x].delete()
                            self.blocks[y*COLS + x] = None
                        self.score += len(to_delete) ** 2
                        lbl2.configure(text=self.score)

                    def fall_blocks(self):
                        for col in range(COLS):
                            empty_space = 0
                            for row in range(ROWS-1, -1, -1):
                                if not self.blocks[row*COLS + col]:
                                    empty_space += 1
                                else:
                                    if empty_space > 0:
                                        self.blocks[(row+empty_space)*COLS + col] = self.blocks[row*COLS + col]
                                        self.blocks[row*COLS + col] = None
                                        self.move_block(self.blocks[(row+empty_space)*COLS + col], col, row+empty_space)
                        for col in range(COLS-1, -1, -1):
                            if all(not self.blocks[row*COLS + col] for row in range(ROWS)):
                                for c in range(col-1, -1, -1):
                                    for r in range(ROWS):
                                        if self.blocks[r*COLS + c]:
                                            self.blocks[r*COLS + c+1] = self.blocks[r*COLS + c]
                                            self.blocks[r*COLS + c] = None
                                            self.move_block(self.blocks[r*COLS + c+1], c+1, r)   
                        self.check_game_lose()
                        self.check_game_win()
                        self.create_new_blocks()
                                        
                    def create_new_blocks(self):
                        for color, count in COLOR_COUNTS.items():
                            for i in range(count):
                                self.create_new_block(color)

                    def create_new_block(self, color):
                        col = random.randint(0, COLS-1)
                        empty_spaces = [row for row in range(ROWS) if not self.blocks[row * COLS + col]]
                        if empty_spaces:
                            row = max(empty_spaces)
                            block = Block(self.canvas, col * BLOCK_SIZE, row * BLOCK_SIZE, color)
                            self.blocks[row * COLS + col] = block
                            self.move_block(block, col, row)
                        else:
                            pass

                    def move_block(self, block, col, row):
                        x = col * BLOCK_SIZE
                        y = row * BLOCK_SIZE
                        self.canvas.coords(block.id, x, y, x + BLOCK_SIZE, y + BLOCK_SIZE)

                    def check_game_win(self):
                        if all(block is None for block in self.blocks):
                            messagebox.showinfo("Game Over", "Всё поле отчищено, вы победили!\nИгра продолжается на том же уровне сложности")
                            self.restart_game(self.score)

                    def check_game_lose(self):
                        check_block = 0
                        for row in range(ROWS):
                            for col in range(COLS):
                                block = self.blocks[row*COLS + col]
                                if block and hasattr(block, 'color'):
                                    color = block.color
                                    if col > 0 and self.blocks[row*COLS + col-1] is not None and hasattr(self.blocks[row*COLS + col-1], 'color') and self.blocks[row*COLS + col-1].color == color:
                                        check_block += 1
                                    if col < COLS-1 and self.blocks[row*COLS + col+1] is not None and hasattr(self.blocks[row*COLS + col+1], 'color') and self.blocks[row*COLS + col+1].color == color:
                                        check_block += 1
                                    if row > 0 and self.blocks[(row-1)*COLS + col] is not None and hasattr(self.blocks[(row-1)*COLS + col], 'color') and self.blocks[(row-1)*COLS + col].color == color:
                                        check_block += 1
                                    if row < ROWS-1 and self.blocks[(row+1)*COLS + col] is not None and hasattr(self.blocks[(row+1)*COLS + col], 'color') and self.blocks[(row+1)*COLS + col].color == color:
                                        check_block += 1
                        if check_block == 0:
                            messagebox.showinfo("Game Over", "На поле остались блоки которые невозможно уничтожить, вы проиграли:(\nВашь счёт:" + str(self.score) + "\nИгра начентся с начала")
                            self.restart_game(0)

                    def get_block_position(self, block):
                        index = self.blocks.index(block)
                        row = index // COLS
                        col = index % COLS
                        return row, col

                    def restart_game(self, score):
                        global COLOR_COUNTS
                        COLOR_COUNTS = {"red": 40, "green": 40, "blue": 40, "yellow": 40}
                        self.canvas.delete("all")
                        self.blocks = []
                        self.score = score
                        lbl2.configure(text=self.score)
                        self.create_blocks()

                    def start(self):
                        self.window.mainloop()

                game = Clickomania()
                game.start()

            Play()
            GLMenu.show()

        def openPlayHard():
            Slosnost.close()
            GLMenu.show()
            GLMenu.hide()
            def Play():
                global COLOR_COUNTS
                COLOR_COUNTS = {"red": 32, "green":32 , "blue": 32, "yellow": 32, "purple": 32}
                BLOCK_SIZE = 50
                ROWS = 16
                COLS = 10

                class Block:
                    def __init__(self, canvas, x, y, color):
                        self.canvas = canvas
                        self.id = canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill=color)
                        self.color = color
                    
                    def delete(self):
                        self.canvas.delete(self.id)

                class Clickomania:
                    def __init__(self):
                        global lbl2
                        self.window = tk.Tk()
                        self.window.title("Кликомания")
                        self.canvas = tk.Canvas(self.window, width=COLS*BLOCK_SIZE, height=ROWS*BLOCK_SIZE)
                        self.canvas.pack()
                        self.blocks = []
                        self.score = 0
                        lbl2 = Label(self.window, text=self.score)
                        lbl2.pack(side="bottom")
                        lbl = Label(self.window, text="Score:")
                        lbl.pack(side='bottom')
                        self.create_blocks()
                        self.canvas.bind("<Button-1>", self.on_click)
                        restart_button = Button(self.window, text="Начать снова", command=lambda: self.restart_game(0))
                        restart_button.pack()
                        GLMenu_Btn = Button(self.window, text="Главное меню", command=self.GLmenu)
                        GLMenu_Btn.pack()
                        self.window.mainloop()
                    
                    def GLmenu(self):
                        self.window.destroy()
                    
                    def get_random_color(self):
                        colors = list(COLOR_COUNTS.keys())
                        counts = list(COLOR_COUNTS.values())
                        total_counts = sum(counts)
                        if total_counts == 0:
                            return None
                        rand = random.randint(1, total_counts)
                        for i in range(len(colors)):
                            count = counts[i]
                            if rand <= count:
                                COLOR_COUNTS[colors[i]] -= 1
                                return colors[i]
                            rand -= count
                        return None
                    
                    def create_blocks(self):
                        for row in range(ROWS):
                            for col in range(COLS):
                                color = self.get_random_color()
                                block = Block(self.canvas, col*BLOCK_SIZE, row*BLOCK_SIZE, color)
                                self.blocks.append(block)
                                
                    def on_click(self, event):
                        x = event.x // BLOCK_SIZE
                        y = event.y // BLOCK_SIZE
                        color = self.blocks[y*COLS + x].color
                        to_delete = [(x, y)]
                        self.check_neighbours(x, y, color, to_delete)
                        if len(to_delete) >= 2:
                            self.delete_blocks(to_delete)
                            self.fall_blocks()
                    
                    def check_neighbours(self, x, y, color, to_delete):
                        if x > 0 and (x-1, y) not in to_delete and self.blocks[y*COLS + x-1] is not None and hasattr(self.blocks[y*COLS + x-1], 'color') and self.blocks[y*COLS + x-1].color == color:
                            to_delete.append((x-1, y))
                            self.check_neighbours(x-1, y, color, to_delete)
                        if x < COLS-1 and (x+1, y) not in to_delete and self.blocks[y*COLS + x+1] is not None and hasattr(self.blocks[y*COLS + x+1], 'color') and self.blocks[y*COLS + x+1].color == color:
                            to_delete.append((x+1, y))
                            self.check_neighbours(x+1, y, color, to_delete)
                        if y > 0 and (x, y-1) not in to_delete and self.blocks[(y-1)*COLS + x] is not None and hasattr(self.blocks[(y-1)*COLS + x], 'color') and self.blocks[(y-1)*COLS + x].color == color:
                            to_delete.append((x, y-1))
                            self.check_neighbours(x, y-1, color, to_delete)
                        if y < ROWS-1 and (x, y+1) not in to_delete and self.blocks[(y+1)*COLS + x].color == color:
                            to_delete.append((x, y+1))
                            self.check_neighbours(x, y+1, color, to_delete)
                            
                    def delete_blocks(self, to_delete):
                        global lbl2
                        for x, y in to_delete:
                            self.blocks[y*COLS + x].delete()
                            self.blocks[y*COLS + x] = None
                        self.score += len(to_delete) ** 2
                        lbl2.configure(text=self.score)

                    def fall_blocks(self):
                        for col in range(COLS):
                            empty_space = 0
                            for row in range(ROWS-1, -1, -1):
                                if not self.blocks[row*COLS + col]:
                                    empty_space += 1
                                else:
                                    if empty_space > 0:
                                        self.blocks[(row+empty_space)*COLS + col] = self.blocks[row*COLS + col]
                                        self.blocks[row*COLS + col] = None
                                        self.move_block(self.blocks[(row+empty_space)*COLS + col], col, row+empty_space)
                        for col in range(COLS-1, -1, -1):
                            if all(not self.blocks[row*COLS + col] for row in range(ROWS)):
                                for c in range(col-1, -1, -1):
                                    for r in range(ROWS):
                                        if self.blocks[r*COLS + c]:
                                            self.blocks[r*COLS + c+1] = self.blocks[r*COLS + c]
                                            self.blocks[r*COLS + c] = None
                                            self.move_block(self.blocks[r*COLS + c+1], c+1, r)   
                        self.check_game_lose()
                        self.check_game_win()
                        self.create_new_blocks()
                                        
                    def create_new_blocks(self):
                        for color, count in COLOR_COUNTS.items():
                            for i in range(count):
                                self.create_new_block(color)

                    def create_new_block(self, color):
                        col = random.randint(0, COLS-1)
                        empty_spaces = [row for row in range(ROWS) if not self.blocks[row * COLS + col]]
                        if empty_spaces:
                            row = max(empty_spaces)
                            block = Block(self.canvas, col * BLOCK_SIZE, row * BLOCK_SIZE, color)
                            self.blocks[row * COLS + col] = block
                            self.move_block(block, col, row)
                        else:
                            pass

                    def move_block(self, block, col, row):
                        x = col * BLOCK_SIZE
                        y = row * BLOCK_SIZE
                        self.canvas.coords(block.id, x, y, x + BLOCK_SIZE, y + BLOCK_SIZE)

                    def check_game_win(self):
                        if all(block is None for block in self.blocks):
                            messagebox.showinfo("Game Over", "Всё поле отчищено, вы победили!\nИгра продолжается на том же уровне сложности")
                            self.restart_game(self.score)

                    def check_game_lose(self):
                        check_block = 0
                        for row in range(ROWS):
                            for col in range(COLS):
                                block = self.blocks[row*COLS + col]
                                if block and hasattr(block, 'color'):
                                    color = block.color
                                    if col > 0 and self.blocks[row*COLS + col-1] is not None and hasattr(self.blocks[row*COLS + col-1], 'color') and self.blocks[row*COLS + col-1].color == color:
                                        check_block += 1
                                    if col < COLS-1 and self.blocks[row*COLS + col+1] is not None and hasattr(self.blocks[row*COLS + col+1], 'color') and self.blocks[row*COLS + col+1].color == color:
                                        check_block += 1
                                    if row > 0 and self.blocks[(row-1)*COLS + col] is not None and hasattr(self.blocks[(row-1)*COLS + col], 'color') and self.blocks[(row-1)*COLS + col].color == color:
                                        check_block += 1
                                    if row < ROWS-1 and self.blocks[(row+1)*COLS + col] is not None and hasattr(self.blocks[(row+1)*COLS + col], 'color') and self.blocks[(row+1)*COLS + col].color == color:
                                        check_block += 1
                        if check_block == 0:
                            messagebox.showinfo("Game Over", "На поле остались блоки которые невозможно уничтожить, вы проиграли:(\nВашь счёт:" + str(self.score) + "\nИгра начентся с начала")
                            self.restart_game(0)

                    def get_block_position(self, block):
                        index = self.blocks.index(block)
                        row = index // COLS
                        col = index % COLS
                        return row, col

                    def restart_game(self, score):
                        global COLOR_COUNTS
                        COLOR_COUNTS = {"red": 32, "green":32 , "blue": 32, "yellow": 32, "purple": 32}
                        self.canvas.delete("all")
                        self.blocks = []
                        self.score = score
                        lbl2.configure(text=self.score)
                        self.create_blocks()

                    def start(self):
                        self.window.mainloop()

                game = Clickomania()
                game.start()

            Play()
            GLMenu.show()

        def returnGLMenu():
            Slosnost.close()
            GLMenu.show()
        
        ui.Btn_GLMenu.clicked.connect(returnGLMenu)
        ui.Btn_Easy.clicked.connect(openPlayEasy)
        ui.Btn_Hard.clicked.connect(openPlayHard)
        ui.Btn_Medium.clicked.connect(openPlayMedium)

    ui.Btn_Play.clicked.connect(openPlay)
    ui.Btn_Rule.clicked.connect(openRulePlay)
    ui.Btn_Exit.clicked.connect(GLMenu.close)
    ui.Btn_ElUprav.clicked.connect(openElUprav)

    sys.exit(app.exec_())