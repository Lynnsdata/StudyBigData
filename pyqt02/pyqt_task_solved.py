import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

# UI 스레드와 작업스레드 분리
class Worker(QThread):
    # QThread 는 화면을 그릴 권한이 없음
    # 대신 통신통해서 UI스레드가 그림을 그릴 수 있도록 통신수행
    valChangeSignal = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.working = True  # 클래스 내부변수 working을 지정

    def run(self):
        while self.working:
            for i in range(0, 1000000):  # 응답없음 발생!!
                print(f'출력 : {i}')
                # self.pgbTask.setValue(i)
                # self.txbLog.append(f'출력 > {i}')
                self.valChangeSignal.emit(i)  # UI스레드야 화면은 너가 그려줘~
                time.sleep(0.0001)  # 1micro sec 텀을 둠

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # class 함수들은 내가 누군지 언급해줘야 해/ 그게 self/ 생성자는 리턴이 없어서 기본적으로 None/ None 대신 str 들어가면 문자열 리턴해줘야 해 
        super().__init__()
        uic.loadUi('./pyqt02/ttask.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()
        
    def addControls(self) -> None:
        self.btnStart.clicked.connect(self.btn1_clicked)  # 시그널 연결 (btn1_clicked 이라는 함수랑)
        #  Worker 클래스 생성
        self.worker = Worker(self)
        self.worker.valChangeSignal.connect(self.updateProgress)  # 스레드에서 받은 시그널은 updateprogress 함수에서 처리해줌

    @pyqtSlot(int)  # '시그널과 슬롯을 연결할 때 데커레이터를 적어주면 더 좋다' 정도로만 이해
    def updateProgress(self, val): # val이 Worker스레드에서 전달받은 반복값
        self.pgbTask.setValue(val)
        self.txbLog.append(f'출력 > {val}')
        if val == 999999:
            self.worker.working = False

    
    def btn1_clicked(self):
        self.txbLog.append('실행!!')
        self.pgbTask.setRange(0, 999999)
        self.worker.start()
        self.worker.working = True
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()  # 실행