import sys
import platform
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint,
                          QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
# Import MySQL
import mysql.connector as mc
# Import loading screen UI
from loading_screen import Ui_Loading_window
# Import login screen UI
from login_screen import Ui_Login_window
# Import main screen UI
from main_screen import Ui_Main_window

# Globals
GLOBAL_STATE = 0
counter = 0


# Loading window
class Loading_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Loading_window()
        self.ui.setupUi(self)

        # Remove Title Bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        # QTimer Start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(20)

        self.show()

    # App Function
    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)

        # Close loading Screen
        if counter > 100:
            self.timer.stop()

            # Declare main as Login Window
            self.main = Login_window()
            self.main.show()

            self.close()

        counter += 1


# Login window
class Login_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login_window()
        self.ui.setupUi(self)

        # Remove Title Bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Close and Minimize
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # Go To Login Window
        self.ui.btn_login.clicked.connect(self.login_function)

        # Move window
        def move_window(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_2.mouseMoveEvent = move_window

    # Declare Dragging Function
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # App Function

    # Login Function
    def login_function(self):
        if self.ui.username.text() == "" or self.ui.password.text() == "":
            self.ui.label.setText("All field are required")
        else:
            try:
                username = self.ui.username.text()
                password = self.ui.password.text()

                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="student_profiling"
                )

                mycursor = mydb.cursor()
                query = "SELECT username,password FROM admin WHERE username = '" + username + "'AND password = '" + password + "'"
                mycursor.execute(query)
                result = mycursor.fetchone()

                if result is None:
                    self.ui.label.setText("Incorrect username and password")

                elif result:
                    self.go_to_main_window()

            except mc.Error as e:
                self.ui.label.setText("Error")

    # Go to Main Window Function
    def go_to_main_window(self):
        self.main = Main_window()
        self.main.show()
        self.close()


# Main window
class Main_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Main_window()
        self.ui.setupUi(self)

        # Remove Title Bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Close, Maximize/Restore and Minimize
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_maximize_restore.clicked.connect(lambda: self.maximize_restore())

        # Resize Window
        self.sizegrip = QSizeGrip(self.ui.frame_bottom)
        self.sizegrip.setStyleSheet("width: 15px; height: 15px; margin: 0px; padding: 0px;")

        # Go to Pages
        # View Users Page
        self.ui.btn_view_page.clicked.connect(lambda: self.ui.pages_widgets.setCurrentWidget(self.ui.page_view_users))
        # Add User Page
        self.ui.btn_add_page.clicked.connect(lambda: self.ui.pages_widgets.setCurrentWidget(self.ui.page_add_user))
        # Update User Page
        self.ui.btn_update_page.clicked.connect(
            lambda: self.ui.pages_widgets.setCurrentWidget(self.ui.page_update_user))

        # Go Back to Login
        self.ui.btn_logout.clicked.connect(self.go_to_login_window)

        # Load Table
        self.load_user_data()

        # Load Data in Update Screen
        self.ui.btn_load.clicked.connect(self.load_update_data)

        # Update Table
        self.ui.btn_update.clicked.connect(self.update_user_data)

        # Delete Table
        self.ui.btn_delete.clicked.connect(self.delete_user)

        # Create User
        self.ui.btn_create.clicked.connect(self.create_user)

        # Load Image
        self.no_user_img = QPixmap('icons/user-logout-5866.png')
        self.warning_img = QPixmap('icons/warning-3092.png')
        self.check_img = QPixmap('icons/check-symbol-4794.png')
        self.error_img = QPixmap('icons/close-5758.png')

        # Move window
        def move_window(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_top.mouseMoveEvent = move_window

    # Load User Data
    def load_user_data(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="student_profiling"
        )

        mycursor = mydb.cursor()
        load_data = "SELECT * FROM student_table"
        mycursor.execute(load_data)
        result = mycursor.fetchall()

        self.ui.tableWidget.setRowCount(len(result))
        tablerow = 0

        for row in result:
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5].strftime('%Y-%m-%d')))
            self.ui.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))

            tablerow += 1

    # Load to Update Page
    def load_update_data(self):
        if self.ui.student_id_2.text() == "":
            self.ui.notif_3.setText("Enter Student ID")
        else:
            try:
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="student_profiling"
                )

                student_id = self.ui.student_id_2.text()

                mycursor = mydb.cursor()
                load_data = "SELECT * FROM student_table where student_id = '" + student_id + "'"
                mycursor.execute(load_data)
                result = mycursor.fetchone()

                if result:
                    self.ui.firstname_2.setText(result[1])
                    self.ui.lastname_2.setText(result[2])
                    self.ui.address_2.setText(result[3])
                    self.ui.course_year_2.setText(result[4])
                    self.ui.dateEdit_2.setDate(result[5])
                    self.ui.email_2.setText(result[6])
                    self.ui.mobile_no_2.setText(result[7])

            except mc.Error as e:
                self.ui.notif_3.setText("Error")

    # Update Data
    def update_user_data(self):
        if self.ui.student_id_2.text() == "":
            self.ui.notif_2.setText("Enter Student ID")

        else:
            try:
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="student_profiling"
                )

                studentid = self.ui.student_id_2.text()
                fname = self.ui.firstname_2.text()
                lname = self.ui.lastname_2.text()
                add = self.ui.address_2.text()
                courseyear = self.ui.course_year_2.text()
                birthdate = self.ui.dateEdit_2.text()
                email = self.ui.email_2.text()
                mobileno = self.ui.mobile_no_2.text()

                mycursor1 = mydb.cursor()
                check_student_id = "SELECT * FROM student_table WHERE student_id = '" + studentid + "'"
                mycursor1.execute(check_student_id)
                result = mycursor1.fetchone()

                if result is None:
                    self.ui.notif_2.setText("Invalid Student ID")

                elif studentid == "" or fname == "" or lname =="" or add == "" or courseyear == "" or email == "" or mobileno == "":
                    self.ui.notif_2.setText("Click Load")

                else:
                    mycursor = mydb.cursor()
                    query2 = "UPDATE student_table SET  fname = '" + fname + "', lname = '" + lname + "', student_address = '" + add + "', course_year = '" + courseyear + "', birth_date = '" + birthdate + "', email = '" + email + "', mobile_no = '" + mobileno + "' WHERE student_id = '" + studentid + "'"
                    mycursor.execute(query2)
                    mydb.commit()

                    self.ui.notif_2.setText("Successfully Updated")
                    self.ui.student_id_2.setText("")
                    self.ui.firstname_2.setText("")
                    self.ui.lastname_2.setText("")
                    self.ui.address_2.setText("")
                    self.ui.course_year_2.setText("")
                    self.ui.dateEdit_2.setDate(QtCore.QDate(2021, 1, 1))
                    self.ui.email_2.setText("")
                    self.ui.mobile_no_2.setText("")
                    self.load_user_data()

            except mc.Error as e:
                self.ui.notif_2.setText("Error")

    # Delete Data
    def delete_user(self):
        if self.ui.student_id_delete.text() == "":
            self.ui.status_2.setPixmap(self.warning_img)
        else:
            try:
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="student_profiling"
                )
                student_id = self.ui.student_id_delete.text()

                mycursor = mydb.cursor()
                check_student_id = "SELECT * FROM student_table WHERE student_id = '" + student_id + "'"
                mycursor.execute(check_student_id)
                result = mycursor.fetchone()

                if result is None:
                    self.ui.status_2.setPixmap(self.no_user_img)

                else:
                    query = "DELETE FROM student_table WHERE student_id = '" + student_id + "'"
                    mycursor.execute(query)
                    mydb.commit()
                    self.ui.status_2.setPixmap(self.check_img)
                    self.ui.student_id_delete.setText("")
                    self.load_user_data()

            except mc.Error as e:
                self.ui.status_2.setPixmap(self.error_img)

    # Create User
    def create_user(self):
        if self.ui.firstname.text() == "" or self.ui.lastname.text() == "" or self.ui.student_id.text() == "" or \
                self.ui.course_year.text() == "" or self.ui.address.text() == "" or self.ui.email.text() == "" \
                or self.ui.mobile_no.text() == "":
            self.ui.notif.setText("All fields are Required")
        else:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="student_profiling"
            )

            student_id = self.ui.student_id.text()
            first_name = self.ui.firstname.text()
            last_name = self.ui.lastname.text()
            address = self.ui.address.text()
            birthdate = self.ui.dateEdit.text()
            course_year = self.ui.course_year.text()
            email = self.ui.email.text()
            mobile_no = self.ui.mobile_no.text()

            mycursor = mydb.cursor()

            check_student_id = "SELECT * FROM student_table WHERE student_id = '" + student_id + "'"
            mycursor.execute(check_student_id)
            result = mycursor.fetchone()

            if result is not None:
                self.ui.notif.setText("Student ID Already Existed")

            else:
                query = "INSERT INTO student_table (student_id, fname, lname, student_address, course_year, \
                birth_date, email, mobile_no)" \
                        " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                value = (student_id, first_name, last_name, address, course_year, birthdate, email, mobile_no)
                mycursor.execute(query, value)
                mydb.commit()
                self.ui.notif.setText("Added Successfully")
                self.ui.student_id.setText("")
                self.ui.firstname.setText("")
                self.ui.lastname.setText("")
                self.ui.address.setText("")
                self.ui.course_year.setText("")
                self.ui.dateEdit.setDate(QtCore.QDate(2021, 1, 1))
                self.ui.email.setText("")
                self.ui.mobile_no.setText("")
                self.ui.notif.setText("")
                self.load_user_data()

    # Go Back to Login Window Function
    def go_to_login_window(self):
        self.main = Login_window()
        self.main.show()
        self.close()

    # Maximize and Restore Function
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")

    # Declare Dragging Event
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Loading_window()
    sys.exit(app.exec_())
