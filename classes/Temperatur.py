from dataclasses import dataclass

@dataclass
class Temperatur():
    _kelvin: float = None
    _celsius: float = None
    _fahrenheit: float = None

    @property
    def kelvin(self):
        return self._kelvin
    @kelvin.setter
    def kelvin(self, val):
        self._kelvin = val
        self._celsius = self._kelvin - 273.15
        self._fahrenheit = self._kelvin*(9/5) - 459.67

    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, val):
        self._celsius = val
        self._kelvin = self._celsius + 273.15
        self._fahrenheit = self._celsius*(9/5) + 32

    @property
    def fahrenheit(self):
        return self._fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, val):
        self._fahrenheit = val
        self._kelvin = (self._fahrenheit + 459.67) * 5/9
        self._celsius = (self._fahrenheit - 32) * 5/9

    def get_dict(self):
        return {'kelvin': self._kelvin, 'celsius': self._celsius, 'fahrenheit': self._fahrenheit}