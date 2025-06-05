from PyQt5.QtWidgets import QWidget, QFormLayout, QComboBox, QSpinBox, QPushButton
from PyQt5.QtSerialPort import QSerialPortInfo
from utils.config_loader import load_config, save_config

class SettingsPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cfg = load_config()
        self.parent_window = parent
        layout = QFormLayout()

        # Mod seçimi
        self.mode_box = QComboBox()
        self.mode_box.addItems(['SIMULATION', 'LIVE'])
        self.mode_box.setCurrentText(self.cfg['mode'])

        # Port seçimi
        self.port_box = QComboBox()
        self.available_ports = [port.portName() for port in QSerialPortInfo.availablePorts()]
        self.port_box.addItems(self.available_ports)
        if self.cfg['serial_port'] in self.available_ports:
            self.port_box.setCurrentText(self.cfg['serial_port'])

        # Baudrate seçimi
        self.baud_box = QComboBox()
        baud_rates = ['9600', '38400', '57600', '115200']
        self.baud_box.addItems(baud_rates)
        self.baud_box.setCurrentText(str(self.cfg['baud_rate']))

        # Refresh rate (ms)
        self.refresh_input = QSpinBox()
        self.refresh_input.setRange(100, 5000)
        self.refresh_input.setValue(self.cfg['refresh_rate_ms'])

        # Kaydet ve Uygula butonu
        self.save_apply_button = QPushButton('Kaydet ve Uygula')
        self.save_apply_button.clicked.connect(self.save_and_apply)

        # Arayüz yerleşimi
        layout.addRow('Mod:', self.mode_box)
        layout.addRow('Port:', self.port_box)
        layout.addRow('Baudrate:', self.baud_box)
        layout.addRow('Güncelleme (ms):', self.refresh_input)
        layout.addRow(self.save_apply_button)

        self.setLayout(layout)

    def save_and_apply(self):
        new_cfg = {
            'mode': self.mode_box.currentText(),
            'serial_port': self.port_box.currentText(),
            'baud_rate': int(self.baud_box.currentText()),
            'refresh_rate_ms': self.refresh_input.value(),
            'log_enabled': True
        }
        save_config(new_cfg)

        if self.parent_window:
            self.parent_window.apply_settings()
