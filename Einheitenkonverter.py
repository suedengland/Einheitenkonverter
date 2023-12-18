from PySide6 import QtWidgets, QtGui, QtCore

import Einheitenkonverter_GUI
from classes import Temperatur, Druck


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

        # LineEdits aufbereiten (Validator, Initialtext, Signals)
        self.dict_lineEdits_Temperatur = {'kelvin': self.lineEdit_Kelvin, 'celsius': self.lineEdit_Celsius, 'fahrenheit': self.lineEdit_Fahrenheit}
        self.dict_lineEdits_Druck = {'bar': self.lineEdit_bar, 'mbar': self.lineEdit_mbar, 'Pa': self.lineEdit_Pa, 'hPa': self.lineEdit_hPa, 'kPa': self.lineEdit_kPa, 'MPa': self.lineEdit_MPa}

        tmp_dict = self.temperatur.get_dict()
        for k in self.dict_lineEdits_Temperatur.keys():
            self.dict_lineEdits_Temperatur[k].setValidator(QtGui.QDoubleValidator())
            self.dict_lineEdits_Temperatur[k].setText(f'{tmp_dict[k]:.2f}')
        self.dict_lineEdits_Temperatur['kelvin'].editingFinished.connect(lambda: self.update_temperatur('kelvin'))
        self.dict_lineEdits_Temperatur['celsius'].editingFinished.connect(lambda: self.update_temperatur('celsius'))
        self.dict_lineEdits_Temperatur['fahrenheit'].editingFinished.connect(lambda: self.update_temperatur('fahrenheit'))

        tmp_dict = self.druck.get_dict()
        for k in self.dict_lineEdits_Druck.keys():
            self.dict_lineEdits_Druck[k].setValidator(QtGui.QDoubleValidator())
            self.dict_lineEdits_Druck[k].setText(f'{tmp_dict[k]:.1f}')
        self.dict_lineEdits_Druck['bar'].editingFinished.connect(lambda: self.update_druck('bar'))
        self.dict_lineEdits_Druck['mbar'].editingFinished.connect(lambda: self.update_druck('mbar'))
        self.dict_lineEdits_Druck['Pa'].editingFinished.connect(lambda: self.update_druck('Pa'))
        self.dict_lineEdits_Druck['hPa'].editingFinished.connect(lambda: self.update_druck('hPa'))
        self.dict_lineEdits_Druck['kPa'].editingFinished.connect(lambda: self.update_druck('kPa'))
        self.dict_lineEdits_Druck['MPa'].editingFinished.connect(lambda: self.update_druck('MPa'))


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

        self.lineEdit_bar.setText(self.druck.bar_formatted())
        self.lineEdit_mbar.setText(self.druck.mbar_formatted())
        self.lineEdit_Pa.setText(self.druck.Pa_formatted())
        self.lineEdit_hPa.setText(self.druck.hPa_formatted())
        self.lineEdit_kPa.setText(self.druck.kPa_formatted())
        self.lineEdit_MPa.setText(self.druck.MPa_formatted())


def main():
    app = QtWidgets.QApplication([])
    form = DieseApp()
    form.show()
    app.exec()


if __name__ == '__main__':
    main()
