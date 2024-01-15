# Component - Car Dashboard
class CarDashboard:
    def display(self):
        return "Basic Car Dashboard"

# Decorator - Abstract class for additional features
class CarDecorator(CarDashboard):
    def __init__(self, dashboard):
        self.dashboard = dashboard

    def display(self):
        return self.dashboard.display()

# Concrete Decorator - GPS
class GPSDecorator(CarDecorator):
    def display(self):
        return f"{self.dashboard.display()} with GPS"

# Concrete Decorator - Music Player
class MusicPlayerDecorator(CarDecorator):
    def display(self):
        return f"{self.dashboard.display()} with Music Player"

# Concrete Decorator - Climate Control
class ClimateControlDecorator(CarDecorator):
    def display(self):
        return f"{self.dashboard.display()} with Climate Control"

# Example Usage
basic_dashboard = CarDashboard()
dashboard_with_gps = GPSDecorator(basic_dashboard)
dashboard_with_music_player = MusicPlayerDecorator(dashboard_with_gps)
dashboard_with_all_features = ClimateControlDecorator(dashboard_with_music_player)

print("Basic Dashboard:", basic_dashboard.display())
print("Dashboard with GPS:", dashboard_with_gps.display())
print("Dashboard with Music Player:", dashboard_with_music_player.display())
print("Dashboard with All Features:", dashboard_with_all_features.display())
