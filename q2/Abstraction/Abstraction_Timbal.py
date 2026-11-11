from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, location: str):
        self.location = location

    @abstractmethod
    def get_reading(self, time_logged: str):
        pass


class PHSensor(Sensor):
    def __init__(self, location: str):
        super().__init__(location)

    def get_reading(self, time_logged: str):
        return f"Reading: 7.2 pH (Neutral) | Logged at: {time_logged}"


class TemperatureSensor(Sensor):
    def __init__(self, location: str):
        super().__init__(location)

    def get_reading(self, time_logged: str):
        return f"Reading: 24.5°C | Logged at: {time_logged}"



print("-" * 4, "Advanced Lab Inventory System", "-" * 4)


p = PHSensor("Chemistry Lab - Station 1")
t = TemperatureSensor("Biology Incubator - Unit B")


print(f"[{p.location}]")
print(f"   {p.get_reading('10:45 AM')}\n")

print(f"[{t.location}]")
print(f"   {t.get_reading('11:00 AM')}")

print("-" * 37)

#my_sensor = Sensor()