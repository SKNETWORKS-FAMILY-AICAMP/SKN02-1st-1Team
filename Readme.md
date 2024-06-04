# SKN02-1st-1Team
강민호 / 구선아/ 김서연/ 박경희

# 프로젝트 목표

대한민국의 등록차량은 2500만대로 전국민의 2명 중 1명은 차량을 소유하고 있는 나라입니다. 하지만, 차량은 지속적인 정비가 필요한 기구이며 전문적인 지식이 없이는 정비할 수 없습니다.
따라서 정비소의 역할도 중요하지만 지역별 차량수의 변화에 따라 정비소를 적재적소에 설치하여 고객 만족도를 높여야 할 필요성을 느꼈습니다.
그러므로 정비 차량 유지를 목적으로 하는 잠재고객층 유치를 위해 정비소를 추가로 설치해야 하는 곳을 알아내기 위한 지역별 인사이트를 제공하려합니다.


# 기능 명세

1. 연도별 차량등록 수 확인
2. 지역별 스피드메이트, Autooasis 지점량 비교, 지역별 차량 주행량 확인
3. FAQ
4. db연결
5. crawling

# 기술 스택

### 개발환경

![image.png](d1702de4-db47-45ab-a282-9774527df92c.png)![image.png](8ccd6567-f18f-46ef-ba02-4657ea5e36d4.png)![image.png](127af63d-3b2f-4060-b475-569a05b212fd.png)

### 데이터 수집 및 처리

![image.png](bded2042-8d1f-4bb8-b49d-fa508c25b5b8.png)![image.png](d7f58c02-e063-4a84-9680-11d7f333698e.png)![image.png](65d6632b-c685-4385-aa36-1e7ea023f717.png)![image.png](ba4d38a7-b5da-474d-b20c-081bbb78236e.png)

### 웹페이지 구현

![image.png](27dcda40-0b0c-4464-997a-bf4603eef32d.png)![image.png](dee35bd4-f250-4646-a2dc-03d599e5ed42.png)![image.png](9e19efee-f8dd-4d4c-981a-0c7537a8259b.png)

# 기능

## 1. 연도별 차량등록 수 확인

csv파일로 된 차량등록수 데이터를 read_csv함수로 읽어들여오고 matplotlib 라이브러리를 이용하여 bar chart 를 만든다.

## 2. 지역별 차량 주행량 확인, 지역별 스피드메이트, Autooasis 지점수 비교

### folium_graph.py (모듈)

get_graph(인수: 테이블명, total 사용 여부=기본값 False, return Folium map 객체) - folium graph를 사용 목적에 따라 가져오는 function.   
기본적으로는 인수로 들어온 전체 테이블을 조회하여  addr_code의 숫자를 세어 해당 점포 수를 누적시킨다.   
total 사용할 시에는 addr_code 값을 키로, total 값을 밸류로 사용하여 그래프를 생성한다.   
기본적으로는 인수로 들어온 전체 테이블을 조회하여  addr_code의 숫자를 세어 해당 점포 수를 누적시킨다.   
total 사용할 시에는 addr_code 값을 키로, total 값을 밸류로 사용하여 그래프를 생성한다.

## 3. FAQ

my_app - web에 strreamlit을 이용하여 웹을 만들기 위함   
class View : FAQ 분류, 질문, 답변의 형태로 된 데이터프레임을 입력받아 저장   
ViewAllFAQ() : 질문과 답변 분류로 된 데이터프레임을 expander()와 container()를 이용하여 클릭시 확장되며 해당 답변을 확인할 수 있도록 구성   
st.divider() : 페이지 마지막 부분을 구분짓기 위해 구분선 추가

## 4. db연결

db_connector.py   
Connector class 구현 - DB Connection이 singleton으로 사용될 수 있도록 의도   
초기화(인수 없음) - 내부에 가지고 있는 DB 정보들로 초기화하고, 한 번 초기화 된 이후 다시 초기화 시도 시, 예외 발생하도록 함.   
get_connection(인수 없음, return connector 객체) - 외부에서 접근할 수 있는 classmethod로 작성, 외부에서 connector를 반환받을 수 있다.   
select_all(인수: 테이블명, return cursor 객체) - 외부에서 테이블 이름으로 전체 테이블 조회할 수 있는 쿼리 제공

## 5. crawling

# 데이터 정보 및 출처
### 용도별 차종별 시군구별 자동차주행거리
> 정보제공 : 한국교통공단
> 데이터기간 : 2018-2023
> 구분 : 행정구역별
### 자동차등록대수현황 시도별
> 정보제공 : 국토교통부
> 데이터기간 : 2023
> 구분 : 시도명/시군구
### 스피드메이트, 오토오아시스 지점 위치
> 스피드메이트 정보 :  스피드메이트 지점찾기
> 경로 : https://www.speedmate.com/reserve/FindBranchList
> 오토오아시스 정보 : 오토오아시스 지점찾기
> 경로 : https://www.autooasis.com/brand 
