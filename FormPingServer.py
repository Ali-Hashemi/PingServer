from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from Classes.ClassUtility import *

from Classes.MySpinBox import MySpinBox
from Classes.MyDoubleSpinBox import MyDoubleSpinBox
import subprocess
import re
from pythonping import ping


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    NUM_OF_PING = 7

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # subprocess.run(["python", "01-ConvertQtCreatorFileToClass.py"])

        self.shortcut = QShortcut(QKeySequence('Esc'), self)
        self.shortcut.activated.connect(lambda: (self.clear_boxes()))

        self.shortcut = QShortcut(QKeySequence('F1'), self)
        self.shortcut.activated.connect(lambda: (self.get_result()))

        self.shortcut = QShortcut(QKeySequence('F2'), self)
        self.shortcut.activated.connect(lambda: (self.ping_servers()))

        self.pushButton_ping.clicked.connect(lambda: (self.ping_servers()))

        self.pushButton_get_resutl.clicked.connect(lambda: (self.get_result()))

    def ping_servers(self):
        self.clear_boxes()

        textbox_value = str(self.textbox_ips.toPlainText()).split("\n")

        for i in textbox_value:
            if i:
                i=i.strip()
                Print.print_red(i)
                print("")
                Print.print_black("")

                # ---------------------------------------
                # os.system("ping -n 7 " + i)
                # ---------------------------------------

                # ---------------------------------------
                response = ping(i, count=self.NUM_OF_PING, verbose=True)

                # os.system('cls' if os.name == 'nt' else 'clear')

                # for i in response:
                #     print(i)
                # ---------------------------------------

                Print.print_full_line(CustomColor.BLACK)

    def get_result(self):

        self.clear_boxes()

        textbox_value = str(self.textbox_ips.toPlainText()).split("\n")

        clean_servers = []
        filtered_servers = []

        for i in textbox_value:
            if i:
                Print.print_red(i)
                print("")

                ping_text = 'ping -n ' + str(self.NUM_OF_PING) + ' ' + i

                # response = os.popen('ping -n 6 i')

                response = os.popen(ping_text)

                counter = 0

                for line in response.readlines():

                    x = re.search("^Reply from", line)

                    if x:
                        Print.print_black(line)
                        counter += 1

                if counter == (self.NUM_OF_PING):
                    clean_servers.append(i)
                    # Print.print_green(i)

                else:
                    filtered_servers.append(i)
                    # Print.print_red(i)

                Print.print_full_line(CustomColor.MAGENTA)

        self.listWidget_clean.addItems(clean_servers)
        self.listWidget_filtered.addItems(filtered_servers)

        self.label_clean_ip_number.setText(str(clean_servers.__len__()))
        self.label_filter_ip_number.setText(str(filtered_servers.__len__()))

    def clear_boxes(self):

        # self.textbox_ips.setPlainText("")

        self.listWidget_filtered.clear()
        self.listWidget_clean.clear()

        self.label_clean_ip_number.setText("0")
        self.label_filter_ip_number.setText("0")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
