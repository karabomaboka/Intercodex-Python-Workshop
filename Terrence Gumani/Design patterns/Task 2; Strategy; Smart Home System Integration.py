from abc import ABC, abstractmethod

# Define a common interface for all smart devices
class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Concrete strategy for Smart Lights
class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart Light is turned on")

    def turn_off(self):
        print("Smart Light is turned off")

# Concrete strategy for Smart Thermostats
class SmartThermostat(SmartDevice):
    def turn_on(self):
        print("Smart Thermostat is heating")

    def turn_off(self):
        print("Smart Thermostat is turned off")

# Concrete strategy for Smart Locks
class SmartLock(SmartDevice):
    def turn_on(self):
        print("Smart Lock is locked")

    def turn_off(self):
        print("Smart Lock is unlocked")

# Context - Smart Home System
class SmartHomeSystem:
    def __init__(self, smart_device):
        self.smart_device = smart_device

    def operate_device(self):
        self.smart_device.turn_on()

# Example Usage
smart_light = SmartLight()
smart_thermostat = SmartThermostat()
smart_lock = SmartLock()

smart_home_system_light = SmartHomeSystem(smart_light)
smart_home_system_thermostat = SmartHomeSystem(smart_thermostat)
smart_home_system_lock = SmartHomeSystem(smart_lock)

smart_home_system_light.operate_device()
smart_home_system_thermostat.operate_device()
smart_home_system_lock.operate_device()
