# Component interface
class Dashboard:
    def show(self):
        pass

# Concrete component
class BasicDashboard(Dashboard):
    def show(self):
        print("Basic Dashboard")

# Decorator base class
class DashboardDecorator(Dashboard):
    def __init__(self, dashboard):
        self.dashboard = dashboard

    def show(self):
        self.dashboard.show()

# Concrete decorators
class GPSDecorator(DashboardDecorator):
    def show(self):
        super().show()
        print("GPS added")

class MusicPlayerDecorator(DashboardDecorator):
    def show(self):
        super().show()
        print("Music Player added")

class ClimateControlDecorator(DashboardDecorator):
    def show(self):
        super().show()
        print("Climate Control added")

# Usage example
dashboard = BasicDashboard()
dashboard = GPSDecorator(dashboard)
dashboard = MusicPlayerDecorator(dashboard)
dashboard = ClimateControlDecorator(dashboard)

dashboard.show()