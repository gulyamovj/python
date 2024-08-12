class Auto:
    def __init__(self):
        self.number = ""
        self.power = 0

    def get_tax(self, min_rate=12, max_rate=25):
        rate = min_rate
        if self.power > 100:
            rate = max_rate
        return rate * self.power * 1.2

class Bus(Auto):
    def get_tax(self, min_rate=15, max_rate=15):
        return super().get_tax(min_rate, max_rate)

auto = Auto()
auto.power = 100
print(auto.get_tax())

bus = Bus()
bus.power = 100
print(bus.get_tax())