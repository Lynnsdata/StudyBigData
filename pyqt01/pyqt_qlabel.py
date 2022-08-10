from cProfile import label
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import *
# from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # class 함수들은 내가 누군지 언급해줘야 해/ 그게 self/ 생성자는 리턴이 없어서 기본적으로 None/ None 대신 str 들어가면 문자열 리턴해줘야 해 
        super().__init__()
        self.initUI()

    # 화면정의를 위해 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 100, 640, 400)  # x축, y축, 창의 너비, 창의 높이
        self.setWindowTitle('QLabel')
        self.text = 'What a wonderful world~'
        self.show()

    # 상대경로 하나 상위파일부터 부르기
    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./pyqt01/image/lion.png'))  # 윈도우 아이콘 지정/ 창의 아이콘은 바뀌는데 작업표시줄에는 안바뀐다(윈도우 특성)
        label1 = QLabel('Label1', self)
        label2 = QLabel('Label2', self)
        label1.setStyleSheet(
            'border-width: 3px;'  # 선 두께
            'border-style: solid;'  # 선 종류 (실선)
            'border-color: blue;'
            'image:url(./pyqt01/image/image1.png)'
        )
        label2.setStyleSheet(
            'border-width: 3px;'  # 선 두께
            'border-style: dot-dot-dash;'  # 선 종류 (점선)
            'border-color: red;'
            'image:url(./pyqt01/image/image1.png)'
        )

        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()  # 실행