import requests
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from db_connector import Connector
import pandas as pd

# 질문 분류 / 질문 / 답변 담을 리스트 초기화
data = []
table_name = 'speedmate_faq'

# 1~2p에 해당하는 FAQ 받아오기
for j in range(1, 3):
    url = f'https://www.speedmate.com/customer/FAQ?categoryNm=&pageNo={j}'
    req = requests.get(url)

    driver = Chrome()
    driver.get(url)
    time.sleep(1)

    conn = Connector.get_connection()
    cur = conn.cursor()

    questions = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dt > strong')
    
    for i in range(len(questions)) :
        questions = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dt > strong')
        print(questions[i].text)
        this_question = questions[i].text.strip()

        clickable = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dt')
        clickable[i].click()
        time.sleep(0.5)

        q_header = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dt > span:nth-child(2)')
        print(q_header[i].text)
        time.sleep(0.5)
        this_header = q_header[i].text.strip()

        answers = driver.find_elements(By.CSS_SELECTOR, 'div#tabFaq > dl > dd > div')
        print(answers[i].text)
        time.sleep(0.5)
        this_answer = answers[i].text.strip()

        query = "INSERT INTO %s (category, question, answer) VALUES ('%s', '%s', '%s')" %(table_name, this_header, this_question, this_answer)
        print(this_header)
        print(this_question)
        print(this_answer)
        cur.execute(query)
        data.append([q_header[i].text, questions[i].text, answers[i].text])

    conn.commit()
    conn.close()

file_name = f'./data/{table_name}.csv'
columns = ['분류','질문','답변']
faq_tbl = pd.DataFrame(data, columns=columns)
faq_tbl.to_csv(file_name,index = False)