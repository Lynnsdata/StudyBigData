# Selenium 사용 웹 페이지 크롤링
# 패키지 로드
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

def getCoffeeBeanStoreInfo(result):
    # USB: usb_device_handle_win.cc:1048 시스 에 부착된 장치가 작동하지 않습니다.
    # 오류 해결방법
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome('./day03/chromedriver.exe', options=options)

    # chrome webdriver 객체 생성
    #wd = webdriver.Chrome('./day03/chromedriver.exe')  # 경로 조심!

    for i in range(1, 10+1):
        wd.get('https://www.coffeebeankorea.com/store/store.asp')
        time.sleep(1)

        # 없는 곳도 있어서 예외처리
        try:
            wd.execute_script(f"storePop2('{i}')")
            
            time.sleep(0.5)  # 팝업 표시후에 크롤링이 안돼서 브라우저가 닫히는 것을 방지
    # 주피터에서 한거 복붙
            html = wd.page_source
            soup = BeautifulSoup(html, 'html.parser')
            store_name = soup.select('div.store_txt > h2')[0].string
            print(store_name)
            store_info = soup.select('table.store_table > tbody > tr > td')
            store_address_list = list(store_info[2])
            store_address = store_address_list[0].strip()
            store_contact = store_info[3].string
            result.append([store_name]+[store_address]+[store_contact])
        except Exception as e:
            print(e)
            continue


        

def main():
    result = []
    print('커피빈 매장 크롤링 >>> ')
    getCoffeeBeanStoreInfo(result)

    # 판다스 데이터프레임 생성
    columns = ['store', 'address', 'phone']
    coffeebean_df = pd.DataFrame(result, columns=columns)

    # csv 저장
    coffeebean_df.to_csv('./coffeebean_shop_info.csv', index=True, encoding='utf-8')
    print('저장완료')

    del result[:]

if __name__ == '__main__':
    main()