import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # class 함수들은 내가 누군지 언급해줘야 해/ 그게 self/ 생성자는 리턴이 없어서 기본적으로 None/ None 대신 str 들어가면 문자열 리턴해줘야 해 
        super().__init__()
        self.initUI()

    # 화면정의를 위해 사용자 함수
    def initUI(self) -> None:
        self.setGeometry(300, 100, 640, 400)  # x축, y축, 창의 너비, 창의 높이
        self.setWindowTitle('QTemplate!!!')
        self.text = 'What a wonderful world~'
        self.show()

# QWidget 의 내장함수/ 화면을 그리는 일을 수행
    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        # 그리는 함수 추가
        self.drawText(event, paint)
        paint.end()

    # 텍스트 그리기 위한 사용자 함수
    def drawText(self, event, paint):
        paint.setPen(QColor(50,50,50))  # 색깔 검은색으로
        paint.setFont(QFont('NanumGothic', 20))
        paint.drawText(105, 100, 'HELL WORLD~')  # QLabel 이랑은 다른 방식으로 글자 표현/ 글자를 drawText 함수 사용해서 그린것임
        paint.setPen(QColor(0,250,10))  # RGB
        paint.setFont(QFont('Impact', 14))  # 영어에서 많이 쓰는 폰트
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)  # 정중앙에 나오도록

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()  # 실행