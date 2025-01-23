## Installation
***Die folgende Anleitung bezieht sich auf die Windows PowerShell***

Virtuelle Python-Umgebung anlegen
```
python -m venv .\py_venv
```

Virtuelle Python-Umgebung aktivieren
```
.\py_venv\Scripts\Activate.ps1
```

Test, ob Verknüpfung zur virtuellen Python-Umgebung richtig ist
```
Get-Command python
Get-Command pip
```

Pakete aus der requirements.txt installieren
```
pip install -r requirements.txt
```


## Dateien
- Einheitenkonverter_GUI.ui:  wird mit Qt Designer geöffnet/editiert und enthält die GUI
- Einheitenkonverter_GUI.py:  wird mittels `pyside6-uic Einheitenkonverter_GUI.ui -o Einheitenkonverter_GUI.py` erzeugt und kann anschließend in Einheitenkonverter.py importiert werden
- Einheitenkonverter.py: hier sind die eigentlichen Funktionen der App implementiert und kann mittels `python Einheitenkonverter.py` ausgeführt werden (venv aktivieren!)


## GUI-Entwicklung
Der Qt Designer befindet sich unter folgender Adresse und kann ausgeführt werden, ohne dass die virtuelle Python-Umgebung geladen wurde
```
\\PFAD_ZUR\py_venv\Lib\site-packages\PySide6\designer.exe
```

Eine Qt .ui-Datei wird anschließend zu einer .py-Datei übersetzt
```
pyside6-uic [...].ui -o [...].py
```


## App starten
Unter Linux kann die App mittels `make` gestartet werden. Dabei wird, je nach Befarf, die .ui-Datei konvertiert,
sollte diese älter sein, als die zugehörige .py-Datei.

Die App kann entweder mit python aus der Kommandozeile (venv aktivieren!) heraus gestartet werden
```
(.\py_venv\Scripts\Activate.ps1)
python Einheitenkonverter.py
```

oder zu einer eigenständigen Exe kompiliert werden
```
pyinstaller --onefile --noconsole --name Einheitenkonverter Einheitenkonverter.py
```

Die Flags bedeuten:
- `--onefile`: Eine einzige Datei erzeugen
- `--noconsole`: Neben dem GUI-Fenster soll keine Konsole (für STDOUT, STDERR) geöffnet werden
- `--name`: Name der Exe

Die Exe liegt anschließend im Ordner `./dist/Einheitenkonverter.exe`
Beim Kompilieren entsteht außerdem eine `EinheitenkonverterEinheitenkonverter.spec`, mit der man wiederum anschließend die Exe ebenfalls kompilieren kann,
da in ihr die Flags als Einstellungen gespeichert sind:
```
pyinstaller Einheitenkonverter.spec
```
