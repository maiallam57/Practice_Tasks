import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2


VBL = QHBoxLayout()
veritcalLayout = QVBoxLayout()

class VideoCap(QWidget):
    def __init__(self):
        super(VideoCap, self).__init__()
        
        self.setWindowIcon(QIcon("images.png"))
        self.setWindowTitle("ROV GUI")
        self.setFixedSize(1200, 600)
        
        self.FeedLabel = QLabel()
        VBL.addWidget(self.FeedLabel)

        self.PauseBTN = QPushButton("Pause")
        self.PauseBTN.setFixedSize(60,35)
        self.PauseBTN.clicked.connect(self.PauseFeed)
        VBL.addWidget(self.PauseBTN)

        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        
        self.dispalyButtons()
        self.Timer()
        self.dispalyHat()
        
        self.setLayout(VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def PauseFeed(self):
        self.Worker1.stop()
       
    def dispalyButtons(self):
        self.horizontalLayout = QHBoxLayout()
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {"button 1": (0, 0), "button 2": (0, 1), "button 3": (0, 2), "button 4": (0, 3),
                   "button 5": (0, 4), "button 6": (0, 5), "button 7": (1, 0), "button 8": (1,1), 
                   "button 9": (1, 2), "button 10": (1, 3), "button 11": (1, 4), "button 12": (1, 5)
        }

        for buttonText, position in buttons.items():
            self.buttons[buttonText] = QPushButton(buttonText)
            self.buttons[buttonText].setFixedSize(60,35)
            self.buttons[buttonText].setStyleSheet("QPushButton"
                                 "{"
                                 "border : 2px solid gray;"
                                 "background : lightgray;"
                                 "}")
            buttonsLayout.addWidget(self.buttons[buttonText], position[0], position[1])

        self.horizontalLayout.addLayout(buttonsLayout)
        VBL.addLayout(self.horizontalLayout)
        
    def dispalyHat(self):
    
        self.arrowsLayout = QHBoxLayout()
        leftBtn = QPushButton("", self)
        leftBtn.setFixedSize(50,60)
        leftBtn.setIcon(QIcon('left.png'))
        leftBtn.setStyleSheet("QPushButton"
                                 "{"
                                 "border : 4px solid gray;"
                                 "background : white;"
                                 "}")
        self.arrowsLayout.addWidget(leftBtn)
        
        self.forwardBackwardLayout = QGridLayout()
        arrows = {'forward': (0, 0), 'backward': (1, 0)}
        arrows['forward'] = QPushButton("", self)
        arrows['forward'].setFixedWidth(50)
        arrows['forward'].setIcon(QIcon('forward.png'))
        arrows['forward'].setStyleSheet("QPushButton"
                                 "{"
                                 "border : 4px solid gray;"
                                 "background : white;"
                                 "}")
        self.forwardBackwardLayout.addWidget(arrows['forward'])
    
        arrows['backward'] = QPushButton("", self)
        arrows['backward'].setFixedWidth(50)
        arrows['backward'].setIcon(QIcon('backward.png'))
        arrows['backward'].setStyleSheet("QPushButton"
                                 "{"
                                 "border : 4px solid gray;"
                                 "background : white;"
                                 "}")
        self.forwardBackwardLayout.addWidget(arrows['backward'])
        
        self.arrowsLayout.addLayout(self.forwardBackwardLayout)
        
        rightBtn = QPushButton("", self)
        rightBtn.setFixedSize(50,60)
        rightBtn.setIcon(QIcon('right.png'))
        rightBtn.setStyleSheet("QPushButton"
                                 "{"
                                 "border : 4px solid gray;"
                                 "background : white;"
                                 "}")
        self.arrowsLayout.addWidget(rightBtn)
        
        
        veritcalLayout.addLayout(self.arrowsLayout)
        VBL.addLayout(veritcalLayout)
        
       
    def Timer(self):
            self.minute=00
            self.second=00
            self.startwidth=False
            
            self.timerBtn = QGridLayout()
            self.label=QLabel(self)
            self.label.setStyleSheet("QLabel"
                                     "{"
                                     
                                     "font : bold;"
                                     "color : blue"
                                     "}")
            self.timerBtn.addWidget(self.label,0,1)
            
            self.start = QPushButton("Start", self)
            self.start.setFixedSize(60,35)
            self.timerBtn.addWidget(self.start,1,1)
            self.start.clicked.connect(self.Start)
            self.start.setStyleSheet("QPushButton"
                                     "{"
                                     "border : 4px solid red;"
                                     "background : pink;"
                                     "}")
            
            self.reset = QPushButton("Reset", self)
            self.reset.setFixedSize(60,35)
            self.timerBtn.addWidget(self.reset,1,3)
            self.reset.clicked.connect(self.Reset)
            self.reset.setStyleSheet("QPushButton"
                                     "{"
                                     "border : 4px solid green;"
                                     "background : lightgreen;"
                                     "}")    
            
            veritcalLayout.addLayout(self.timerBtn)
            VBL.addLayout(veritcalLayout)  
            
            timer=QTimer(self)
            timer.timeout.connect(self.showCounter)
            timer.start(1000)
            

    def showCounter(self):
            if self.startwidth:
                self.second+=1
                if self.second==60:
                    self.minute+=1
                    self.second=00
            watch = ' \t  ' + str(self.minute)+' : '+ str(self.second)
            self.label.setText(watch)
       
    def Start(self):
        if self.start.text()=='stop':
            self.start.setText('Resume')
            self.startwidth=False
        else:
            self.startwidth = True
            self.start.setText('stop')
    
    def Reset(self):
        self.minute=0
        self.second=0


class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
                
    def stop(self):
        self.ThreadActive = False
        self.quit()
        

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = VideoCap()
    Root.show()
    sys.exit(App.exec())