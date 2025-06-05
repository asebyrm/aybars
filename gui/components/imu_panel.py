
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtCore import QTimer

from gui.components.rocket_3d import Rocket3D
from gui.components.artificial_horizon import ArtificialHorizon
from gui.components.altitude_plot import AltitudePlot
from gui.components.map_plot import MapPlot
from gui.components.compass_plot import CompassPlot
from gui.components.polar_deviation_plot import PolarDeviationPlot

class IMUPanel(QWidget):
    def __init__(self, telemetry_manager, parent=None):
        super().__init__(parent)

        self.telemetry = telemetry_manager
        self.parent_window = parent
        layout = QGridLayout()

        self.rocket_3d = Rocket3D()
        self.horizon = ArtificialHorizon()
        self.altitude = AltitudePlot(telemetry=self.telemetry)
        self.map_plot = MapPlot()
        self.compass_plot = CompassPlot()
        self.polar_plot = PolarDeviationPlot()

        self.rocket_3d.setMinimumSize(300, 300)
        self.horizon.setMinimumSize(300, 300)
        self.map_plot.setMinimumSize(300, 300)
        self.compass_plot.setMinimumSize(300, 300)
        self.polar_plot.setMinimumSize(300, 300)

        layout.addWidget(self.rocket_3d, 0, 0)
        layout.addWidget(self.horizon, 0, 1)
        layout.addWidget(self.altitude, 0, 2)
        layout.addWidget(self.map_plot, 1, 0)
        layout.addWidget(self.compass_plot, 1, 1)
        layout.addWidget(self.polar_plot, 1, 2)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_all)
        self.timer.start(300)

    def set_manager(self, new_manager):
        self.telemetry = new_manager

    def update_all(self):
        try:
            pitch, roll, yaw = self.telemetry.get_orientation()
            altitude = self.telemetry.get_altitude()
            lat, lon = self.telemetry.get_position()
            heading = self.telemetry.get_heading()
            deviation = self.telemetry.get_deviation()

            self.rocket_3d.update_orientation(pitch, roll, yaw)
            self.horizon.update_attitude(pitch, roll)
            self.altitude.update_altitude(altitude)
            self.map_plot.update_position(lat, lon)
            self.compass_plot.update_heading(heading)
            self.polar_plot.update_value(deviation)

        except Exception as e:
            print(f"[HATA - IMU update_all] {e}")
