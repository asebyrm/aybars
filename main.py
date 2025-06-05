from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from core.telemetry_manager import TelemetryManager
from data.simulator import SimulatedTelemetry
from services.serial_service import SerialTelemetry
from utils.config_loader import load_config
import sys

cfg = load_config()
mode = cfg.get('mode', 'SIMULATION')

if mode == 'SIMULATION':
    source = SimulatedTelemetry()
else:
    source = SerialTelemetry(cfg['serial_port'], cfg['baud_rate'])

app = QApplication(sys.argv)
tm = TelemetryManager(source)
window = MainWindow(tm)
window.show()
sys.exit(app.exec_())
