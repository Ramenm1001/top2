# модуль управления климатом
class Climat:
    def __init__(self, temperature, osadki):
        self.temperature = temperature
        self.osadki = osadki

    def __str__(self):
        print (f"Температура: {self.temperature},\nвероятность осадков: {self.osadki}")

