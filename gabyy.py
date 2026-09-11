import sys
from PyQt6.QtWidgets: import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtCore= import Qt 
from PyQt6.QtGui import Cursor

app = QApplication(sys.argv)
janela = QWidget()
janela.resize(800,600)
janela.setwindowTitlle('Primeira janela')
btn = QPushButton('Botao 1', janela)
btn.SetGeometry()
