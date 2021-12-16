from PySide6.QtCore import Qt
from PySide6.QtGui import (QBrush, QColor, QFont, )
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QSizeGrip)
import sys
from test import get_df
from ui_function import *
from setting import Settings
from Keyword_UI import Ui_MainWindow
import pandas as pd

class WindowClass(QMainWindow):
    
    def __init__(self):
        super().__init__(flags=Qt.Window)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        Settings.CUSTOM_TITLE_BAR = True
        title = "kyopark's Keyword_searcher"
        self.setWindowTitle(title)
        
        self.font = QFont()
        self.font.setPointSize(10) # 폰트 크기
        self.font.setBold(True) # 폰트 굵게
        
        self.brush = QBrush(QColor(255, 255, 255)) # 브러쉬 색깔
        self.brush.setStyle(Qt.SolidPattern) # 브러쉬 패턴
        
        
        df = pd.DataFrame(get_df())#({"atest" : list(range(0, 20)),"best" : list(range(0, 20)),"cap" : list(range(20, 40))})
        self.ui.tableWidget.setColumnCount(len(df.columns)) # col 수 지정
        self.ui.tableWidget.setRowCount(len(df.index)) # row 수 지정
        
        for col_name in df.columns:
            self.ui.col_box.addItem(col_name)
            self.ui.col_box_2.addItem(col_name)
            self.ui.col_box_3.addItem(col_name)
        
        self.set_data(df)
        
        self.ui.SearchBtn.clicked.connect(lambda : self.run_search(df))
        self.ui.SetBtn.clicked.connect(lambda : self.run_filter(df))
        
        
        UIFunctions.uiDefinitions(self)
        
    def set_data(self, df):
        #table_setting
        self.ui.tableWidget.clear()
        
        #fill col
        for col, col_name in enumerate(df):
            colset = QTableWidgetItem()
            colset.setText(str(col_name));
            colset.setFont(self.font)
            colset.setForeground(self.brush)
            colset.setBackground(QColor(13, 11, 67))
            self.ui.tableWidget.setHorizontalHeaderItem(col, colset)
        
        #fill row & data
        for i in range(len(df.index)):
            rowset = QTableWidgetItem(str(i))
            rowset.setForeground(self.brush)
            rowset.setBackground(QColor(13, 11, 67))
            self.ui.tableWidget.setVerticalHeaderItem(i, rowset)
            
            for j in range(len(df.columns)):
                value = QTableWidgetItem()
                value.setText(str(df.iloc[i, j]))
                value.setFont(self.font)
                value.setForeground(self.brush)
                value.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget.setItem(i,j, value)
    
    
    def run_search(self, df):
        if self.ui.col_box_3.currentText() != "None":
            searching = df[self.ui.col_box_3.currentText()].str.contains(self.ui.keyword_edit.text())
            self.set_data(df[searching])
        else:
            self.set_data(df)
    
    
    def run_filter(self, df):
        #condition filter
        if self.ui.col_box.currentText() != "None":
            if self.ui.col_box_2.currentText() != "None":
                df = df[(int(self.ui.condi1.text()) <= df[self.ui.col_box.currentText()]) & (df[self.ui.col_box.currentText()] <= int(self.ui.condi2.text())) &\
                            (int(self.ui.condi1_2.text()) <= df[self.ui.col_box_2.currentText()]) & (df[self.ui.col_box_2.currentText()] <= int(self.ui.condi2_2.text()))]
            else:
                df = df[(int(self.ui.condi1.text()) <= df[self.ui.col_box.currentText()]) & (df[self.ui.col_box.currentText()] <= int(self.ui.condi2.text()))]
            
        self.set_data(df)
    
    def mousePressEvent(self, event):
        # window drag
        self.dragPos = event.globalPosition().toPoint()

        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
    

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec())