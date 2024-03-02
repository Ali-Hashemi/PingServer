import os

from send2trash import send2trash

qtcreator_py_file = "D:\\Tab\\PrintCalculator\\MainWindow.py"

if os.path.exists(qtcreator_py_file):
    send2trash(qtcreator_py_file)

os.system("pyuic5 Mainwindow.ui -o MainWindow.py")

