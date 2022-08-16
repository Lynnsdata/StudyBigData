import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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

    def btn1_clicked(self):
        self.txbLog.append('실행!!')
        self.pgbTask.setRange(0, 999999)
        for i in range(0, 1000000):  # 응답없음 발생!!
            print(f'출력 : {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'출력 > {i}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()  # 실행