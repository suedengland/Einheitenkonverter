from PySide6 import QtWidgets, QtGui, QtCore

import Einheitenkonverter_GUI
from classes import Temperatur, Druck, Flaeche, Laenge


class DieseApp(QtWidgets.QMainWindow, Einheitenkonverter_GUI.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)  # Einfach gesagt: das erlaubt uns, Variablen aus der GUI-Datei aufzurufen

        self.setupUi(self)

        # Standard-Locale auf Englisch setzen -> Punkt als Dezimaltrenner
        QtCore.QLocale.setDefault(QtCore.QLocale.English)

        # Datenklassen initialisieren
        self.temperatur = Temperatur.Temperatur()
        self.temperatur.celsius = 0

        self.druck = Druck.Druck()
        self.druck.bar = 1

        self.flaeche = Flaeche.Flaeche()
        self.flaeche.m_sq = 1

        self.laenge = Laenge.Laenge()
        self.laenge.m = 1

        # LineEdits aufbereiten (Validator, Initialtext, Signals)
        self.dict_lineEdits_Temperatur = {'kelvin': self.lineEdit_Kelvin,
                                          'celsius': self.lineEdit_Celsius,
                                          'fahrenheit': self.lineEdit_Fahrenheit}
        self.dict_lineEdits_Druck = {'bar': self.lineEdit_bar,
                                     'mbar': self.lineEdit_mbar,
                                     'Pa': self.lineEdit_Pa,
                                     'hPa': self.lineEdit_hPa,
                                     'kPa': self.lineEdit_kPa,
                                     'MPa': self.lineEdit_MPa,
                                     'psi': self.lineEdit_psi}
        self.dict_lineEdits_Flaeche = {'km_sq': self.lineEdit_km_sq,
                                       'm_sq': self.lineEdit_m_sq,
                                       'cm_sq': self.lineEdit_cm_sq,
                                       'mm_sq': self.lineEdit_mm_sq,
                                       'in_sq': self.lineEdit_in_sq,
                                       'a': self.lineEdit_a,
                                       'ha': self.lineEdit_ha}
        self.dict_lineEdits_Laenge = {'km': self.lineEdit_km,
                                      'm': self.lineEdit_m,
                                      'dm': self.lineEdit_dm,
                                      'cm': self.lineEdit_cm,
                                      'mm': self.lineEdit_mm,
                                      'in': self.lineEdit_in,
                                      'ft': self.lineEdit_ft,
                                      'yd': self.lineEdit_yd,
                                      'mi': self.lineEdit_mi}

        tmp_dict = self.temperatur.get_dict()
        for k in self.dict_lineEdits_Temperatur:
            self.dict_lineEdits_Temperatur[k].setValidator(QtGui.QDoubleValidator())
            self.dict_lineEdits_Temperatur[k].setText(f'{tmp_dict[k]:.2f}')
        self.dict_lineEdits_Temperatur['kelvin'].editingFinished.connect(lambda: self.update_temperatur('kelvin'))
        self.dict_lineEdits_Temperatur['celsius'].editingFinished.connect(lambda: self.update_temperatur('celsius'))
        self.dict_lineEdits_Temperatur['fahrenheit'].editingFinished.connect(lambda: self.update_temperatur('fahrenheit'))

        tmp_dict = self.druck.get_dict()
        for k in self.dict_lineEdits_Druck:
            self.dict_lineEdits_Druck[k].setValidator(QtGui.QDoubleValidator())
            self.dict_lineEdits_Druck[k].setText(f'{tmp_dict[k]:.1f}')
        self.dict_lineEdits_Druck['bar'].editingFinished.connect(lambda: self.update_druck('bar'))
        self.dict_lineEdits_Druck['mbar'].editingFinished.connect(lambda: self.update_druck('mbar'))
        self.dict_lineEdits_Druck['Pa'].editingFinished.connect(lambda: self.update_druck('Pa'))
        self.dict_lineEdits_Druck['hPa'].editingFinished.connect(lambda: self.update_druck('hPa'))
        self.dict_lineEdits_Druck['kPa'].editingFinished.connect(lambda: self.update_druck('kPa'))
        self.dict_lineEdits_Druck['MPa'].editingFinished.connect(lambda: self.update_druck('MPa'))
        self.dict_lineEdits_Druck['psi'].editingFinished.connect(lambda: self.update_druck('psi'))

        tmp_dict = self.flaeche.get_dict()
        for k in self.dict_lineEdits_Flaeche:
            self.dict_lineEdits_Flaeche[k].setValidator(QtGui.QDoubleValidator())
            self.dict_lineEdits_Flaeche[k].setText(f'{tmp_dict[k]:.1f}')
        self.dict_lineEdits_Flaeche['km_sq'].editingFinished.connect(lambda: self.update_flaeche('km_sq'))
        self.dict_lineEdits_Flaeche['m_sq'].editingFinished.connect(lambda: self.update_flaeche('m_sq'))
        self.dict_lineEdits_Flaeche['cm_sq'].editingFinished.connect(lambda: self.update_flaeche('cm_sq'))
        self.dict_lineEdits_Flaeche['mm_sq'].editingFinished.connect(lambda: self.update_flaeche('mm_sq'))
        self.dict_lineEdits_Flaeche['in_sq'].editingFinished.connect(lambda: self.update_flaeche('in_sq'))
        self.dict_lineEdits_Flaeche['a'].editingFinished.connect(lambda: self.update_flaeche('a'))
        self.dict_lineEdits_Flaeche['ha'].editingFinished.connect(lambda: self.update_flaeche('ha'))

        tmp_dict = self.laenge.get_dict()
        for k in self.dict_lineEdits_Laenge:
            self.dict_lineEdits_Laenge[k].setValidator(QtGui.QDoubleValidator())
            self.dict_lineEdits_Laenge[k].setText(f'{tmp_dict[k]:.3f}')
        self.dict_lineEdits_Laenge['km'].editingFinished.connect(lambda: self.update_laenge('km'))
        self.dict_lineEdits_Laenge['m'].editingFinished.connect(lambda: self.update_laenge('m'))
        self.dict_lineEdits_Laenge['dm'].editingFinished.connect(lambda: self.update_laenge('dm'))
        self.dict_lineEdits_Laenge['cm'].editingFinished.connect(lambda: self.update_laenge('cm'))
        self.dict_lineEdits_Laenge['mm'].editingFinished.connect(lambda: self.update_laenge('mm'))
        self.dict_lineEdits_Laenge['in'].editingFinished.connect(lambda: self.update_laenge('in'))
        self.dict_lineEdits_Laenge['ft'].editingFinished.connect(lambda: self.update_laenge('ft'))
        self.dict_lineEdits_Laenge['yd'].editingFinished.connect(lambda: self.update_laenge('yd'))
        self.dict_lineEdits_Laenge['mi'].editingFinished.connect(lambda: self.update_laenge('mi'))


    def update_temperatur(self, einheit):
        if einheit == 'kelvin':
            self.temperatur.kelvin = float(self.lineEdit_Kelvin.text())
        elif einheit == 'celsius':
            self.temperatur.celsius = float(self.lineEdit_Celsius.text())
        elif einheit == 'fahrenheit':
            self.temperatur.fahrenheit = float(self.lineEdit_Fahrenheit.text())

        self.lineEdit_Kelvin.setText(f'{self.temperatur.kelvin:.2f}')
        self.lineEdit_Celsius.setText(f'{self.temperatur.celsius:.2f}')
        self.lineEdit_Fahrenheit.setText(f'{self.temperatur.fahrenheit:.2f}')


    def update_druck(self, einheit):
        if einheit == 'bar':
            self.druck.bar = float(self.lineEdit_bar.text())
        elif einheit == 'mbar':
            self.druck.mbar = float(self.lineEdit_mbar.text())
        elif einheit == 'Pa':
            self.druck.Pa = float(self.lineEdit_Pa.text())
        elif einheit == 'hPa':
            self.druck.hPa = float(self.lineEdit_hPa.text())
        elif einheit == 'kPa':
            self.druck.kPa = float(self.lineEdit_kPa.text())
        elif einheit == 'MPa':
            self.druck.MPa = float(self.lineEdit_MPa.text())
        elif einheit == 'psi':
            self.druck.psi = float(self.lineEdit_psi.text())

        self.lineEdit_bar.setText(self.druck.bar_formatted())
        self.lineEdit_mbar.setText(self.druck.mbar_formatted())
        self.lineEdit_Pa.setText(self.druck.Pa_formatted())
        self.lineEdit_hPa.setText(self.druck.hPa_formatted())
        self.lineEdit_kPa.setText(self.druck.kPa_formatted())
        self.lineEdit_MPa.setText(self.druck.MPa_formatted())
        self.lineEdit_psi.setText(self.druck.psi_formatted())


    def update_flaeche(self, einheit):
        if einheit == 'km_sq':
            self.flaeche.km_sq = float(self.lineEdit_km_sq.text())
        elif einheit == 'm_sq':
            self.flaeche.m_sq = float(self.lineEdit_m_sq.text())
        elif einheit == 'cm_sq':
            self.flaeche.cm_sq = float(self.lineEdit_cm_sq.text())
        elif einheit == 'mm_sq':
            self.flaeche.mm_sq = float(self.lineEdit_mm_sq.text())
        elif einheit == 'in_sq':
            self.flaeche.in_sq = float(self.lineEdit_in_sq.text())
        elif einheit == 'a':
            self.flaeche.a = float(self.lineEdit_a.text())
        elif einheit == 'ha':
            self.flaeche.ha = float(self.lineEdit_ha.text())

        self.lineEdit_km_sq.setText(self.flaeche.km_sq_formatted())
        self.lineEdit_m_sq.setText(self.flaeche.m_sq_formatted())
        self.lineEdit_cm_sq.setText(self.flaeche.cm_sq_formatted())
        self.lineEdit_mm_sq.setText(self.flaeche.mm_sq_formatted())
        self.lineEdit_in_sq.setText(self.flaeche.in_sq_formatted())
        self.lineEdit_a.setText(self.flaeche.a_formatted())
        self.lineEdit_ha.setText(self.flaeche.ha_formatted())


    def update_laenge(self, einheit):
        if einheit == 'km':
            self.laenge.km = float(self.lineEdit_km.text())
        elif einheit == 'm':
            self.laenge.m = float(self.lineEdit_m.text())
        elif einheit == 'dm':
            self.laenge.dm = float(self.lineEdit_dm.text())
        elif einheit == 'cm':
            self.laenge.cm = float(self.lineEdit_cm.text())
        elif einheit == 'mm':
            self.laenge.mm = float(self.lineEdit_mm.text())
        elif einheit == 'in':
            self.laenge.inch = float(self.lineEdit_in.text())
        elif einheit == 'ft':
            self.laenge.ft = float(self.lineEdit_ft.text())
        elif einheit == 'yd':
            self.laenge.yd = float(self.lineEdit_yd.text())
        elif einheit == 'mi':
            self.laenge.mi = float(self.lineEdit_mi.text())

        self.lineEdit_km.setText(self.laenge.km_formatted())
        self.lineEdit_m.setText(self.laenge.m_formatted())
        self.lineEdit_dm.setText(self.laenge.dm_formatted())
        self.lineEdit_cm.setText(self.laenge.cm_formatted())
        self.lineEdit_mm.setText(self.laenge.mm_formatted())
        self.lineEdit_in.setText(self.laenge.in_formatted())
        self.lineEdit_ft.setText(self.laenge.ft_formatted())
        self.lineEdit_yd.setText(self.laenge.yd_formatted())
        self.lineEdit_mi.setText(self.laenge.mi_formatted())


def main():
    app = QtWidgets.QApplication([])
    form = DieseApp()
    form.show()
    app.exec()


if __name__ == '__main__':
    main()
