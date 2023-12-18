from dataclasses import dataclass
from classes.decorators import value_formatter

@dataclass
class Druck():
    _bar: float = None
    _mbar: float = None
    _Pa: float = None
    _hPa: float = None
    _kPa: float = None
    _MPa: float = None

    @property
    def bar(self):
        return self._bar
    @bar.setter
    def bar(self, val):
        self._bar = val
        self._mbar = self._bar*1000
        self._Pa = self._bar*1e5
        self._hPa = self._Pa/100
        self._kPa = self._Pa/1000
        self._MPa = self._Pa/1e6
    @value_formatter
    def bar_formatted(self):
        return self._bar

    @property
    def mbar(self):
        return self._mbar
    @mbar.setter
    def mbar(self, val):
        self._mbar = val
        self._bar = self._mbar/1000
        self._Pa = self._bar*1e5
        self._hPa = self._Pa/100
        self._kPa = self._Pa/1000
        self._MPa = self._Pa/1e6
    @value_formatter
    def mbar_formatted(self):
        return self._mbar

    @property
    def Pa(self):
        return self._Pa
    @Pa.setter
    def Pa(self, val):
        self._Pa = val
        self._hPa = self._Pa/100
        self._kPa = self._Pa/1000
        self._MPa = self._Pa/1e6
        self._bar = self._Pa/1e5
        self._mbar = self._bar*1000
    @value_formatter
    def Pa_formatted(self):
        return self._Pa

    @property
    def hPa(self):
        return self._hPa
    @hPa.setter
    def hPa(self, val):
        self._hPa = val
        self._Pa = self._hPa*100
        self._kPa = self._Pa/1000
        self._MPa = self._Pa/1e6
        self._bar = self._Pa/1e5
        self._mbar = self._bar*1000
    @value_formatter
    def hPa_formatted(self):
        return self._hPa

    @property
    def kPa(self):
        return self._kPa
    @kPa.setter
    def kPa(self, val):
        self._kPa = val
        self._Pa = self._kPa*1000
        self._hPa = self._Pa/100
        self._MPa = self._Pa/1e6
        self._bar = self._Pa/1e5
        self._mbar = self._bar*1000
    @value_formatter
    def kPa_formatted(self):
        return self._kPa

    @property
    def MPa(self):
        return self._MPa
    @MPa.setter
    def MPa(self, val):
        self._MPa = val
        self._Pa = self._MPa*1e6
        self._hPa = self._Pa/100
        self._kPa = self._Pa/1000
        self._bar = self._Pa/1e5
        self._mbar = self._bar*1000
    @value_formatter
    def MPa_formatted(self):
        return self._MPa

    def get_dict(self):
        return {'bar': self._bar, 'mbar': self._mbar, 'Pa': self._Pa, 'hPa': self._hPa, 'kPa': self._kPa, 'MPa': self._MPa}