from pyqtgraph import PlotWidget
from PyQt5.QtCore import QTimer
import pyqtgraph as pg

class AltitudePlot(PlotWidget):
    def __init__(self, telemetry):  # <-- burada telemetry parametresi alınmalı
        super().__init__()
        self.telemetry = telemetry

        self.setTitle('Altitude')
        self.setLabel('left', 'Meters')
        self.setLabel('bottom', 'Time')

        self.altitude_data = []
        self.time_data = []
        self.ptr = 0
        self.plot_line = self.plot()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(500)

    def update_plot(self):
        altitude = self.telemetry.get_altitude()
        self.update_altitude(altitude)

    def update_altitude(self, altitude):
        self.altitude_data.append(altitude)
        self.time_data.append(self.ptr)
        self.ptr += 1
        if len(self.altitude_data) > 200:
            self.altitude_data = self.altitude_data[-200:]
            self.time_data = self.time_data[-200:]
        self.plot_line.setData(self.time_data, self.altitude_data)
