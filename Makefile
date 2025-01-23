gui_file = Einheitenkonverter_GUI
main_file = Einheitenkonverter.py

venv = PATH/TO/PYVENV/bin/activate

OBJECTS = $(gui_file).py

all: $(OBJECTS) run

$(OBJECTS): %.py: %.ui
	. $(venv) && pyside6-uic $< -o $@

run:
	. $(venv) && python $(main_file)
