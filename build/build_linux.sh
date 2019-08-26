#! /bin/bash

rm -r ../bin/linux/*;
pyinstaller --noconsole --onefile ../BellBoardExporter.py;
cp -r dist/BellBoardExporter ../bin/linux/BellBoardExporter;
rm -r BellBoardExporter.spec build ../__pycache__ dist;
