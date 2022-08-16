import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # class 함수들은 내가 누군지 언급해줘야 해/ 그게 self/ 생성자는 리턴이 없어서 기본적으로 None/ None 대신 str 들어가면 문자열 리턴해줘야 해 
        super().__init__()
        uic.loadUi('./pyqt02/basic01.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()
        
    def addControls(self) -> None:
        self.btn1.clicked.connect(self.btn1_clicked)  # 시그널 연결 (btn1_clicked 이라는 함수랑)

    def btn1_clicked(self):
        self.label.setText('메시지 : btn1 버튼 클릭!!')
        QMessageBox.critical(self, 'signal', 'bt1_clicked!!!')  # 에러창


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()  # 실행