from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_window(object):
    def setupUi(self, Login_window):
        Login_window.setObjectName("Login_window")
        Login_window.resize(480, 667)
        self.centralwidget = QtWidgets.QWidget(Login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(480, 680))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top = QtWidgets.QFrame(self.frame)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_top.setStyleSheet("background-color: rgb(40, 57, 113);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_top)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_7 = QtWidgets.QFrame(self.frame_top)
        self.frame_7.setMinimumSize(QtCore.QSize(100, 40))
        self.frame_7.setMaximumSize(QtCore.QSize(100, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_7)
        self.btn_minimize.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_minimize.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    image: url(:/20x20/icons/20x20/cil-minus.png);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 123, 75);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(161, 145, 88);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_7)
        self.btn_close.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_close.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    \n"
"    image: url(:/20x20/icons/20x20/cil-x.png);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 123, 75);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(161, 145, 88);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_3.addWidget(self.frame_top)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_3.setStyleSheet("image: url(:/login_logo/icons/user-4250 (1).png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_13 = QtWidgets.QFrame(self.frame_6)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_4.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_4.setStyleSheet("image: url(:/login_logo/icons/person-295.png);\n"
"background-color: transparent")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.username = QtWidgets.QLineEdit(self.frame_6)
        self.username.setMinimumSize(QtCore.QSize(240, 40))
        self.username.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"    border-radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(64, 92, 182)\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"    background-color: transparent\n"
"}")
        self.username.setObjectName("username")
        self.horizontalLayout_4.addWidget(self.username)
        self.frame_14 = QtWidgets.QFrame(self.frame_6)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_4.addWidget(self.frame_14)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_18 = QtWidgets.QFrame(self.frame_8)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_3.addWidget(self.frame_18)
        self.frame_5 = QtWidgets.QFrame(self.frame_8)
        self.frame_5.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_5.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_5.setStyleSheet("image: url(:/login_logo/icons/padlock-328.png);\n"
"background-color: transparent")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.password = QtWidgets.QLineEdit(self.frame_8)
        self.password.setMinimumSize(QtCore.QSize(240, 40))
        self.password.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"    border-radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(64, 92, 182)\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"    background-color: transparent\n"
"}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.frame_20 = QtWidgets.QFrame(self.frame_8)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_3.addWidget(self.frame_20)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.frame_17 = QtWidgets.QFrame(self.frame)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_21 = QtWidgets.QFrame(self.frame_17)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_6.addWidget(self.frame_21)
        self.label = QtWidgets.QLabel(self.frame_17)
        self.label.setMinimumSize(QtCore.QSize(300, 30))
        self.label.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: rgb(161, 145, 88);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: transparent;\n"
"}")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_6.addWidget(self.frame_19)
        self.verticalLayout_3.addWidget(self.frame_17)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_15 = QtWidgets.QFrame(self.frame_9)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_5.addWidget(self.frame_15)
        self.btn_login = QtWidgets.QPushButton(self.frame_9)
        self.btn_login.setMinimumSize(QtCore.QSize(137, 40))
        self.btn_login.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"    border-radius: 10px;\n"
"    color: rgb(161, 145, 88);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(64, 92, 182)\n"
"}\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(40, 57, 113);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_5.addWidget(self.btn_login)
        self.frame_16 = QtWidgets.QFrame(self.frame_9)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_5.addWidget(self.frame_16)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3.addWidget(self.frame_10)
        self.verticalLayout.addWidget(self.frame)
        Login_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_window)
        QtCore.QMetaObject.connectSlotsByName(Login_window)

    def retranslateUi(self, Login_window):
        _translate = QtCore.QCoreApplication.translate
        Login_window.setWindowTitle(_translate("Login_window", "MainWindow"))
        self.username.setPlaceholderText(_translate("Login_window", "Username"))
        self.password.setPlaceholderText(_translate("Login_window", "Password"))
        self.btn_login.setText(_translate("Login_window", "Login"))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_window = QtWidgets.QMainWindow()
    ui = Ui_Login_window()
    ui.setupUi(Login_window)
    Login_window.show()
    sys.exit(app.exec_())
