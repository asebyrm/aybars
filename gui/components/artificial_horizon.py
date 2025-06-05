from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class ArtificialHorizon(QWidget):
    def __init__(self):
        super().__init__()
        self.pitch = 0
        self.roll = 0

    def update_attitude(self, pitch, roll):
        self.pitch = pitch
        self.roll = roll
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        center = rect.center()
        painter.translate(center)
        painter.rotate(-self.roll)
        painter.setPen(QPen(Qt.blue, 2))
        painter.drawLine(-100, 0, 100, 0)
        painter.setPen(QPen(Qt.green, 1))
        painter.drawText(-30, -20, f'Pitch: {self.pitch:.1f}')
        painter.drawText(-30, 20, f'Roll: {self.roll:.1f}')
