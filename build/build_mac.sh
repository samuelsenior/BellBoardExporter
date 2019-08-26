#! /bin/bash

rm -r ../bin/mac/*

pyinstaller --noconsole --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' ../BellBoardExporter.py;

#pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' BellBoardExporter.py

cp -r dist/BellBoardExporter ../bin/mac/BellBoardExporter&
cp -r dist/BellBoardExporter.app ../bin/mac/BellBoardExporter.app;

rm -r BellBoardExporter.spec build ../__pycache__ dist
