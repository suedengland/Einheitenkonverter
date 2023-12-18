from PySide6 import QtWidgets, QtGui, QtCore

import Einheitenkonverter_GUI


class DieseApp(QtWidgets.QMainWindow, Einheitenkonverter_GUI.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)  # Einfach gesagt: das erlaubt uns, Variablen aus der GUI-Datei aufzurufen

        self.setupUi(self)

        # Standard-Locale auf Englisch setzen -> Punkt als Dezimaltrenner
        QtCore.QLocale.setDefault(QtCore.QLocale.English)

        self.lineEdit_Kelvin.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_Celsius.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_Fahrenheit.setValidator(QtGui.QDoubleValidator())

        self.lineEdit_Kelvin.editingFinished.connect(lambda: self.update_temperatur('kelvin'))
        self.lineEdit_Celsius.editingFinished.connect(lambda: self.update_temperatur('celsius'))
        self.lineEdit_Fahrenheit.editingFinished.connect(lambda: self.update_temperatur('fahrenheit'))


    def update_temperatur(self, einheit):
        if einheit == 'kelvin':
            tmp_kelvin = float(self.lineEdit_Kelvin.text())
            tmp_celsius = tmp_kelvin - 273.15
            tmp_fahrenheit = tmp_kelvin*(9/5) - 459.67
        elif einheit == 'celsius':
            tmp_celsius = float(self.lineEdit_Celsius.text())
            tmp_kelvin = tmp_celsius + 273.15
            tmp_fahrenheit = tmp_celsius*(9/5) + 32
        elif einheit == 'fahrenheit':
            tmp_fahrenheit = float(self.lineEdit_Fahrenheit.text())
            tmp_kelvin = (tmp_fahrenheit + 459.67)*5/9
            tmp_celsius = (tmp_fahrenheit - 32)*5/9

        self.lineEdit_Kelvin.setText(f'{tmp_kelvin:.2f}')
        self.lineEdit_Celsius.setText(f'{tmp_celsius:.2f}')
        self.lineEdit_Fahrenheit.setText(f'{tmp_fahrenheit:.2f}')


def main():
    app = QtWidgets.QApplication([])
    form = DieseApp()
    form.show()
    app.exec()


if __name__ == '__main__':
    main()
