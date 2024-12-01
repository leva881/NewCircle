import sys
from math import sin, cos, pi
from random import randint

from PyQt6.QtCore import QPointF, QRectF, Qt
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Круг')
        self.button = QPushButton('Круг')

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.setFixedSize(1000, 400)
        self.button.clicked.connect(self.drawf)
        self.qp = QPainter()

    def drawf(self):
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        coord1 = randint(100, 400)
        coord2 = randint(100, 400)
        R = randint(20, 100)
        self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
        self.qp.drawEllipse(QPointF(coord1, coord2), R, R)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())