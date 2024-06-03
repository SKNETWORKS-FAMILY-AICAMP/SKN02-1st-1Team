from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from db_connector import Connector
import time
import requests
import pandas as pd

data = []
table_name = 'speedmate_store'

url = 'https://www.speedmate.com/reserve/FindBranchList'
r = requests.get(url)

driver = Chrome()
driver.get(url)
time.sleep(1.5)

conn = Connector().get_connection()
cur = conn.cursor()

for i in range(1, 18) :
    # 지역 select --- 화살표 클릭
    arrow = driver.find_element(By.CLASS_NAME, 'select2-selection__arrow')
    arrow.click()
    time.sleep(1)

    # 지역 li tag list 받아오기
    els = driver.find_elements(By.CSS_SELECTOR, '#select2-city-results > li')
    el = els[i]
    el.click()
    time.sleep(1)
    print("element 클릭")

    # 검색창에 cursor 후 Enter 전송
    input_space = driver.find_element(By.ID, 'searchStore')
    input_space.click()
    input_space.send_keys(Keys.ENTER)

    print("Send ENTER")
    time.sleep(1.5)

    # 검색된 store list --- li tag 리스트 받아오기
    store_list = driver.find_elements(By.CSS_SELECTOR, '.placeList > li')

    # li tag 내부 제목/주소 텍스트 가져오기
    for store in store_list:
        store_name = store.find_element(By.CSS_SELECTOR, "dl > dt > h4").text
        print(store_name)
        address = store.find_element(By.CSS_SELECTOR, "dl > dd > p").text
        data.append([store_name, address])
        
        split_addr = address.split()
        query = f"INSERT INTO {table_name} VALUES ('{store_name}', '{address}', '{split_addr[0]}', '{split_addr[1]}', '{split_addr[2]}')"
        cur.execute(query)

conn.commit()
conn.close()

# data to CSV file
file_name = f'./data/{table_name}.csv'
columns = ["지점명", "주소", "지역구분1", "지역구분2", "지역구분3"]
result_df = pd.DataFrame(data, columns = columns)
result_df.to_csv(file_name, index=False)