# Third-party device interfaces
class SmartLight:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class SmartThermostat:
    def set_temperature(self, temperature):
        pass

class SmartLock:
    def lock(self):
        pass

    def unlock(self):
        pass

# Unified control interface
class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def set_temperature(self, temperature):
        pass

    def lock(self):
        pass

    def unlock(self):
        pass

# Adapters for each device
class SmartLightAdapter(SmartDevice):
    def __init__(self, smart_light):
        self.smart_light = smart_light

    def turn_on(self):
        self.smart_light.turn_on()

    def turn_off(self):
        self.smart_light.turn_off()

class SmartThermostatAdapter(SmartDevice):
    def __init__(self, smart_thermostat):
        self.smart_thermostat = smart_thermostat

    def set_temperature(self, temperature):
        self.smart_thermostat.set_temperature(temperature)

class SmartLockAdapter(SmartDevice):
    def __init__(self, smart_lock):
        self.smart_lock = smart_lock

    def lock(self):
        self.smart_lock.lock()

    def unlock(self):
        self.smart_lock.unlock()

# Smart home system
class SmartHomeSystem:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def turn_on_all_devices(self):
        for device in self.devices:
            device.turn_on()

    def turn_off_all_devices(self):
        for device in self.devices:
            device.turn_off()

    # Other methods for controlling devices

# Usage example
smart_light = SmartLight()
smart_light_adapter = SmartLightAdapter(smart_light)

smart_thermostat = SmartThermostat()
smart_thermostat_adapter = SmartThermostatAdapter(smart_thermostat)

smart_lock = SmartLock()
smart_lock_adapter = SmartLockAdapter(smart_lock)

smart_home_system = SmartHomeSystem()
smart_home_system.add_device(smart_light_adapter)
smart_home_system.add_device(smart_thermostat_adapter)
smart_home_system.add_device(smart_lock_adapter)

smart_home_system.turn_on_all_devices()
smart_home_system.turn_off_all_devices()