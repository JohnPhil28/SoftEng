from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_window(object):
    def setupUi(self, Main_window):
        Main_window.setObjectName("Main_window")
        Main_window.resize(1002, 680)
        self.centralwidget = QtWidgets.QWidget(Main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("background-color: rgb(40, 57, 113);")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top = QtWidgets.QFrame(self.frame_main)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_top.setStyleSheet("background-color: rgb(40, 57, 113);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top)
        self.frame_label_top_btns.setMinimumSize(QtCore.QSize(0, 23))
        self.frame_label_top_btns.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_top_btns.setStyleSheet("background-color: rgb(40, 57, 113);")
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_icon_top_bar = QtWidgets.QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
"image: url(:/16x16/icons/16x16/cil-user.png);\n"
"")
        self.frame_icon_top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)
        self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
"color: rgb(161, 145, 88);\n"
"margin-left: 5px;")
        self.label_title_bar_top.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.horizontalLayout_2.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QtWidgets.QFrame(self.frame_top)
        self.frame_btns_right.setMinimumSize(QtCore.QSize(0, 23))
        self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 30))
        self.frame_btns_right.setStyleSheet("background-color:rgb(40, 57, 113)")
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns_right)
        self.btn_minimize.setMaximumSize(QtCore.QSize(40, 30))
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
"    image: url(:/20x20/icons/20x20/cil-window-minimize.png);\n"
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
        self.horizontalLayout_5.addWidget(self.btn_minimize)
        self.btn_maximize_restore = QtWidgets.QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setMaximumSize(QtCore.QSize(40, 30))
        self.btn_maximize_restore.setStyleSheet("QPushButton {\n"
"    image: url(:/20x20/icons/20x20/cil-window-maximize.png);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 123, 75);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(161, 145, 88);\n"
"}")
        self.btn_maximize_restore.setText("")
        self.btn_maximize_restore.setObjectName("btn_maximize_restore")
        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
        self.btn_close.setMaximumSize(QtCore.QSize(40, 30))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    image: url(:/20x20/icons/20x20/cil-x.png);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 123, 75);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(161, 145, 88);\n"
"}\n"
"")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_5.addWidget(self.btn_close)
        self.horizontalLayout_2.addWidget(self.frame_btns_right)
        self.verticalLayout_2.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QFrame(self.frame_main)
        self.frame_center.setStyleSheet("")
        self.frame_center.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_left_menu = QtWidgets.QFrame(self.frame_center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet("background-color: rgb(40, 57, 113);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_menus.setMinimumSize(QtCore.QSize(0, 210))
        self.frame_menus.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menus.setObjectName("frame_menus")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_menus)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_view_page = QtWidgets.QPushButton(self.frame_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_view_page.sizePolicy().hasHeightForWidth())
        self.btn_view_page.setSizePolicy(sizePolicy)
        self.btn_view_page.setMinimumSize(QtCore.QSize(70, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_view_page.setFont(font)
        self.btn_view_page.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_view_page.setStyleSheet("QPushButton {\n"
"    image: url(:/login_logo/icons/team-5701 (1).png);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 123, 75);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(161, 145, 88);\n"
"}")
        self.btn_view_page.setText("")
        self.btn_view_page.setObjectName("btn_view_page")
        self.verticalLayout_8.addWidget(self.btn_view_page)
        self.btn_add_page = QtWidgets.QPushButton(self.frame_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_page.sizePolicy().hasHeightForWidth())
        self.btn_add_page.setSizePolicy(sizePolicy)
        self.btn_add_page.setMinimumSize(QtCore.QSize(70, 60))
        self.btn_add_page.setMaximumSize(QtCore.QSize(16777215, 60))
        self.btn_add_page.setStyleSheet("QPushButton {\n"
"    image: url(:/20x20/icons/20x20/cil-plus.png);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 123, 75);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(161, 145, 88);\n"
"}")
        self.btn_add_page.setText("")
        self.btn_add_page.setObjectName("btn_add_page")
        self.verticalLayout_8.addWidget(self.btn_add_page)
        self.btn_update_page = QtWidgets.QPushButton(self.frame_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_update_page.sizePolicy().hasHeightForWidth())
        self.btn_update_page.setSizePolicy(sizePolicy)
        self.btn_update_page.setMinimumSize(QtCore.QSize(70, 60))
        self.btn_update_page.setMaximumSize(QtCore.QSize(16777215, 60))
        self.btn_update_page.setStyleSheet("QPushButton {\n"
"    \n"
"    image: url(:/login_logo/icons/arrows-refresh-2847.png);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 123, 75);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(161, 145, 88);\n"
"}")
        self.btn_update_page.setText("")
        self.btn_update_page.setObjectName("btn_update_page")
        self.verticalLayout_8.addWidget(self.btn_update_page)
        self.verticalLayout_9.addWidget(self.frame_menus)
        self.frame_extra = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_extra.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_extra.setStyleSheet("width: 70;\n"
"height: 60")
        self.frame_extra.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_extra.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_extra.setObjectName("frame_extra")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_extra)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_9.addWidget(self.frame_extra)
        self.frame_extra_menus = QtWidgets.QFrame(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy)
        self.frame_extra_menus.setMinimumSize(QtCore.QSize(70, 60))
        self.frame_extra_menus.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_extra_menus.setStyleSheet("background-color: transparent;")
        self.frame_extra_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_extra_menus.setObjectName("frame_extra_menus")
        self.layout_menu_bottom_2 = QtWidgets.QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom_2.setContentsMargins(0, 0, 0, 0)
        self.layout_menu_bottom_2.setSpacing(0)
        self.layout_menu_bottom_2.setObjectName("layout_menu_bottom_2")
        self.btn_logout = QtWidgets.QPushButton(self.frame_extra_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QtCore.QSize(70, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.btn_logout.setFont(font)
        self.btn_logout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_logout.setStyleSheet("QPushButton {    \n"
"    image: url(:/16x16/icons/16x16/cil-account-logout.png);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 123, 75);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(161, 145, 88);\n"
"}")
        self.btn_logout.setText("")
        self.btn_logout.setObjectName("btn_logout")
        self.layout_menu_bottom_2.addWidget(self.btn_logout)
        self.verticalLayout_9.addWidget(self.frame_extra_menus)
        self.horizontalLayout.addWidget(self.frame_left_menu)
        self.pages_widgets = QtWidgets.QStackedWidget(self.frame_center)
        self.pages_widgets.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pages_widgets.setObjectName("pages_widgets")
        self.page_view_users = QtWidgets.QWidget()
        self.page_view_users.setObjectName("page_view_users")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_view_users)
        self.verticalLayout_6.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_view_users = QtWidgets.QFrame(self.page_view_users)
        self.frame_view_users.setMinimumSize(QtCore.QSize(500, 65))
        self.frame_view_users.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_view_users.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_view_users.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_view_users.setObjectName("frame_view_users")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_view_users)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_view_user = QtWidgets.QLabel(self.frame_view_users)
        self.label_view_user.setMinimumSize(QtCore.QSize(0, 50))
        self.label_view_user.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_view_user.setFont(font)
        self.label_view_user.setStyleSheet("color: rgb(40, 57, 113);\n"
"background-color: transparent;\n"
"border: none;")
        self.label_view_user.setTextFormat(QtCore.Qt.RichText)
        self.label_view_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_view_user.setObjectName("label_view_user")
        self.verticalLayout_4.addWidget(self.label_view_user)
        self.frame_15 = QtWidgets.QFrame(self.frame_view_users)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 5))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 5))
        self.frame_15.setStyleSheet("background-color: rgb(161, 145, 88);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_4.addWidget(self.frame_15)
        self.verticalLayout_6.addWidget(self.frame_view_users)
        self.frame_view_table = QtWidgets.QFrame(self.page_view_users)
        self.frame_view_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_view_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_view_table.setLineWidth(1)
        self.frame_view_table.setObjectName("frame_view_table")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_view_table)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_11 = QtWidgets.QFrame(self.frame_view_table)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section {\n"
"background-color: rgb(40, 57, 113);\n"
"border: 1px solid rgb(161, 145, 88);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QTableView{\n"
"gridline-color: rgb(161, 145, 88);\n"
"border-color: rgb(161, 145, 88);\n"
"color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(161, 145, 88);\n"
"}")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_view_table)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_12)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 5))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 5))
        self.frame_3.setStyleSheet("background-color: rgb(161, 145, 88);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_10 = QtWidgets.QFrame(self.frame_12)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 15))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 15))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_8 = QtWidgets.QFrame(self.frame_12)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_view_user_3 = QtWidgets.QLabel(self.frame_8)
        self.label_view_user_3.setMinimumSize(QtCore.QSize(200, 40))
        self.label_view_user_3.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_view_user_3.setFont(font)
        self.label_view_user_3.setStyleSheet("color: rgb(40, 57, 113);\n"
"background-color: transparent;\n"
"border: none;")
        self.label_view_user_3.setTextFormat(QtCore.Qt.RichText)
        self.label_view_user_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_view_user_3.setObjectName("label_view_user_3")
        self.horizontalLayout_3.addWidget(self.label_view_user_3)
        self.frame_14 = QtWidgets.QFrame(self.frame_8)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_3.addWidget(self.frame_14)
        self.student_id_delete = QtWidgets.QLineEdit(self.frame_8)
        self.student_id_delete.setMinimumSize(QtCore.QSize(200, 40))
        self.student_id_delete.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.student_id_delete.setFont(font)
        self.student_id_delete.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.student_id_delete.setText("")
        self.student_id_delete.setObjectName("student_id_delete")
        self.horizontalLayout_3.addWidget(self.student_id_delete)
        self.btn_delete = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        self.btn_delete.setMinimumSize(QtCore.QSize(45, 45))
        self.btn_delete.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("QPushButton{\n"
"    image: url(:/login_logo/icons/trash-347.png);\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(64, 92, 182)\n"
"}\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(40, 57, 113);\n"
"}")
        self.btn_delete.setText("")
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_3.addWidget(self.btn_delete)
        self.frame_16 = QtWidgets.QFrame(self.frame_8)
        self.frame_16.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_16.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.status_2 = QtWidgets.QLabel(self.frame_16)
        self.status_2.setText("")
        self.status_2.setObjectName("status_2")
        self.verticalLayout_10.addWidget(self.status_2)
        self.horizontalLayout_3.addWidget(self.frame_16)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.verticalLayout_6.addWidget(self.frame_view_table)
        self.pages_widgets.addWidget(self.page_view_users)
        self.page_add_user = QtWidgets.QWidget()
        self.page_add_user.setObjectName("page_add_user")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_add_user)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_2 = QtWidgets.QFrame(self.page_add_user)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMinimumSize(QtCore.QSize(180, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 530))
        self.frame_5.setMaximumSize(QtCore.QSize(530, 16777215))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setMinimumSize(QtCore.QSize(0, 100))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(40, 57, 113);\n"
"background-color: transparent;\n"
"border: none;")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(530, 100))
        self.frame_6.setMaximumSize(QtCore.QSize(530, 100))
        self.frame_6.setStyleSheet("image: url(:/login_logo/icons/add-user-302.png)\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_13.addWidget(self.frame_6)
        self.frame_17 = QtWidgets.QFrame(self.frame_5)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.firstname = QtWidgets.QLineEdit(self.frame_17)
        self.firstname.setMinimumSize(QtCore.QSize(245, 40))
        self.firstname.setMaximumSize(QtCore.QSize(245, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.firstname.setFont(font)
        self.firstname.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.firstname.setText("")
        self.firstname.setObjectName("firstname")
        self.horizontalLayout_7.addWidget(self.firstname)
        self.lastname = QtWidgets.QLineEdit(self.frame_17)
        self.lastname.setMinimumSize(QtCore.QSize(245, 40))
        self.lastname.setMaximumSize(QtCore.QSize(245, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lastname.setFont(font)
        self.lastname.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.lastname.setText("")
        self.lastname.setObjectName("lastname")
        self.horizontalLayout_7.addWidget(self.lastname)
        self.verticalLayout_13.addWidget(self.frame_17)
        self.frame_19 = QtWidgets.QFrame(self.frame_5)
        self.frame_19.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.student_id = QtWidgets.QLineEdit(self.frame_19)
        self.student_id.setMinimumSize(QtCore.QSize(245, 40))
        self.student_id.setMaximumSize(QtCore.QSize(245, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.student_id.setFont(font)
        self.student_id.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.student_id.setText("")
        self.student_id.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.student_id.setObjectName("student_id")
        self.horizontalLayout_9.addWidget(self.student_id)
        self.course_year = QtWidgets.QLineEdit(self.frame_19)
        self.course_year.setMinimumSize(QtCore.QSize(245, 40))
        self.course_year.setMaximumSize(QtCore.QSize(245, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.course_year.setFont(font)
        self.course_year.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.course_year.setText("")
        self.course_year.setObjectName("course_year")
        self.horizontalLayout_9.addWidget(self.course_year)
        self.verticalLayout_13.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_5)
        self.frame_20.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_24 = QtWidgets.QFrame(self.frame_20)
        self.frame_24.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_24.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_24.setStyleSheet("image: url(:/login_logo/icons/pin-49.png);\n"
"background-color: transparent")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_11.addWidget(self.frame_24)
        self.address = QtWidgets.QLineEdit(self.frame_20)
        self.address.setMinimumSize(QtCore.QSize(200, 40))
        self.address.setMaximumSize(QtCore.QSize(145, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.address.setFont(font)
        self.address.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.address.setText("")
        self.address.setObjectName("address")
        self.horizontalLayout_11.addWidget(self.address)
        self.frame_13 = QtWidgets.QFrame(self.frame_20)
        self.frame_13.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_13.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_13.setStyleSheet("image: url(:/login_logo/icons/event-calendar-597 (1).png);\n"
"background-color: transparent")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11.addWidget(self.frame_13)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_20)
        self.dateEdit.setMinimumSize(QtCore.QSize(200, 40))
        self.dateEdit.setMaximumSize(QtCore.QSize(145, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("border: 2px solid rgb(40, 57, 113);\n"
"color: rgb(0, 0, 0);\n"
"background-color: transparent;")
        self.dateEdit.setWrapping(False)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_11.addWidget(self.dateEdit)
        self.verticalLayout_13.addWidget(self.frame_20)
        self.frame_18 = QtWidgets.QFrame(self.frame_5)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_18.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_18)
        self.frame_7.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_7.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_7.setStyleSheet("image: url(:/login_logo/icons/message-324.png);\n"
"background-color: transparent")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8.addWidget(self.frame_7)
        self.email = QtWidgets.QLineEdit(self.frame_18)
        self.email.setMinimumSize(QtCore.QSize(200, 40))
        self.email.setMaximumSize(QtCore.QSize(145, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.email.setText("")
        self.email.setObjectName("email")
        self.horizontalLayout_8.addWidget(self.email)
        self.frame_9 = QtWidgets.QFrame(self.frame_18)
        self.frame_9.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_9.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_9.setStyleSheet("image: url(:/login_logo/icons/mobile-phone-697.png);\n"
"background-color: transparent")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8.addWidget(self.frame_9)
        self.mobile_no = QtWidgets.QLineEdit(self.frame_18)
        self.mobile_no.setMinimumSize(QtCore.QSize(200, 40))
        self.mobile_no.setMaximumSize(QtCore.QSize(145, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.mobile_no.setFont(font)
        self.mobile_no.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.mobile_no.setText("")
        self.mobile_no.setObjectName("mobile_no")
        self.horizontalLayout_8.addWidget(self.mobile_no)
        self.verticalLayout_13.addWidget(self.frame_18)
        self.frame_25 = QtWidgets.QFrame(self.frame_5)
        self.frame_25.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_25.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_13.addWidget(self.frame_26)
        self.notif = QtWidgets.QLabel(self.frame_25)
        self.notif.setMinimumSize(QtCore.QSize(300, 25))
        self.notif.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.notif.setFont(font)
        self.notif.setText("")
        self.notif.setAlignment(QtCore.Qt.AlignCenter)
        self.notif.setObjectName("notif")
        self.horizontalLayout_13.addWidget(self.notif)
        self.frame_27 = QtWidgets.QFrame(self.frame_25)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_13.addWidget(self.frame_27)
        self.verticalLayout_13.addWidget(self.frame_25)
        self.frame_21 = QtWidgets.QFrame(self.frame_5)
        self.frame_21.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_12.addWidget(self.frame_22)
        self.btn_create = QtWidgets.QPushButton(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create.sizePolicy().hasHeightForWidth())
        self.btn_create.setSizePolicy(sizePolicy)
        self.btn_create.setMinimumSize(QtCore.QSize(200, 40))
        self.btn_create.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.btn_create.setFont(font)
        self.btn_create.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"    border-radius: 5px;\n"
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
        self.btn_create.setObjectName("btn_create")
        self.horizontalLayout_12.addWidget(self.btn_create)
        self.frame_23 = QtWidgets.QFrame(self.frame_21)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_12.addWidget(self.frame_23)
        self.verticalLayout_13.addWidget(self.frame_21)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(180, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.verticalLayout_14.addWidget(self.frame_2)
        self.pages_widgets.addWidget(self.page_add_user)
        self.page_update_user = QtWidgets.QWidget()
        self.page_update_user.setObjectName("page_update_user")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_update_user)
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_28 = QtWidgets.QFrame(self.page_update_user)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_29.setFont(font)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_36 = QtWidgets.QFrame(self.frame_29)
        self.frame_36.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_36.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_36)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_view_user_2 = QtWidgets.QLabel(self.frame_36)
        self.label_view_user_2.setMinimumSize(QtCore.QSize(150, 40))
        self.label_view_user_2.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_view_user_2.setFont(font)
        self.label_view_user_2.setStyleSheet("color: rgb(40, 57, 113);\n"
"background-color: transparent;\n"
"border: none;")
        self.label_view_user_2.setTextFormat(QtCore.Qt.RichText)
        self.label_view_user_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_view_user_2.setObjectName("label_view_user_2")
        self.horizontalLayout_31.addWidget(self.label_view_user_2)
        self.frame_60 = QtWidgets.QFrame(self.frame_36)
        self.frame_60.setMinimumSize(QtCore.QSize(240, 40))
        self.frame_60.setMaximumSize(QtCore.QSize(240, 40))
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_60)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.horizontalLayout_31.addWidget(self.frame_60)
        self.frame_62 = QtWidgets.QFrame(self.frame_36)
        self.frame_62.setMinimumSize(QtCore.QSize(240, 40))
        self.frame_62.setMaximumSize(QtCore.QSize(240, 40))
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_62)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.horizontalLayout_31.addWidget(self.frame_62)
        self.frame_61 = QtWidgets.QFrame(self.frame_36)
        self.frame_61.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_61.setMaximumSize(QtCore.QSize(150, 40))
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_61)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.horizontalLayout_31.addWidget(self.frame_61)
        self.verticalLayout_12.addWidget(self.frame_36)
        self.frame_30 = QtWidgets.QFrame(self.frame_29)
        self.frame_30.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_59 = QtWidgets.QFrame(self.frame_30)
        self.frame_59.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_59.setMaximumSize(QtCore.QSize(150, 40))
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.horizontalLayout_15.addWidget(self.frame_59)
        self.student_id_2 = QtWidgets.QLineEdit(self.frame_30)
        self.student_id_2.setMinimumSize(QtCore.QSize(240, 40))
        self.student_id_2.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.student_id_2.setFont(font)
        self.student_id_2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.student_id_2.setText("")
        self.student_id_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.student_id_2.setObjectName("student_id_2")
        self.horizontalLayout_15.addWidget(self.student_id_2)
        self.btn_load = QtWidgets.QPushButton(self.frame_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load.sizePolicy().hasHeightForWidth())
        self.btn_load.setSizePolicy(sizePolicy)
        self.btn_load.setMinimumSize(QtCore.QSize(150, 40))
        self.btn_load.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.btn_load.setFont(font)
        self.btn_load.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"    border-radius: 5px;\n"
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
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout_15.addWidget(self.btn_load)
        self.notif_3 = QtWidgets.QLabel(self.frame_30)
        self.notif_3.setMinimumSize(QtCore.QSize(240, 45))
        self.notif_3.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.notif_3.setFont(font)
        self.notif_3.setText("")
        self.notif_3.setObjectName("notif_3")
        self.horizontalLayout_15.addWidget(self.notif_3)
        self.verticalLayout_12.addWidget(self.frame_30)
        self.frame_31 = QtWidgets.QFrame(self.frame_29)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_31.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_41 = QtWidgets.QFrame(self.frame_31)
        self.frame_41.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_41.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_14.addWidget(self.frame_41)
        self.firstname_2 = QtWidgets.QLineEdit(self.frame_31)
        self.firstname_2.setMinimumSize(QtCore.QSize(240, 40))
        self.firstname_2.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.firstname_2.setFont(font)
        self.firstname_2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.firstname_2.setText("")
        self.firstname_2.setObjectName("firstname_2")
        self.horizontalLayout_14.addWidget(self.firstname_2)
        self.lastname_2 = QtWidgets.QLineEdit(self.frame_31)
        self.lastname_2.setMinimumSize(QtCore.QSize(240, 40))
        self.lastname_2.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lastname_2.setFont(font)
        self.lastname_2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.lastname_2.setText("")
        self.lastname_2.setObjectName("lastname_2")
        self.horizontalLayout_14.addWidget(self.lastname_2)
        self.frame_37 = QtWidgets.QFrame(self.frame_31)
        self.frame_37.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_37.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.horizontalLayout_14.addWidget(self.frame_37)
        self.verticalLayout_12.addWidget(self.frame_31)
        self.frame_32 = QtWidgets.QFrame(self.frame_29)
        self.frame_32.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_42 = QtWidgets.QFrame(self.frame_32)
        self.frame_42.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_42.setMaximumSize(QtCore.QSize(150, 40))
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.horizontalLayout_16.addWidget(self.frame_42)
        self.course_year_2 = QtWidgets.QLineEdit(self.frame_32)
        self.course_year_2.setMinimumSize(QtCore.QSize(240, 40))
        self.course_year_2.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.course_year_2.setFont(font)
        self.course_year_2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.course_year_2.setText("")
        self.course_year_2.setObjectName("course_year_2")
        self.horizontalLayout_16.addWidget(self.course_year_2)
        self.frame_38 = QtWidgets.QFrame(self.frame_32)
        self.frame_38.setMinimumSize(QtCore.QSize(240, 40))
        self.frame_38.setMaximumSize(QtCore.QSize(240, 40))
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_16.addWidget(self.frame_38)
        self.frame_39 = QtWidgets.QFrame(self.frame_32)
        self.frame_39.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_39.setMaximumSize(QtCore.QSize(150, 40))
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_16.addWidget(self.frame_39)
        self.verticalLayout_12.addWidget(self.frame_32)
        self.frame_33 = QtWidgets.QFrame(self.frame_29)
        self.frame_33.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_33.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_33)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_43 = QtWidgets.QFrame(self.frame_33)
        self.frame_43.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_43.setMaximumSize(QtCore.QSize(150, 40))
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_17.addWidget(self.frame_43)
        self.frame_50 = QtWidgets.QFrame(self.frame_33)
        self.frame_50.setMinimumSize(QtCore.QSize(245, 45))
        self.frame_50.setMaximumSize(QtCore.QSize(245, 45))
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_50)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_45 = QtWidgets.QFrame(self.frame_50)
        self.frame_45.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_45.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_45.setStyleSheet("image: url(:/login_logo/icons/pin-49.png);\n"
"background-color: transparent")
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.horizontalLayout_21.addWidget(self.frame_45)
        self.address_2 = QtWidgets.QLineEdit(self.frame_50)
        self.address_2.setMinimumSize(QtCore.QSize(200, 40))
        self.address_2.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.address_2.setFont(font)
        self.address_2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.address_2.setText("")
        self.address_2.setObjectName("address_2")
        self.horizontalLayout_21.addWidget(self.address_2)
        self.horizontalLayout_17.addWidget(self.frame_50)
        self.frame_40 = QtWidgets.QFrame(self.frame_33)
        self.frame_40.setMinimumSize(QtCore.QSize(245, 45))
        self.frame_40.setMaximumSize(QtCore.QSize(245, 45))
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_40)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_46 = QtWidgets.QFrame(self.frame_40)
        self.frame_46.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_46.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_46.setStyleSheet("image: url(:/login_logo/icons/event-calendar-597 (1).png);\n"
"background-color: transparent")
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout_20.addWidget(self.frame_46)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_40)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(200, 40))
        self.dateEdit_2.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet("border: 2px solid rgb(40, 57, 113);\n"
"color: rgb(0, 0, 0);\n"
"background-color: transparent;")
        self.dateEdit_2.setWrapping(False)
        self.dateEdit_2.setFrame(True)
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_2.setAccelerated(False)
        self.dateEdit_2.setProperty("showGroupSeparator", False)
        self.dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEdit_2.setCalendarPopup(False)
        self.dateEdit_2.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_20.addWidget(self.dateEdit_2)
        self.horizontalLayout_17.addWidget(self.frame_40)
        self.frame_49 = QtWidgets.QFrame(self.frame_33)
        self.frame_49.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_49.setMaximumSize(QtCore.QSize(150, 40))
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.horizontalLayout_17.addWidget(self.frame_49)
        self.verticalLayout_12.addWidget(self.frame_33)
        self.frame_34 = QtWidgets.QFrame(self.frame_29)
        self.frame_34.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_34.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_55 = QtWidgets.QFrame(self.frame_34)
        self.frame_55.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_55.setMaximumSize(QtCore.QSize(150, 40))
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.horizontalLayout_18.addWidget(self.frame_55)
        self.frame_52 = QtWidgets.QFrame(self.frame_34)
        self.frame_52.setMinimumSize(QtCore.QSize(245, 45))
        self.frame_52.setMaximumSize(QtCore.QSize(245, 45))
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_52)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_48 = QtWidgets.QFrame(self.frame_52)
        self.frame_48.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_48.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_48.setStyleSheet("image: url(:/login_logo/icons/message-324.png);\n"
"background-color: transparent")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.horizontalLayout_23.addWidget(self.frame_48)
        self.email_2 = QtWidgets.QLineEdit(self.frame_52)
        self.email_2.setMinimumSize(QtCore.QSize(200, 40))
        self.email_2.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.email_2.setFont(font)
        self.email_2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.email_2.setText("")
        self.email_2.setObjectName("email_2")
        self.horizontalLayout_23.addWidget(self.email_2)
        self.horizontalLayout_18.addWidget(self.frame_52)
        self.frame_51 = QtWidgets.QFrame(self.frame_34)
        self.frame_51.setMinimumSize(QtCore.QSize(245, 45))
        self.frame_51.setMaximumSize(QtCore.QSize(245, 45))
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_51)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_47 = QtWidgets.QFrame(self.frame_51)
        self.frame_47.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_47.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_47.setStyleSheet("image: url(:/login_logo/icons/mobile-phone-697.png);\n"
"background-color: transparent")
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.horizontalLayout_22.addWidget(self.frame_47)
        self.mobile_no_2 = QtWidgets.QLineEdit(self.frame_51)
        self.mobile_no_2.setMinimumSize(QtCore.QSize(200, 40))
        self.mobile_no_2.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.mobile_no_2.setFont(font)
        self.mobile_no_2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
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
        self.mobile_no_2.setText("")
        self.mobile_no_2.setObjectName("mobile_no_2")
        self.horizontalLayout_22.addWidget(self.mobile_no_2)
        self.horizontalLayout_18.addWidget(self.frame_51)
        self.btn_update = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy)
        self.btn_update.setMinimumSize(QtCore.QSize(150, 40))
        self.btn_update.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(40, 57, 113);\n"
"    border-radius: 5px;\n"
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
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_18.addWidget(self.btn_update)
        self.verticalLayout_12.addWidget(self.frame_34)
        self.frame_35 = QtWidgets.QFrame(self.frame_29)
        self.frame_35.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_35.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.frame_44 = QtWidgets.QFrame(self.frame_35)
        self.frame_44.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_44.setMaximumSize(QtCore.QSize(150, 40))
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.horizontalLayout_27.addWidget(self.frame_44)
        self.frame_53 = QtWidgets.QFrame(self.frame_35)
        self.frame_53.setMinimumSize(QtCore.QSize(240, 40))
        self.frame_53.setMaximumSize(QtCore.QSize(240, 40))
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_53)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_27.addWidget(self.frame_53)
        self.frame_54 = QtWidgets.QFrame(self.frame_35)
        self.frame_54.setMinimumSize(QtCore.QSize(150, 40))
        self.frame_54.setMaximumSize(QtCore.QSize(150, 40))
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_54)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_27.addWidget(self.frame_54)
        self.notif_2 = QtWidgets.QLabel(self.frame_35)
        self.notif_2.setMinimumSize(QtCore.QSize(240, 40))
        self.notif_2.setMaximumSize(QtCore.QSize(240, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.notif_2.setFont(font)
        self.notif_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.notif_2.setText("")
        self.notif_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.notif_2.setObjectName("notif_2")
        self.horizontalLayout_27.addWidget(self.notif_2)
        self.verticalLayout_12.addWidget(self.frame_35)
        self.horizontalLayout_24.addWidget(self.frame_29)
        self.verticalLayout_15.addWidget(self.frame_28)
        self.pages_widgets.addWidget(self.page_update_user)
        self.horizontalLayout.addWidget(self.pages_widgets)
        self.verticalLayout_2.addWidget(self.frame_center)
        self.frame_bottom = QtWidgets.QFrame(self.frame_main)
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 15))
        self.frame_bottom.setStyleSheet("background-color: rgb(40, 57, 113);")
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_bottom)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label = QtWidgets.QLabel(self.frame_bottom)
        self.label.setObjectName("label")
        self.verticalLayout_21.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_bottom)
        self.verticalLayout.addWidget(self.frame_main)
        Main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_window)
        self.pages_widgets.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main_window)

    def retranslateUi(self, Main_window):
        _translate = QtCore.QCoreApplication.translate
        Main_window.setWindowTitle(_translate("Main_window", "MainWindow"))
        self.label_title_bar_top.setText(_translate("Main_window", "ADMIN DASHBOARD"))
        self.label_view_user.setText(_translate("Main_window", "<html><head/><body><p><span style=\" font-weight:600;\">VIEW</span> USERS</p></body></html>"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Main_window", "Student ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Main_window", "First name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Main_window", "Last name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Main_window", "Address"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Main_window", "Birthdate"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Main_window", "Course and Year"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Main_window", "Email"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Main_window", "Contact No."))
        self.label_view_user_3.setText(_translate("Main_window", "<strong>DELETE</strong> USER"))
        self.student_id_delete.setPlaceholderText(_translate("Main_window", "Student ID"))
        self.label_6.setText(_translate("Main_window", "<html><head/><body><p><span style=\" font-weight:600;\">  CREATE ACCOUNT</span></p></body></html>"))
        self.firstname.setPlaceholderText(_translate("Main_window", "First Name"))
        self.lastname.setPlaceholderText(_translate("Main_window", "Last Name"))
        self.student_id.setPlaceholderText(_translate("Main_window", "Student ID"))
        self.course_year.setPlaceholderText(_translate("Main_window", "Course and Year"))
        self.address.setPlaceholderText(_translate("Main_window", "Address"))
        self.dateEdit.setDisplayFormat(_translate("Main_window", "yyyy/MM/dd"))
        self.email.setPlaceholderText(_translate("Main_window", "Email"))
        self.mobile_no.setPlaceholderText(_translate("Main_window", "Mobile No."))
        self.btn_create.setText(_translate("Main_window", "Create"))
        self.label_view_user_2.setText(_translate("Main_window", "<html><head/><body><p><span style=\" font-weight:600;\">UPDATE</span> USER</p></body></html>"))
        self.student_id_2.setPlaceholderText(_translate("Main_window", "Student ID"))
        self.btn_load.setText(_translate("Main_window", "Load"))
        self.firstname_2.setPlaceholderText(_translate("Main_window", "First Name"))
        self.lastname_2.setPlaceholderText(_translate("Main_window", "Last Name"))
        self.course_year_2.setPlaceholderText(_translate("Main_window", "Course and Year"))
        self.address_2.setPlaceholderText(_translate("Main_window", "Address"))
        self.dateEdit_2.setDisplayFormat(_translate("Main_window", "yyyy/MM/dd"))
        self.email_2.setPlaceholderText(_translate("Main_window", "Email"))
        self.mobile_no_2.setPlaceholderText(_translate("Main_window", "Mobile No."))
        self.btn_update.setText(_translate("Main_window", "Update"))
        self.label.setText(_translate("Main_window", "None"))

import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_window = QtWidgets.QMainWindow()
    ui = Ui_Main_window()
    ui.setupUi(Main_window)
    Main_window.show()
    sys.exit(app.exec_())
