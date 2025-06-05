from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTabWidget, QMessageBox
from gui.components.imu_panel import IMUPanel
from gui.components.settings_panel import SettingsPanel
from utils.config_loader import load_config
from services.serial_service import SerialTelemetry
from data.simulator import SimulatedTelemetry
from core.telemetry_manager import TelemetryManager

class MainWindow(QMainWindow):
    def __init__(self, telemetry_manager):
        super().__init__()
        self.setWindowTitle('Aybars - IMU Viewer')

        self.tabs = QTabWidget()

        # IMU sekmesi
        self.imu_tab = QWidget()
        self.imu_layout = QVBoxLayout()
        self.imu_panel = IMUPanel(telemetry_manager, parent=self)
        self.imu_layout.addWidget(self.imu_panel)
        self.imu_tab.setLayout(self.imu_layout)

        # Ayarlar sekmesi
        self.settings_tab = QWidget()
        self.settings_layout = QVBoxLayout()
        self.settings_panel = SettingsPanel(parent=self)
        self.settings_layout.addWidget(self.settings_panel)
        self.settings_tab.setLayout(self.settings_layout)

        self.tabs.addTab(self.imu_tab, 'IMU')
        self.tabs.addTab(self.settings_tab, 'Ayarlar')

        self.setCentralWidget(self.tabs)

    def apply_settings(self):
        cfg = load_config()
        try:
            if cfg["mode"] == "LIVE":
                telemetry = SerialTelemetry(cfg["serial_port"], cfg["baud_rate"])
            else:
                telemetry = SimulatedTelemetry()

            self.imu_panel.set_manager(TelemetryManager(telemetry))
            print("✅ Yeni ayarlar uygulandı.")
        except Exception as e:
            QMessageBox.critical(self, "Port Hatası", f"Port açılamadı:\n{e}")
            self.settings_panel.mode_box.setCurrentText("SIMULATION")
