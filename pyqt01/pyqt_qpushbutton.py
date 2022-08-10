import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # class 함수들은 내가 누군지 언급해줘야 해/ 그게 self/ 생성자는 리턴이 없어서 기본적으로 None/ None 대신 str 들어가면 문자열 리턴해줘야 해 
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 100, 640, 400)  # x축, y축, 창의 너비, 창의 높이
        self.setWindowTitle('QPushbutton')
        self.show()
        
    def addControls(self) -> None:
        btn1 = QPushButton('click', self)
        btn1.setGeometry(510, 350, 120, 40)  # 버튼에 대한 사이즈, 위치

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()  # 실행