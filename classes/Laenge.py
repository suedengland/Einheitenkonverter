from dataclasses import dataclass
from classes.decorators import value_formatter

@dataclass
class Laenge():
    _km: float = None
    _m: float = None
    _dm: float = None
    _cm: float = None
    _mm: float = None
    _in: float = None
    _ft: float = None
    _yd: float = None
    _mi: float = None

    decimals = 2

    @property
    def km(self):
        return self._km
    @km.setter
    def km(self, val):
        self._km = val
        self._m = self._km*1000
        self._dm = self._m*10
        self._cm = self._m*100
        self._mm = self._m*1000
        self._in = self._cm/2.54
        self._ft = self._in/12
        self._yd = self._in/36
        self._mi = self._yd/1760
    @value_formatter(decimals=decimals)
    def km_formatted(self):
        return self._km

    @property
    def m(self):
        return self._m
    @m.setter
    def m(self, val):
        self._m = val
        self._km = self._m/1000
        self._dm = self._m*10
        self._cm = self._m*100
        self._mm = self._m*1000
        self._in = self._cm/2.54
        self._ft = self._in/12
        self._yd = self._in/36
        self._mi = self._yd/1760
    @value_formatter(decimals=decimals)
    def m_formatted(self):
        return self._m

    @property
    def dm(self):
        return self._dm
    @dm.setter
    def dm(self, val):
        self._dm = val
        self._m = self._dm/10
        self._km = self._m/1000
        self._cm = self._m*100
        self._mm = self._m*1000
        self._in = self._cm/2.54
        self._ft = self._in/12
        self._yd = self._in/36
        self._mi = self._yd/1760
    @value_formatter(decimals=decimals)
    def dm_formatted(self):
        return self._dm

    @property
    def cm(self):
        return self._cm
    @cm.setter
    def cm(self, val):
        self._cm = val
        self._m = self._cm/100
        self._km = self._m/1000
        self._dm = self._m*10
        self._mm = self._m*1000
        self._in = self._cm/2.54
        self._ft = self._in/12
        self._yd = self._in/36
        self._mi = self._yd/1760
    @value_formatter(decimals=decimals)
    def cm_formatted(self):
        return self._cm

    @property
    def mm(self):
        return self._mm
    @mm.setter
    def mm(self, val):
        self._mm = val
        self._m = self._mm/1000
        self._km = self._m/1000
        self._dm = self._m*10
        self._cm = self._m*100
        self._in = self._cm/2.54
        self._ft = self._in/12
        self._yd = self._in/36
        self._mi = self._yd/1760
    @value_formatter(decimals=decimals)
    def mm_formatted(self):
        return self._mm

    @property
    def inch(self):
        return self._in
    @inch.setter
    def inch(self, val):
        self._in = val
        self._ft = self._in/12
        self._yd = self._in/36
        self._mi = self._yd/1760
        self._cm = self._in*2.54
        self._m = self._cm/100
        self._km = self._m/1000
        self._dm = self._m*10
        self._mm = self._m*1000
    @value_formatter(decimals=decimals)
    def in_formatted(self):
        return self._in

    @property
    def ft(self):
        return self._ft
    @ft.setter
    def ft(self, val):
        self._ft = val
        self._in = self._ft*12
        self._yd = self._in/36
        self._mi = self._yd/1760
        self._cm = self._in*2.54
        self._m = self._cm/100
        self._km = self._m/1000
        self._dm = self._m*10
        self._mm = self._m*1000
    @value_formatter(decimals=decimals)
    def ft_formatted(self):
        return self._ft

    @property
    def yd(self):
        return self._yd
    @yd.setter
    def yd(self, val):
        self._yd = val
        self._mi = self._yd/1760
        self._in = self._yd*36
        self._ft = self._in/12
        self._cm = self._in*2.54
        self._m = self._cm/100
        self._km = self._m/1000
        self._dm = self._m*10
        self._mm = self._m*1000
    @value_formatter(decimals=decimals)
    def yd_formatted(self):
        return self._yd

    @property
    def mi(self):
        return self._mi
    @mi.setter
    def mi(self, val):
        self._mi = val
        self._yd = self._mi*1760
        self._in = self._yd*36
        self._ft = self._in/12
        self._cm = self._in*2.54
        self._m = self._cm/100
        self._km = self._m/1000
        self._dm = self._m*10
        self._mm = self._m*1000
    @value_formatter(decimals=decimals)
    def mi_formatted(self):
        return self._mi

    def get_dict(self):
        return {'km': self._km, 'm': self._m, 'dm': self._dm, 'cm': self._cm, 'mm': self._mm, 'in': self._in, 'ft': self._ft, 'yd': self._yd, 'mi': self._mi}