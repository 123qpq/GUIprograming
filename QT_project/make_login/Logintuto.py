# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(309, 432)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 290, 410))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 290, 410))
        self.label.setStyleSheet(u"background-color:rgba(15, 30, 41, 240);\n"
"border-radius:10px;")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 210, 250, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(45, 82, 101, 255);\n"
"color:rgb(255, 255,255);\n"
"padding-bottom: 7px;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 260, 250, 30))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(45, 82, 101, 255);\n"
"color:rgb(255, 255,255);\n"
"padding-bottom: 7px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 320, 250, 40))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 30, 180, 150))
        font2 = QFont()
        font2.setPointSize(70)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:rgba(0, 125, 236, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 370, 230, 16))
        self.label_3.setStyleSheet(u"color:rgba(255,255, 255, 150);")
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 291, 30))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.close = QPushButton(self.horizontalLayoutWidget)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(16, 16))
        self.close.setMaximumSize(QSize(16, 16))
        self.close.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color:rgb(255, 70, 70);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255, 70, 70, 150);\n"
"}")

        self.gridLayout.addWidget(self.close, 0, 2, 1, 1)

        self.minimize = QPushButton(self.horizontalLayoutWidget)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(16, 16))
        self.minimize.setMaximumSize(QSize(16, 16))
        self.minimize.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"border-radius:8px;\n"
"background-color:rgb(255, 189, 57);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255, 189, 57, 150);\n"
"}")

        self.gridLayout.addWidget(self.minimize, 0, 1, 1, 1)

        self.name_bar = QLabel(self.horizontalLayoutWidget)
        self.name_bar.setObjectName(u"name_bar")
        font3 = QFont()
        font3.setFamily(u"Arial Black")
        font3.setBold(True)
        font3.setWeight(75)
        self.name_bar.setFont(font3)
        self.name_bar.setStyleSheet(u"color:rgba(255,255, 255, 150);")

        self.gridLayout.addWidget(self.name_bar, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u" User Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u266c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Forgot Your Yser Name or Password ", None))
        self.close.setText("")
        self.minimize.setText("")
        self.name_bar.setText(QCoreApplication.translate("MainWindow", u"kyopark's programe", None))
    # retranslateUi

