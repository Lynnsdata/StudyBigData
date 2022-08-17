import sys
from turtle import title
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from urllib.parse import quote
import urllib.request
import json
import webbrowser

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # class 함수들은 내가 누군지 언급해줘야 해/ 그게 self/ 생성자는 리턴이 없어서 기본적으로 None/ None 대신 str 들어가면 문자열 리턴해줘야 해 
        super().__init__()
        uic.loadUi('./pyqt02/navermovie.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()
        
    def addControls(self) -> None:  # 위젯 정의, 이벤트(시그널) 처리
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.txtSearch.returnPressed.connect(self.btnSearchClicked)  # 검색 누르지 않고 엔터키로도 검색되도록 하기 (사용자 편의성)
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)

    def tblResultSelected(self) -> None:
        selected = self.tblResult.currentRow()  # 현재 선택된 열의 인덱스
        link = self.tblResult.item(selected, 2).text()  # 1 -> 2로 변경
        webbrowser.open(link)

    def btnSearchClicked(self) -> None:  # 슬롯(이벤트핸들러(처리자))
        jsonResult = []
        totalResult = []
        keyword = 'movie'
        search_word = self.txtSearch.text()
        display_count = 100

        # QMessageBox.information(self, '결과', search_word)
        jsonResult = self.getNaverSearch(keyword, search_word, 1, display_count)  # return 뒤에 아무것도 안넣으면 None이랑 같은 결과
        # print(jsonResult)

        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post))

        # print(totalResult)
        self.makeTable(totalResult)  # 결과를 터미널이 아닌 창에 뿌리기 위함
        return

    

    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)  # set 안붙였어서 오류났었다
        self.tblResult.setColumnCount(3)  # from 2
        self.tblResult.setRowCount(len(result))  # displayCount에 따라서 변경, 현재는 50
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '상영년도', '영화링크'])  # 제목변경
        self.tblResult.setColumnWidth(0, 250)
        self.tblResult.setColumnWidth(1, 100)
        self.tblResult.setColumnWidth(2, 100)  # 세번째 컬럼 길이
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)  # readonly

        i = 0
        for item in result:
            title = self.strip_tag(item[0]['title'])
            subtitle = self.strip_tag(item[0]['subtitle'])
            pubDate = item[0]['pubDate']
            link = item[0]['link']
            self.tblResult.setItem(i, 0, QTableWidgetItem(f'{title} / {subtitle}'))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(link))
            i += 1

    def strip_tag(self, title):  # html 태그를 없애주는 함수
            ret = title.replace('&lt;', '<')
            ret = ret.replace('&gt;', '>')
            ret = ret.replace('&quot;', '"')
            ret = ret.replace('&apos;', "'")
            ret = ret.replace('&amp;', '&')
            ret = ret.replace('<b>', '')
            ret = ret.replace('</b>', '')
            return ret

    def getPostData(self, post):
        temp = []
        title = post['title']
        subtitle = post['subtitle']
        link = post['link']
        pubDate = post['pubDate']  # 기사 실린 날짜

        temp.append({'title':title
                    , 'subtitle':subtitle
                    , 'pubDate':pubDate
                    , 'link':link})

        return temp


    # 네이버API 크롤링 함수
    def getNaverSearch(self, keyword, search, start, dispaly):
        url = f'https://openapi.naver.com/v1/search/{keyword}.json' \
            f'?query={quote(search)}&start={start}&display={dispaly}'
        print(url)
        req = urllib.request.Request(url)
        # 네이버 인증 추가
        req.add_header('X-Naver-Client-Id', 'nPPmnz7WW775lZrpBxkI')
        req.add_header('X-Naver-Client-Secret', '4LsoY2TM4E')

        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print('URL request succeed')
        else:
            print('URL request failed')

        ret = res.read().decode('utf-8')
        if ret == None:
            return None
        else:
            return json.loads(ret)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()  # 실행