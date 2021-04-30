from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Loading_window(object):
    def setupUi(self, Loading_window):
        Loading_window.setObjectName("Loading_window")
        Loading_window.setWindowModality(QtCore.Qt.ApplicationModal)
        Loading_window.resize(680, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Loading_window.sizePolicy().hasHeightForWidth())
        Loading_window.setSizePolicy(sizePolicy)
        Loading_window.setMaximumSize(QtCore.QSize(16777215, 16777213))
        Loading_window.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        Loading_window.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(Loading_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(50, 240, 581, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    \n"
"    background-color: rgb(40, 57, 113);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(161, 145, 88);\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 260, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(40, 57, 113);\n"
"background-color: transparent;\n"
"border: none;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(-10, 350, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(40, 57, 113);\n"
"background-color: transparent;\n"
"border: none;")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(50, 40, 581, 171))
        self.frame_2.setStyleSheet("background-color: rgb(40, 57, 113);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 40, 581, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(161, 145, 88);\n"
"border-radius: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        Loading_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Loading_window)
        QtCore.QMetaObject.connectSlotsByName(Loading_window)

    def retranslateUi(self, Loading_window):
        _translate = QtCore.QCoreApplication.translate
        Loading_window.setWindowTitle(_translate("Loading_window", "MainWindow"))
        self.label_3.setText(_translate("Loading_window", "loading..."))
        self.label_4.setText(_translate("Loading_window", "<html><head/><body><p><span style=\" font-weight:600;\">Developed by:</span> Group D</p></body></html>"))
        self.label.setText(_translate("Loading_window", "<html><head/><body><p><span style=\" font-weight:600;\">STUDENT PROFILING</span> APP</p></body></html>"))
    import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Loading_window = QtWidgets.QMainWindow()
    ui = Ui_Loading_window()
    ui.setupUi(Loading_window)
    Loading_window.show()
    sys.exit(app.exec_())
