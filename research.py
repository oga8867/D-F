#streamlit run research.py
import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import time
import numpy as np
global x, char_lv, charname, charclass, data
data = []
API_KEY = "eEWia7fBRvOd4sws6g7rgL9wqyUcKXEH"
def main():
    st.image('./DF.jpg')
    st.header('당신은 왜 중간에 게임을 접었나요?')
    #SERVER_NAME = ['안톤', '바칼', '카인', '카시야스', '디레지에', '힐더', '프레이', '시로코']
    SERVER_NAME = st.selectbox('당신 캐릭터의 서버 이름은?', ['안톤', '바칼', '카인', '카시야스', '디레지에', '힐더', '프레이', '시로코'])
    servers = {'안톤':'anton','바칼':'bakal','카인':'cain','카시야스':'casillas','디레지에':'diregie','힐더':'hilder','프레이':'prey','시로코':'siroco'}


    name = st.text_input('당신 캐릭터의 이름은?')
    charservername=servers[SERVER_NAME]
    try:
        if st.button('검색'):

            print(servers[SERVER_NAME])

            url = f"https://api.neople.co.kr/df/servers/{servers[SERVER_NAME]}/characters?characterName={name}&apikey={API_KEY}"
            response = requests.get(url)
            player_info = response.json()
            print(player_info)
            for char_info in player_info['rows']:
                x = f"이름: {char_info['characterName']}, 직업: {char_info['jobName']}, 전직: {char_info['jobGrowName']} , 레벨: {char_info['level']}"
                char_lv = char_info['level']
                charname = char_info['characterName']
                charclass = char_info['jobName']
                print(char_lv)
            st.write(x)




    except:
        st.write("캐릭터가 존재하지 않는것 같아요.")
        st.image('./error.gif')


    # try:
    if 'char_lv' in globals() and char_lv >= 110:
        examples = '만렙이시네요!'
    else:
        examples = '중간에 그만 두셧군요.'

    url = f"https://api.neople.co.kr/df/servers/{servers[SERVER_NAME]}/characters?characterName={name}&apikey={API_KEY}"
    response = requests.get(url)
    player_info = response.json()

    char_lv = player_info['rows'][0]['level']
    charname = player_info['rows'][0]['characterName']
    charclass = player_info['rows'][0]['jobName']
    research = st.text_area(
        f'{examples} 혹시 게임 중간에 마음에 안드는 구간이나 컨텐츠는 무엇이였나요? 혹은 재미없거나 흥미가 떨어진다고 생각하시는 부분은 어떤 것인가요?')
    if st.button('제출'):
        st.write('감사합니다!')
        data.append([charservername,charname, charclass, char_lv, research])
        df = pd.DataFrame(data)
        #df = pd.DataFrame(data, columns=['ch_id', 'class', 'LV', 'research'])
        print(df)
        df.to_csv('research.csv',mode='a', header=False, encoding='cp949', index=False)
    #
    # except:
    #     pass

main()