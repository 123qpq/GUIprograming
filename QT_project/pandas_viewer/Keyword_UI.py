# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyword.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1002, 582)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_frame = QFrame(self.centralwidget)
        self.Main_frame.setObjectName(u"Main_frame")
        self.Main_frame.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 14, 173, 255), stop:1 rgba(168, 13, 112, 255));\n"
"border-radius: 8px;\n"
"")
        self.Main_frame.setFrameShape(QFrame.StyledPanel)
        self.Main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.Main_frame)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 30))
        self.header.setMaximumSize(QSize(16777215, 30))
        self.header.setStyleSheet(u"background-color : rgb(13, 11, 67);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.name_bar = QLabel(self.header)
        self.name_bar.setObjectName(u"name_bar")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.name_bar.setFont(font)
        self.name_bar.setStyleSheet(u"color:rgb(255,255, 255);")
        self.name_bar.setMargin(0)

        self.horizontalLayout_3.addWidget(self.name_bar)

        self.setting = QFrame(self.header)
        self.setting.setObjectName(u"setting")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting.sizePolicy().hasHeightForWidth())
        self.setting.setSizePolicy(sizePolicy)
        self.setting.setMinimumSize(QSize(100, 0))
        self.setting.setMaximumSize(QSize(100, 16777215))
        self.setting.setFrameShape(QFrame.StyledPanel)
        self.setting.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.setting)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.minimize = QPushButton(self.setting)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(16, 16))
        self.minimize.setMaximumSize(QSize(16, 16))
        self.minimize.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:3px;\n"
"background-color:rgb(255, 189, 57);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255, 189, 57, 150);\n"
"}")

        self.horizontalLayout_4.addWidget(self.minimize)

        self.maximize = QPushButton(self.setting)
        self.maximize.setObjectName(u"maximize")
        self.maximize.setMinimumSize(QSize(16, 16))
        self.maximize.setMaximumSize(QSize(16, 16))
        self.maximize.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:3px;\n"
"background-color:rgb(115, 255, 131);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(115, 255, 131, 150);\n"
"}")

        self.horizontalLayout_4.addWidget(self.maximize)

        self.close = QPushButton(self.setting)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(16, 16))
        self.close.setMaximumSize(QSize(16, 16))
        self.close.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:3px;\n"
"background-color:rgb(255, 70, 70);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255, 70, 70, 150);\n"
"}")

        self.horizontalLayout_4.addWidget(self.close)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.setting, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.View_frame = QFrame(self.Main_frame)
        self.View_frame.setObjectName(u"View_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.View_frame.sizePolicy().hasHeightForWidth())
        self.View_frame.setSizePolicy(sizePolicy1)
        self.View_frame.setStyleSheet(u"")
        self.View_frame.setFrameShape(QFrame.StyledPanel)
        self.View_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.View_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.params = QFrame(self.View_frame)
        self.params.setObjectName(u"params")
        self.params.setMinimumSize(QSize(0, 30))
        self.params.setMaximumSize(QSize(16777215, 30))
        self.params.setStyleSheet(u"background-color : rgb(13, 11, 67);\n"
"")
        self.params.setFrameShape(QFrame.StyledPanel)
        self.params.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.params)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, 0)
        self.keyword = QLabel(self.params)
        self.keyword.setObjectName(u"keyword")
        self.keyword.setMinimumSize(QSize(50, 20))
        self.keyword.setMaximumSize(QSize(70, 20))
        font1 = QFont()
        font1.setBold(True)
        self.keyword.setFont(font1)
        self.keyword.setStyleSheet(u"color:rgb(255,255, 255);")
        self.keyword.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.keyword)

        self.box_frame_3 = QFrame(self.params)
        self.box_frame_3.setObjectName(u"box_frame_3")
        self.box_frame_3.setMinimumSize(QSize(100, 20))
        self.box_frame_3.setMaximumSize(QSize(100, 20))
        self.box_frame_3.setStyleSheet(u"background-color : rgb(244, 236, 254);")
        self.box_frame_3.setFrameShape(QFrame.StyledPanel)
        self.box_frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.box_frame_3)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.col_box_3 = QComboBox(self.box_frame_3)
        self.col_box_3.addItem("")
        self.col_box_3.setObjectName(u"col_box_3")
        self.col_box_3.setMinimumSize(QSize(100, 20))
        self.col_box_3.setMaximumSize(QSize(100, 20))
        font2 = QFont()
        font2.setPointSize(9)
        self.col_box_3.setFont(font2)
        self.col_box_3.setStyleSheet(u"background-color : rgb(244, 236, 254);")

        self.gridLayout_11.addWidget(self.col_box_3, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.box_frame_3)

        self.keyword_2 = QLabel(self.params)
        self.keyword_2.setObjectName(u"keyword_2")
        self.keyword_2.setMinimumSize(QSize(50, 20))
        self.keyword_2.setMaximumSize(QSize(70, 20))
        self.keyword_2.setFont(font1)
        self.keyword_2.setStyleSheet(u"color:rgb(255,255, 255);")
        self.keyword_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.keyword_2)

        self.keyword_edit = QLineEdit(self.params)
        self.keyword_edit.setObjectName(u"keyword_edit")
        self.keyword_edit.setMinimumSize(QSize(100, 20))
        self.keyword_edit.setMaximumSize(QSize(200, 20))
        self.keyword_edit.setStyleSheet(u"background-color : rgb(244, 236, 254);")

        self.horizontalLayout_2.addWidget(self.keyword_edit)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.SearchBtn = QPushButton(self.params)
        self.SearchBtn.setObjectName(u"SearchBtn")
        self.SearchBtn.setMinimumSize(QSize(100, 20))
        self.SearchBtn.setMaximumSize(QSize(100, 20))
        self.SearchBtn.setFont(font1)
        self.SearchBtn.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius : 10px;\n"
"color:rgb(255,255, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(237, 81, 72, 255), stop:1 rgba(255, 65, 168, 255));\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255, 255, 150);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(237, 81, 72, 255), stop:1 rgba(255, 65, 168, 255));\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.SearchBtn, 0, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.params)

        self.filter = QFrame(self.View_frame)
        self.filter.setObjectName(u"filter")
        self.filter.setMinimumSize(QSize(0, 30))
        self.filter.setMaximumSize(QSize(16777215, 30))
        self.filter.setStyleSheet(u"background-color : rgb(13, 11, 67);")
        self.filter.setFrameShape(QFrame.StyledPanel)
        self.filter.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.filter)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(15)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(10, 3, 20, 3)
        self.fframe = QFrame(self.filter)
        self.fframe.setObjectName(u"fframe")
        self.fframe.setStyleSheet(u"background-color: rgb(7, 6, 35);\n"
"")
        self.fframe.setFrameShape(QFrame.StyledPanel)
        self.fframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.fframe)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, 0)
        self.label_1 = QLabel(self.fframe)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(80, 20))
        self.label_1.setMaximumSize(QSize(80, 20))
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"color:rgb(255,255, 255);\n"
"border-style:None;")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_1)

        self.box_frame = QFrame(self.fframe)
        self.box_frame.setObjectName(u"box_frame")
        self.box_frame.setMinimumSize(QSize(100, 20))
        self.box_frame.setMaximumSize(QSize(100, 20))
        self.box_frame.setStyleSheet(u"background-color : rgb(244, 236, 254);")
        self.box_frame.setFrameShape(QFrame.StyledPanel)
        self.box_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.box_frame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.col_box = QComboBox(self.box_frame)
        self.col_box.addItem("")
        self.col_box.setObjectName(u"col_box")
        self.col_box.setMinimumSize(QSize(100, 20))
        self.col_box.setMaximumSize(QSize(100, 20))
        self.col_box.setFont(font2)
        self.col_box.setStyleSheet(u"background-color : rgb(244, 236, 254);")

        self.gridLayout_7.addWidget(self.col_box, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.box_frame)

        self.label_2 = QLabel(self.fframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 20))
        self.label_2.setMaximumSize(QSize(50, 20))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:rgb(255,255, 255);\n"
"background-color: rgb(7, 6, 35);\n"
"border-style:None;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.condi1 = QLineEdit(self.fframe)
        self.condi1.setObjectName(u"condi1")
        self.condi1.setMinimumSize(QSize(50, 20))
        self.condi1.setMaximumSize(QSize(50, 20))
        self.condi1.setStyleSheet(u"background-color : rgb(244, 236, 254);")

        self.horizontalLayout_5.addWidget(self.condi1)

        self.label_3 = QLabel(self.fframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 20))
        self.label_3.setMaximumSize(QSize(30, 20))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:rgb(255,255, 255);\n"
"background-color: rgb(7, 6, 35);\n"
"border-style:None;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.condi2 = QLineEdit(self.fframe)
        self.condi2.setObjectName(u"condi2")
        self.condi2.setMinimumSize(QSize(49, 20))
        self.condi2.setMaximumSize(QSize(50, 20))
        self.condi2.setStyleSheet(u"background-color : rgb(244, 236, 254);\n"
"border-style:None;")

        self.horizontalLayout_5.addWidget(self.condi2)


        self.gridLayout_5.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.fframe, 0, 0, 1, 1)

        self.fframe_2 = QFrame(self.filter)
        self.fframe_2.setObjectName(u"fframe_2")
        self.fframe_2.setStyleSheet(u"background-color: rgb(7, 6, 35);")
        self.fframe_2.setFrameShape(QFrame.StyledPanel)
        self.fframe_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.fframe_2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, -1, 10, 0)
        self.label_4 = QLabel(self.fframe_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 20))
        self.label_4.setMaximumSize(QSize(80, 20))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:rgb(255,255, 255);\n"
"background-color: rgb(7, 6, 35);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.box_frame_2 = QFrame(self.fframe_2)
        self.box_frame_2.setObjectName(u"box_frame_2")
        self.box_frame_2.setMinimumSize(QSize(100, 20))
        self.box_frame_2.setMaximumSize(QSize(100, 20))
        self.box_frame_2.setStyleSheet(u"background-color : rgb(244, 236, 254);")
        self.box_frame_2.setFrameShape(QFrame.StyledPanel)
        self.box_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.box_frame_2)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.col_box_2 = QComboBox(self.box_frame_2)
        self.col_box_2.addItem("")
        self.col_box_2.setObjectName(u"col_box_2")
        self.col_box_2.setMinimumSize(QSize(100, 20))
        self.col_box_2.setMaximumSize(QSize(100, 20))
        self.col_box_2.setFont(font2)
        self.col_box_2.setStyleSheet(u"background-color : rgb(244, 236, 254);")

        self.gridLayout_10.addWidget(self.col_box_2, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.box_frame_2)

        self.label_5 = QLabel(self.fframe_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 20))
        self.label_5.setMaximumSize(QSize(50, 20))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:rgb(255,255, 255);\n"
"background-color: rgb(7, 6, 35);\n"
"border-style:None;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.condi1_2 = QLineEdit(self.fframe_2)
        self.condi1_2.setObjectName(u"condi1_2")
        self.condi1_2.setMinimumSize(QSize(50, 20))
        self.condi1_2.setMaximumSize(QSize(50, 20))
        self.condi1_2.setStyleSheet(u"background-color : rgb(244, 236, 254);")

        self.horizontalLayout_8.addWidget(self.condi1_2)

        self.label_6 = QLabel(self.fframe_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(30, 20))
        self.label_6.setMaximumSize(QSize(30, 20))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color:rgb(255,255, 255);\n"
"background-color: rgb(7, 6, 35);\n"
"border-style:None;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.condi2_2 = QLineEdit(self.fframe_2)
        self.condi2_2.setObjectName(u"condi2_2")
        self.condi2_2.setMinimumSize(QSize(49, 20))
        self.condi2_2.setMaximumSize(QSize(50, 20))
        self.condi2_2.setStyleSheet(u"background-color : rgb(244, 236, 254);\n"
"border-style:None;")

        self.horizontalLayout_8.addWidget(self.condi2_2)


        self.gridLayout_8.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.fframe_2, 0, 1, 1, 1)

        self.SetBtn = QPushButton(self.filter)
        self.SetBtn.setObjectName(u"SetBtn")
        self.SetBtn.setMinimumSize(QSize(100, 20))
        self.SetBtn.setMaximumSize(QSize(100, 20))
        self.SetBtn.setFont(font1)
        self.SetBtn.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius : 10px;\n"
"color:rgb(255,255, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(237, 81, 72, 255), stop:1 rgba(255, 65, 168, 255));\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255, 255, 150);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(237, 81, 72, 255), stop:1 rgba(255, 65, 168, 255));\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_9.addWidget(self.SetBtn, 0, 2, 1, 1, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.filter)

        self.table = QFrame(self.View_frame)
        self.table.setObjectName(u"table")
        self.table.setFrameShape(QFrame.StyledPanel)
        self.table.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.table)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.table)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color : rgba(13, 11, 67, 180);")

        self.gridLayout_4.addWidget(self.tableWidget, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.table)


        self.verticalLayout.addWidget(self.View_frame)

        self.bottom = QFrame(self.Main_frame)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 25))
        self.bottom.setMaximumSize(QSize(16777215, 25))
        self.bottom.setStyleSheet(u"background-color : rgb(13, 11, 67);")
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.bottom)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.bottom)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:rgba(255,255, 255, 100);")
        self.label.setMargin(20)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.control_size = QFrame(self.bottom)
        self.control_size.setObjectName(u"control_size")
        self.control_size.setMinimumSize(QSize(20, 20))
        self.control_size.setMaximumSize(QSize(20, 20))
        self.control_size.setStyleSheet(u"")
        self.control_size.setFrameShape(QFrame.StyledPanel)
        self.control_size.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.control_size, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.bottom)


        self.gridLayout.addWidget(self.Main_frame, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.name_bar.setText(QCoreApplication.translate("MainWindow", u"kyopark's programe", None))
        self.minimize.setText("")
        self.maximize.setText("")
        self.close.setText("")
        self.keyword.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9 \ud589  : ", None))
        self.col_box_3.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.keyword_2.setText(QCoreApplication.translate("MainWindow", u"search  : ", None))
        self.SearchBtn.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u25cf 1\ucc28 \ud544\ud130  : ", None))
        self.col_box.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc870\uac74 : ", None))
        self.condi1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.condi2.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u25cf 2\ucc28 \ud544\ud130  : ", None))
        self.col_box_2.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uc870\uac74 : ", None))
        self.condi1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.condi2_2.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.SetBtn.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"by. kyopark     -- ver 1.0 --", None))
    # retranslateUi

