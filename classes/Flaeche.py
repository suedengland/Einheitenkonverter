from dataclasses import dataclass
from classes.decorators import value_formatter

@dataclass
class Flaeche():
    _km_sq: float = None
    _m_sq: float = None
    _cm_sq: float = None
    _mm_sq: float = None
    _in_sq: float = None
    _a: float = None
    _ha: float = None

    @property
    def km_sq(self):
        return self._km_sq
    @km_sq.setter
    def km_sq(self, val):
        self._km_sq = val
        self._m_sq = self._km_sq*1e6
        self._cm_sq = self._m_sq*1e4
        self._mm_sq = self._m_sq*1e6
        self._in_sq = self._cm_sq/(2.54**2)
        self._a = self._m_sq/1e2
        self._ha = self._a/100
    @value_formatter
    def km_sq_formatted(self):
        return self._km_sq

    @property
    def m_sq(self):
        return self._m_sq
    @m_sq.setter
    def m_sq(self, val):
        self._m_sq = val
        self._km_sq = self._m_sq/1e6
        self._cm_sq = self._m_sq*1e4
        self._mm_sq = self._m_sq*1e6
        self._in_sq = self._cm_sq/(2.54**2)
        self._a = self._m_sq/1e2
        self._ha = self._a/100
    @value_formatter
    def m_sq_formatted(self):
        return self._m_sq

    @property
    def cm_sq(self):
        return self._cm_sq
    @cm_sq.setter
    def cm_sq(self, val):
        self._cm_sq = val
        self._m_sq = self._cm_sq/1e4
        self._km_sq = self._m_sq/1e6
        self._mm_sq = self._m_sq*1e6
        self._in_sq = self._cm_sq/(2.54**2)
        self._a = self._m_sq/1e2
        self._ha = self._a/100
    @value_formatter
    def cm_sq_formatted(self):
        return self._cm_sq

    @property
    def mm_sq(self):
        return self._mm_sq
    @mm_sq.setter
    def mm_sq(self, val):
        self._mm_sq = val
        self._m_sq = self._mm_sq/1e6
        self._km_sq = self._m_sq/1e6
        self._cm_sq = self._m_sq*1e4
        self._in_sq = self._cm_sq/(2.54**2)
        self._a = self._m_sq/1e2
        self._ha = self._a/100
    @value_formatter
    def mm_sq_formatted(self):
        return self._mm_sq

    @property
    def in_sq(self):
        return self._in_sq
    @in_sq.setter
    def in_sq(self, val):
        self._in_sq = val
        self._cm_sq = self._in_sq*(2.54**2)
        self._m_sq = self._cm_sq/1e4
        self._km_sq = self._m_sq/1e6
        self._mm_sq = self._m_sq*1e6
        self._a = self._m_sq/1e2
        self._ha = self._a/100
    @value_formatter
    def in_sq_formatted(self):
        return self._in_sq

    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, val):
        self._a = val
        self._m_sq = self._a*100
        self._km_sq = self._m_sq/1e6
        self._cm_sq = self._m_sq*1e4
        self._mm_sq = self._m_sq*1e6
        self._in_sq = self._cm_sq/(2.54**2)
        self._ha = self._a/100
    @value_formatter
    def a_formatted(self):
        return self._a

    @property
    def ha(self):
        return self._ha
    @ha.setter
    def ha(self, val):
        self._ha = val
        self._a = self.ha*100
        self._m_sq = self._a*100
        self._km_sq = self._m_sq/1e6
        self._cm_sq = self._m_sq*1e4
        self._mm_sq = self._m_sq*1e6
        self._in_sq = self._cm_sq/(2.54**2)
    @value_formatter
    def ha_formatted(self):
        return self._ha

    def get_dict(self):
        return {'km_sq': self._km_sq, 'm_sq': self._m_sq, 'cm_sq': self._cm_sq, 'mm_sq': self._mm_sq, 'in_sq': self._in_sq, 'a': self._a, 'ha': self._ha}