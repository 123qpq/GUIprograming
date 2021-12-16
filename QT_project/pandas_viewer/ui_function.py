from main import *
## ==> GLOBALS

GLOBAL_STATE = 0
WINDOW_STATE = False

class UIFunctions(WindowClass):
    
    def maximizer(self):
        global WINDOW_STATE
        if WINDOW_STATE == False:
            self.showMaximized()
            WINDOW_STATE = True
        else:
            self.showNormal()
            WINDOW_STATE = False
            
    def params_maker(self):
        self.keyword = QLabel(self.ui.params)
        self.keyword.setObjectName(u"keyword_2")
        self.keyword.setMinimumSize(QSize(50, 20))
        self.keyword.setMaximumSize(QSize(70, 20))
        font1 = QFont()
        font1.setBold(True)
        self.keyword.setFont(font1)
        self.keyword.setStyleSheet(u"color:rgb(255,255, 255);")
        self.keyword.setAlignment(Qt.AlignCenter)

        self.ui.horizontalLayout_2.addWidget(self.keyword)
        
        self.keyword_edit = QLineEdit(self.ui.params)
        self.keyword_edit.setObjectName(u"keyword_edit_2")
        self.keyword_edit.setMinimumSize(QSize(100, 20))
        self.keyword_edit.setMaximumSize(QSize(200, 20))
        self.keyword_edit.setStyleSheet(u"background-color : rgb(244, 236, 254);")

        self.ui.horizontalLayout_2.addWidget(self.keyword_edit)
        
        
        
    
    def uiDefinitions(self):
        if Settings.CUSTOM_TITLE_BAR:
            self.setWindowFlags(Qt.FramelessWindowHint) #상태바 지움
            self.setAttribute(Qt.WA_TranslucentBackground) # 배경 지움
        
        self.ui.minimize.clicked.connect(lambda: self.showMinimized()) # minimize
        self.ui.maximize.clicked.connect(lambda: UIFunctions.maximizer(self)) # maximize
        self.ui.close.clicked.connect(lambda: self.close()) # close
        
        # window resize
        self.sizegrip = QSizeGrip(self.ui.control_size)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")
        
        #UIFunctions.params_maker(self)
        
        def moveWindow(event):
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                    self.dragPos = event.globalPosition().toPoint()
                    event.accept()
        self.ui.header.mouseMoveEvent = moveWindow

        def dobleClickMaximizer(event):
            if event.type() == QEvent.MouseButtonDblClick:
                UIFunctions.maximizer(self)
        self.ui.header.mouseDoubleClickEvent = dobleClickMaximizer