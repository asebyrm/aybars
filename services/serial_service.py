import serial

class SerialTelemetry:
    def __init__(self, port="/dev/tty.usbserial-A50285BI", baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            print(f"{port} portu açıldı.")
        except Exception as e:
            print(f"HATA: {e}")

        # Tüm verileri burada saklayacağız
        self.data = {
            'pitch': 0.0,
            'roll': 0.0,
            'yaw': 0.0,
            'altitude': 0.0,
            'lat': 0.0,
            'lon': 0.0,
            'heading': 0.0,
            'deviation': 0.0
        }

    def get_data(self):
        try:
            line = self.ser.readline().decode(errors='ignore').strip()
            if not line:
                return self.data  # önceki veriyi döndür

            if line.startswith("EULER:"):
                try:
                    yaw, roll, pitch = map(float, line[6:].split(','))
                    self.data.update({
                        'yaw': yaw,
                        'roll': roll,
                        'pitch': pitch
                    })
                except:
                    print("⛔ Hatalı EULER satırı:", line)

            elif line.startswith("ALT:"):
                try:
                    alt = float(line[4:])
                    self.data['altitude'] = alt
                except:
                    print("⛔ Hatalı ALT satırı:", line)

            elif line.startswith("POS:"):
                try:
                    lat, lon = map(float, line[4:].split(','))
                    self.data['lat'] = lat
                    self.data['lon'] = lon
                except:
                    print("⛔ Hatalı POS satırı:", line)

            elif line.startswith("DEV:"):
                try:
                    dev = float(line[4:])
                    self.data['deviation'] = dev
                except:
                    print("⛔ Hatalı DEV satırı:", line)

            elif line.startswith("HEAD:"):
                try:
                    head = float(line[5:])
                    self.data['heading'] = head
                except:
                    print("⛔ Hatalı HEAD satırı:", line)

        except Exception as e:
            print("❗ UART hata:", e)

        return self.data

    def close(self):
        self.ser.close()
