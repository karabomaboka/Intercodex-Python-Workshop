# Component Interface - Car Dashboard
class CarDashboard:
    def show(self):
        pass

# Concrete Component - BasicCarDashboard
class BasicCarDashboard(CarDashboard):
    def show(self):
        return "Basic Car Dashboard"

# Decorator - CarFeature
class CarFeature(CarDashboard):
    def __init__(self, dashboard):
        self.dashboard = dashboard

    def show(self):
        return self.dashboard.show()

# Concrete Decorator - GPS
class GPSFeature(CarFeature):
    def show(self):
        return f"{super().show()} with GPS"

# Concrete Decorator - MusicPlayer
class MusicPlayerFeature(CarFeature):
    def show(self):
        return f"{super().show()} with Music Player"

# Concrete Decorator - ClimateControl
class ClimateControlFeature(CarFeature):
    def show(self):
        return f"{super().show()} with Climate Control"

# Example Usage
basic_dashboard = BasicCarDashboard()

# Add features dynamically
dashboard_with_gps = GPSFeature(basic_dashboard)
dashboard_with_music_player = MusicPlayerFeature(dashboard_with_gps)
customized_dashboard = ClimateControlFeature(dashboard_with_music_player)

# Show the final dashboard
print(customized_dashboard.show())
