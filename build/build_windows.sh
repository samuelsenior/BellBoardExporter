#! /bin/bash

rm -r ../bin/windows/*;
pyinstaller --noconsole --onefile BellBoardExporter.spec;
cp dist/BellBoardExporter ../bin/windows/BellBoardExporter;
rm -r build ../__pycache__ dist;

