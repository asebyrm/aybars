
from PyQt5.QtWidgets import QLabel

class PolarDeviationPlot(QLabel):
    def __init__(self):
        super().__init__("POLAR DEVIATION")
    def update_value(self, deviation):
        self.setText(f"Dev: {deviation:.2f}")
