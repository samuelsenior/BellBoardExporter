Warning: As of macOS 10.14.6 there is a bug with macOS which causes a crash when the system tk is used with tkinter. This bug causes the mac build to crash and the user to be logged off, therefore it's not adviced to use "BellBoardExporter" or "BellBoardExporter.app" with macOS 10.14.6 until Apple fix this bug.

Instead, a short script, "BellBoardExporter.command", has been provided that runs the python script. To use this firstly make sure you have python 3 installed and then make sure you have "requests" and "pypdf2" installed via pip using the command "pip3 install requests pypdf2".
