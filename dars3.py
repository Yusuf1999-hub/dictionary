# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

# class Win(QWidget):
#     def __init__(self) -> None:
#         super().__init__()

# class MainWindow(QMainWindow):
#     def __init__(self) -> None:
#         super().__init__()

#         self.win1 = Win()

#         btn = QPushButton("NEW", self)
#         btn.clicked.connect(self.show_window)

#     def show_window(self):
#         self.win1.show()

# app = QApplication([])
# win = MainWindow()
# win.show()
# app.exec_()



from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QListWidget

class Add(QWidget):
    def __init__(self):
        super().__init__()

        self.v_lang_lay = QVBoxLayout()
        self.h_top_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.eng_edit = QLineEdit()
        self.eng_edit.setPlaceholderText("Eng...")

        self.uz_edit = QLineEdit()
        self.uz_edit.setPlaceholderText("Uz...")

        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.send_method)

        self.approval_label = QLabel("")

        self.Menu_btn = QPushButton("Menu")
        self.Menu_btn.clicked.connect(self.close_add_win)

        self.v_lang_lay.addWidget(self.eng_edit)
        self.v_lang_lay.addWidget(self.uz_edit)

        self.h_top_lay.addLayout(self.v_lang_lay)
        self.h_top_lay.addWidget(self.send_btn)

        self.v_main_lay.addLayout(self.h_top_lay)
        self.v_main_lay.addWidget(self.approval_label)
        self.v_main_lay.addWidget(self.Menu_btn)

        self.setLayout(self.v_main_lay)

    def send_method(self):
        pass

    def close_add_win(self):
        self.eng_edit.clear()
        self.uz_edit.clear()
        self.close()

class List(QWidget):
    def __init__(self):
        super().__init__()

        self.h_lang_lay = QHBoxLayout()
        self.h_lstWidg_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.eng_label = QLabel("English")
        self.uz_label = QLabel("Uzbek")

        self.h_lang_lay.addWidget(self.eng_label)
        self.h_lang_lay.addWidget(self.uz_label)

        self.eng_list = QListWidget()
        self.uz_list = QListWidget()

        self.h_lstWidg_lay.addWidget(self.eng_list)
        self.h_lstWidg_lay.addWidget(self.uz_list)

        self.Menu_btn = QPushButton("Menu")

        self.v_main_lay.addLayout(self.h_lang_lay)
        self.v_main_lay.addLayout(self.h_lstWidg_lay)
        self.v_main_lay.addWidget(self.Menu_btn)

        self.eng_list.addItem("CAT")
        self.eng_list.addItem("CAT")
        self.eng_list.addItem("CAT")
        self.eng_list.addItem("CAT")
        self.eng_list.addItem("CAT")
        self.setLayout(self.v_main_lay)

    

class Search(QWidget):
    def __init__(self):
        super().__init__()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350,380)

        self.add_obj = Add()
        self.search_obj = Search()
        self.lst_obj = List()

        self.add_btn = QPushButton("ADD",self)
        self.add_btn.setGeometry(125, 50, 100, 75)
        self.add_btn.clicked.connect(self.add_win)

        self.search_btn = QPushButton("SEARCH",self)
        self.search_btn.setGeometry(125, 125, 100, 75)
        self.search_btn.clicked.connect(self.search_win)

        self.lst_btn = QPushButton("LIST",self)
        self.lst_btn.setGeometry(125, 200, 100, 75)
        self.lst_btn.clicked.connect(self.lst_win)


        self.exit_btn = QPushButton("EXIT",self)
        self.exit_btn.setGeometry(125, 275, 100, 75)
        self.exit_btn.clicked.connect(self.close)

    def add_win(self):
        self.add_obj.show()

    def lst_win(self):
        self.lst_obj.show()

    def search_win(self):
        self.search_obj.show()




app = QApplication([])
win = MainWindow()
win.show()
app.exec_()













