import requests
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

# 질문 분류 / 질문 / 답변 담을 리스트 초기화
data = []

# 1~2p에 해당하는 FAQ 받아오기
for j in range(1, 3):
    url = f'https://www.speedmate.com/customer/FAQ?categoryNm=&pageNo={j}'
    req = requests.get(url)

    driver = Chrome()
    driver.get(url)
    time.sleep(1)

    store = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dt > strong')
    
    for i in range(len(store)) :
        store = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dt > strong')
        print(store[i].text)

        clickable = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dt')
        clickable[i].click()
        time.sleep(0.5)

        q_header = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dt > span:nth-child(2)')
        print(q_header[i].text)
        time.sleep(0.5)

        answers = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dd > div')
        print(answers[i].text)
        time.sleep(0.5)

        data.append([q_header[i].text, store[i].text, answers[i].text])

columns = ['분류','질문','답변']
faq_tbl = pd.DataFrame(data, columns=columns)
faq_tbl.to_csv('./result.csv',index = False)

