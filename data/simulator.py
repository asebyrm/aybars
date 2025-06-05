import random

class SimulatedTelemetry:
    def __init__(self):
        self.pitch = 0
        self.roll = 0
        self.yaw = 0
        self.altitude = 100.0
        self.lat = 41.0
        self.lon = 29.0
        self.heading = 0.0
        self.deviation = 0.0

    def get_data(self):
        self.pitch = random.uniform(-30, 30)
        self.roll = random.uniform(-60, 60)
        self.yaw = random.uniform(0, 360)
        self.altitude += random.uniform(-0.5, 0.5)
        self.lat += random.uniform(-0.0001, 0.0001)
        self.lon += random.uniform(-0.0001, 0.0001)
        self.heading = (self.heading + random.uniform(-5, 5)) % 360
        self.deviation = random.uniform(0, 30)

        return {
            "pitch": self.pitch,
            "roll": self.roll,
            "yaw": self.yaw,
            "altitude": self.altitude,
            "lat": self.lat,
            "lon": self.lon,
            "heading": self.heading,
            "deviation": self.deviation
        }
