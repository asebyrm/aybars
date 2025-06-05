
from PyQt5.QtWidgets import QLabel

class MapPlot(QLabel):
    def __init__(self):
        super().__init__("3D MAP PLOT")
    def update_position(self, lat, lon):
        self.setText(f"Lat: {lat:.2f}, Lon: {lon:.2f}")
