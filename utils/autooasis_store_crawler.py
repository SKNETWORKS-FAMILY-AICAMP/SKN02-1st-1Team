from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from db_connector import Connector
import time
import requests
import pandas as pd

data = []
table_name = 'autooasis_store'

url = 'https://www.autooasis.com/brand'
r = requests.get(url)

driver = Chrome()
driver.get(url)
time.sleep(2)

conn = Connector.get_connection()
cur = conn.cursor()

for i in range(1, 18) :
    # 지역 select --- 화살표 클릭
    arrow = driver.find_element(By.ID, 'regionLSelect')
    arrow.click()
    time.sleep(1)

    # 지역 li tag list 받아오기
    els = driver.find_elements(By.CSS_SELECTOR, '#regionLSelect > option')
    el = els[i]
    el.click()
    time.sleep(1)

    #검색버튼 누름
    search = driver.find_element(By.CLASS_NAME, 'search_btn')
    search.click()
    time.sleep(1)

    # 다음 페이지 버튼을 끝까지 눌러서 페이지의 총 길이를 확인한다.
    
    

    #모든 페이지의 길이를 구하기 위해 alert를 이용한다.
    page_cnt = 0
    while(True) :
        try:
            pages = driver.find_elements(By.CSS_SELECTOR, '.list_number > ul > li')
            page_cnt += len(pages)-4
            pages[-1].click()
            time.sleep(1)
            result = Alert(driver)
            result.accept()
        except:
            continue
        else :
            break

    #끝 페이지로 갔을 때 마지막 페이지로 가기 위해 pages[-3] 한번 누르고 
    pages = driver.find_elements(By.CSS_SELECTOR, '.list_number > ul > li')
    pages[-3].click()

    store_list = driver.find_elements(By.CSS_SELECTOR, '.search_result > a')

    # # li tag 내부 제목/주소 텍스트 가져오기
    for store in store_list:
        store_name = store.find_element(By.CLASS_NAME, "branch_title").text
        address = store.find_element(By.CLASS_NAME, "branch_address").text
        postcode = address[1:6]
        address = address[7:]
        data.append([store_name, postcode, address, address.split()[0], address.split()[1], address.split()[2]])

        query = f"INSERT INTO {table_name} VALUES ('{store_name}', '{postcode}', '{address}', '{address.split()[0]}', '{address.split()[1]}', '{address.split()[2]}')"
        print(store_name, postcode, address)
        cur.execute(query)

    print(page_cnt)
    for p in range(1,page_cnt) :
        time.sleep(1)
        pages = driver.find_elements(By.CSS_SELECTOR, '.list_number > ul > li')
        pages[1].click()

    # 검색된 store list --- li tag 리스트 받아오기
        store_list = driver.find_elements(By.CSS_SELECTOR, '.search_result > a')
    # # li tag 내부 제목/주소 텍스트 가져오기
        for store in store_list:
            store_name = store.find_element(By.CLASS_NAME, "branch_title").text
            address = store.find_element(By.CLASS_NAME, "branch_address").text
            postcode = address[1:6]
            address = address[7:]
            data.append([store_name, postcode, address, address.split()[0], address.split()[1], address.split()[2]])

            query = f"INSERT INTO {table_name} VALUES ('{store_name}', '{postcode}', '{address}', '{address.split()[0]}', '{address.split()[1]}', '{address.split()[2]}')"
            print(store_name, postcode, address)
            cur.execute(query)

conn.commit()
conn.close()

# data to CSV file
file_name = f'./data/{table_name}.csv'
columns = ["지점명", "우편번호", "주소", "지역구분1", "지역구분2", "지역구분3"]
result_df = pd.DataFrame(data, columns = columns)
result_df.to_csv(file_name, index=False)