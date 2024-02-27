from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6 import uic
from PyQt6.QtCore import QTimer
from pylogix import PLC
tag_list = ["T4[1].ACC", "T4[2].ACC", "T4[7].ACC", "T4[8].ACC", "T4[10].ACC", "T4[11].ACC", "T4[12].ACC", "T4[13].ACC",
            "T4[17].ACC", "T4[19].ACC", "T4[20].ACC", "T4[21].ACC", "T4[22].ACC", "T4[25].ACC", "T4[26].ACC",
            "T4[28].ACC", "T4[29].ACC",
            "T4[50].ACC", "T4[51].ACC", "T4[60].ACC", "C5[0].ACC", "C5[5].ACC", "T4[61].ACC", "T4[62].ACC",
            "Local:3:I.Data.0", "Local:3:I.Data.1", "Local:3:I.Data.2", "Local:3:I.Data.3", "Local:3:I.Data.4",
            "Local:3:I.Data.5", "Local:3:I.Data.6", "Local:3:I.Data.7", "Local:3:I.Data.8", "Local:3:I.Data.9",
            "Local:3:I.Data.10", "Local:3:I.Data.11", "Local:3:I.Data.12", "Local:3:I.Data.13", "Local:3:I.Data.14",
            "Local:3:I.Data.15", "Local:4:I.Data.0", "Local:4:I.Data.1", "Local:4:I.Data.2", "Local:4:I.Data.3",
            "Local:4:I.Data.4", "Local:4:I.Data.5", "Local:4:I.Data.6", "Local:4:I.Data.7", "Local:4:I.Data.8",
            "Local:4:I.Data.9", "Local:4:I.Data.10", "Local:4:I.Data.11", "Local:4:I.Data.12", "Local:4:I.Data.13",
            "Local:5:I.Data.0", "Local:5:I.Data.1", "Local:5:I.Data.2",
            "Local:5:I.Data.3", "Local:5:I.Data.4", "Local:5:I.Data.5", "Local:5:I.Data.6",
            "Local:5:I.Data.8", "Local:5:I.Data.9", "Local:5:I.Data.10", "Local:6:I.Data.0", "Local:6:I.Data.1",
            "Local:6:I.Data.2", "Local:6:I.Data.3", "Local:6:I.Data.4", "Local:6:I.Data.5", "Local:6:I.Data.6",
            "Local:6:I.Data.7", "Local:6:I.Data.8", "Local:6:I.Data.9", "Local:6:I.Data.10", "Local:6:I.Data.11",
            "Local:6:I.Data.12"]


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("diagnostic_blackstart_ppc.ui", self)

        # Accessing all QTextEdit widgets from the loaded UI file

        self.line_edit_objects = self.findChildren(QLineEdit)  # Find all QTextEdit widgets
        for line_edit in self.line_edit_objects:
            line_edit.setStyleSheet("background-color: lightblue;")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_text_edit)
        self.timer.start(1000)

        # Membuka koneksi ke PLC
        self.comm = PLC()
        self.comm.IPAddress = '192.168.1.10'  # Ganti dengan alamat IP PLC 5000
        self.comm.ProcessorSlot = 0

    def update_text_edit(self):
        # Membuka koneksi ke PLC
        # Function to update the contents of QTextEdit widgets
        ret = self.comm.Read(tag_list)

        for line_edit, value in zip(self.line_edit_objects, ret):
            if True == value.Value:
                value.Value = 1
                line_edit.setText(str(value.Value))
            elif False == value.Value:
                value.Value = 0
                line_edit.setText(str(value.Value))
            else:
                line_edit.setText(str(value.Value))


app = QApplication([])
window = UI()
window.show()
app.exec()
