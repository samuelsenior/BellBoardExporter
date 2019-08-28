#! /bin/bash

rm -r ../bin/linux/*;
pyinstaller --noconsole --onefile BellBoardExporter.spec;
cp dist/BellBoardExporter ../bin/linux/BellBoardExporter;
rm -r build ../__pycache__ dist;
