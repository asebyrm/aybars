class TelemetryManager:
    def __init__(self, source):
        self.source = source
        self.latest = self.source.get_data()

    def get_orientation(self):
        self.latest = self.source.get_data()
        return self.latest["pitch"], self.latest["roll"], self.latest["yaw"]

    def get_altitude(self):
        return self.latest["altitude"]

    def get_position(self):
        return self.latest.get("lat", 0.0), self.latest.get("lon", 0.0)

    def get_heading(self):
        return self.latest.get("heading", 0.0)

    def get_deviation(self):
        return self.latest.get("deviation", 0.0)
