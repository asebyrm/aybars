
from PyQt5.QtWidgets import QLabel

class CompassPlot(QLabel):
    def __init__(self):
        super().__init__("COMPASS")
    def update_heading(self, heading):
        self.setText(f"Heading: {heading:.2f}°")
