#만렙이전 접은 유저들은 몇렙에서 많이 접엇을까? 그 레벨 구간대에 가장 재미없는 컨텐츠가 있는 것은 아닐까?
import pandas as pd
import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import time
import numpy as np
# API 키와 검색할 서버명, 검색할 기간(최근 30일) 설정
API_KEY = "Input_your_Key_:)"
SERVER_NAME = ['prey','anton','bakal','cain','casillas','diregie','hilder','siroco']
end_date = datetime.now()
start_date = end_date - timedelta(days=30)
Nick = ['11','22','33','44','55','66','77','88','99','00','abc','초보','처음','검사','거너','도적','프리','던파','격투','격가','나이트','마창','총검','아처','뉴비','신입']


data = []
df = pd.DataFrame(data, columns=['ch_id', 'LV'])
for j in SERVER_NAME:
    for i in Nick:
        url = f"https://api.neople.co.kr/df/servers/{j}/characters?characterName={i}&wordType=full&startDate={start_date.strftime('%Y%m%d')}&endDate={end_date.strftime('%Y%m%d')}&limit=100000&apikey={API_KEY}"
        response = requests.get(url)
        player_info = response.json()

        # 결과 출력
        for char_info in player_info['rows']:
            print(f"{char_info['characterName']} 레벨 {char_info['level']}")

        # 레벨이 110 미만인 캐릭터 정보를 데이터프레임으로 저장

        for char_info in player_info['rows']:
            if char_info['level'] < 110:
                data.append([char_info['characterName'], char_info['level']])
        df = pd.DataFrame(data, columns=['ch_id', 'LV'])


        url = f"https://api.neople.co.kr/df/servers/{SERVER_NAME}/characters?characterName={i}&wordType=full&startDate={start_date.strftime('%Y%m%d')}&endDate={end_date.strftime('%Y%m%d')}&limit=100000&apikey={API_KEY}"
        #url2 = f"https://api.neople.co.kr/df/servers/{SERVER_NAME}/characters?wordType=nickname&limit=100&apikey={API_KEY}"
        response = requests.get(url)
        player_info = response.json()
        time.sleep(1)

# CSV 파일로 저장
df.to_csv('character_info.csv', encoding = 'cp949',index=False)

# CSV 파일 읽어오기
df = pd.read_csv('character_info.csv', encoding = 'cp949')

# 레벨별 캐릭터 수 세기
level_counts = df['LV'].value_counts()

# 그래프 그리기
fig, ax = plt.subplots()
ax.bar(level_counts.index, level_counts.values)
ax.set_xlabel('level')
ax.set_ylabel('C_num')
ax.set_title('level distribution')
plt.xticks(np.arange(0, 115, 5))

#전체 데이터 수
print(df.shape[0])

# 그래프
plt.show()
