import numpy as np
import pandas as pd
import streamlit as st

seoul = pd.read_csv('seoul_predict_2.csv')

def region_searching():
    st.title('지역 검색')
    loca_1 = st.selectbox('지역 1을 선택해주세요.',
                     ('서울', '경기', '인천', '충북', '충남', '대전', '강원', '경북', '경남', '대구', '울산', '부산', '전북', '전남', '광주', '제주'))
    if loca_1 == '서울':
        loca_2 = st.selectbox('지역 2를 선택해주세요.',
                     ('전체', '강남', '강동', '강북', '강서', '관악', '광진', '구로', '금천', '노원', '도봉', '동대문', '동작', '마포', '서대문', '서초',
                     '성동', '성북', '송파', '양천', '영등포', '용산', '은평', '종로', '중구', '중랑'))
        if loca_2 == '전체':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            st.header('검색 결과')
            df = seoul.loc[(seoul['빗물 이용시설 설치 적합여부[0/1]']==1)]
            st.map(df, zoom=10)
            st.dataframe(seoul_all)
        elif loca_2 == '종로':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_jr = seoul_all.loc[(seoul_all['지역']=='종로구')]
            st.header('검색 결과')
            df_jr = seoul.loc[(seoul['지역']=='종로구')]
            df_jr = df_jr.loc[(df_jr['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_jr.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_jr)
            else:
                st.map(df_jr, zoom=12)
                st.dataframe(seoul_jr)
        elif loca_2 == '송파':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_sp = seoul_all.loc[(seoul_all['지역']=='송파구')]
            st.header('검색 결과')
            df_sp = seoul.loc[(seoul['지역']=='송파구')]
            df_sp = df_sp.loc[(df_sp['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_sp.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_sp)
            else:
                st.map(df_sp, zoom=12)
                st.dataframe(seoul_sp)
        elif loca_2 == '성동':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_sd = seoul_all.loc[(seoul_all['지역']=='성동구')]
            st.header('검색 결과')
            df_sd = seoul.loc[(seoul['지역']=='성동구')]
            df_sd = df_sd.loc[(df_sd['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_sd.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_sd)
            else:
                st.map(df_sd, zoom=12)
                st.dataframe(seoul_sd)
        elif loca_2 == '광진':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_kj = seoul_all.loc[(seoul_all['지역']=='광진구')]
            st.header('검색 결과')
            df_kj = seoul.loc[(seoul['지역']=='광진구')]
            df_kj = df_kj.loc[(df_kj['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_kj.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_kj)
            else:
                st.map(df_kj, zoom=12)
                st.dataframe(seoul_kj)
        elif loca_2 == '중구':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_jk = seoul_all.loc[(seoul_all['지역']=='중구')]
            st.header('검색 결과')
            df_jk = seoul.loc[(seoul['지역']=='중구')]
            df_jk = df_jk.loc[(df_jk['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_jk.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_jk)
            else:
                st.map(df_jk, zoom=12)
                st.dataframe(seoul_jk)
        elif loca_2 == '중랑':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_jrk = seoul_all[(seoul_all['지역']=='중랑구')]
            st.header('검색 결과')
            df_jrk = seoul.loc[(seoul['지역']=='중랑구')]
            df_jrk = df_jrk.loc[(df_jrk['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_jrk.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_jrk)
            else:
                st.map(df_jrk, zoom=12)
                st.dataframe(seoul_jrk)
        elif loca_2 == '성북':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_sb = seoul_all.loc[(seoul_all['지역']=='성북구')]
            st.header('검색 결과')
            df_sb = seoul.loc[(seoul['지역']=='성북구')]
            df_sb = df_sb.loc[(df_sb['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_sb.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_sb)
            else:
                st.map(df_sb, zoom=12)
                st.dataframe(seoul_sb)
        elif loca_2 == '영등포':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_ydp = seoul_all.loc[(seoul_all['지역']=='영등포구')]
            st.header('검색 결과')
            df_ydp = seoul.loc[(seoul['지역']=='영등포구')]
            df_ydp = df_ydp.loc[(df_ydp['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_ydp.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_ydp)
            else:
                st.map(df_ydp, zoom=12)
                st.dataframe(seoul_ydp)
        elif loca_2 == '서초':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_sc = seoul_all.loc[(seoul_all['지역']=='서초구')]
            st.header('검색 결과')
            df_sc = seoul.loc[(seoul['지역']=='서초구')]
            df_sc = df_sc.loc[(df_sc['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_sc.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_sc)
            else:
                st.map(df_sc, zoom=12)
                st.dataframe(seoul_sc)
        elif loca_2 == '양천':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_yc = seoul_all.loc[(seoul_all['지역']=='양천구')]
            st.header('검색 결과')
            df_yc = seoul.loc[(seoul['지역']=='양천구')]
            df_yc = df_yc.loc[(df_yc['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_yc.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_yc)
            else:
                st.map(df_yc, zoom=12)
                st.dataframe(seoul_yc)
        elif loca_2 == '강남':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_kn = seoul_all.loc[(seoul_all['지역']=='강남구')]
            st.header('검색 결과')
            df_kn = seoul.loc[(seoul['지역']=='강남구')]
            df_kn = df_kn.loc[(df_kn['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_kn.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_kn)
            else:
                st.map(df_kn, zoom=12)
                st.dataframe(seoul_kn)
        elif loca_2 == '강동':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_kd = seoul_all.loc[(seoul_all['지역']=='강동구')]
            st.header('검색 결과')
            df_kd = seoul.loc[(seoul['지역']=='강동구')]
            df_kd = df_kd.loc[(df_kd['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_kd.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_kd)
            else:
                st.map(df_kd, zoom=12)
                st.dataframe(seoul_kd)
        elif loca_2 == '강북':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_kb = seoul_all.loc[(seoul_all['지역']=='강북구')]
            st.header('검색 결과')
            df_kb = seoul.loc[(seoul['지역']=='강북구')]
            df_kb = df_kb.loc[(df_kb['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_kb.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_kb)
            else:
                st.map(df_kb, zoom=12)
                st.dataframe(seoul_kb)
        elif loca_2 == '강서':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_ks = seoul_all.loc[(seoul_all['지역']=='강서구')]
            st.header('검색 결과')
            df_ks = seoul.loc[(seoul['지역']=='강서구')]
            df_ks = df_ks.loc[(df_ks['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_ks.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_ks)
            else:
                st.map(df_ks, zoom=12)
                st.dataframe(seoul_ks)
        elif loca_2 == '관악':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_ka = seoul_all.loc[(seoul_all['지역']=='관악구')]
            st.header('검색 결과')
            df_ka = seoul.loc[(seoul['지역']=='관악구')]
            df_ka = df_ka.loc[(df_ka['빗물 이용시설 설치 적합여부[0/1]']==1)]
            if (df_ka.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_ka)
            else:
                st.map(df_ka, zoom=12)
                st.dataframe(seoul_ka)
        elif loca_2 == '구로':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_kr = seoul_all.loc[(seoul_all['지역']=='구로구')]
            st.header('검색 결과')
            df_kr = seoul.loc[(seoul['지역']=='구로구')]
            if (df_kr.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_kr)
            else:
                st.map(df_kr, zoom=12)
                st.dataframe(seoul_kr)
        elif loca_2 == '금천':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_kc = seoul_all.loc[(seoul_all['지역']=='금천구')]
            st.header('검색 결과')
            df_kc = seoul.loc[(seoul['지역']=='금천구')]
            if (df_kc.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_kc)
            else:
                st.map(df_kc, zoom=12)
                st.dataframe(seoul_kc)
        elif loca_2 == '노원':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_nw = seoul_all.loc[(seoul_all['지역']=='노원구')]
            st.header('검색 결과')
            df_nw = seoul.loc[(seoul['지역']=='노원구')]
            if (df_nw.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_nw)
            else:
                st.map(df_nw, zoom=12)
                st.dataframe(seoul_nw)
        elif loca_2 == '도봉':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_db = seoul_all.loc[(seoul_all['지역']=='도봉구')]
            st.header('검색 결과')
            df_db = seoul.loc[(seoul['지역']=='도봉구')]
            if (df_db.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_db)
            else:
                st.map(df_db, zoom=12)
                st.dataframe(seoul_db)
        elif loca_2 == '동대문':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_ddm = seoul_all.loc[(seoul_all['지역']=='동대문구')]
            st.header('검색 결과')
            df_ddm = seoul.loc[(seoul['지역']=='동대문구')]
            if (df_ddm.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_ddm)
            else:
                st.map(df_ddm, zoom=12)
                st.dataframe(seoul_ddm)
        elif loca_2 == '동작':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_dj = seoul_all.loc[(seoul_all['지역']=='동작구')]
            st.header('검색 결과')
            df_dj = seoul.loc[(seoul['지역']=='동작구')]
            if (df_dj.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_dj)
            else:
                st.map(df_dj, zoom=12)
                st.dataframe(seoul_dj)
        elif loca_2 == '마포':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_mp = seoul_all.loc[(seoul_all['지역']=='마포구')]
            st.header('검색 결과')
            df_mp = seoul.loc[(seoul['지역']=='마포구')]
            if (df_mp.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_mp)
            else:
                st.map(df_mp, zoom=12)
                st.dataframe(seoul_mp)
        elif loca_2 == '서대문':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_sdm = seoul_all.loc[(seoul_all['지역']=='서대문구')]
            st.header('검색 결과')
            df_sdm = seoul.loc[(seoul['지역']=='서대문구')]
            if (df_sdm.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_sdm)
            else:
                st.map(df_sdm, zoom=12)
                st.dataframe(seoul_sdm)
        elif loca_2 == '용산':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_ys = seoul_all.loc[(seoul_all['지역']=='용산구')]
            st.header('검색 결과')
            df_ys = seoul.loc[(seoul['지역']=='용산구')]
            if (df_ys.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_ys)
            else:
                st.map(df_ys, zoom=12)
                st.dataframe(seoul_ys)
        elif loca_2 == '은평':
            seoul_all = seoul.sort_values(by=['빗물 이용시설 설치 적합여부[0/1]', '빗물목표량대비사용량'], ascending=[False, False])
            seoul_all = seoul_all[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
            seoul_ep = seoul_all.loc[(seoul_all['지역']=='은평구')]
            st.header('검색 결과')
            df_ep = seoul.loc[(seoul['지역']=='은평구')]
            if (df_ep.shape[0]==0):
                st.subheader('해당 지역에 적합한 건물이 없습니다.')
                st.dataframe(seoul_ep)
            else:
                st.map(df_ep, zoom=12)
                st.dataframe(seoul_ep)
def building_searching():
    st.title('시설물 검색')
    title = st.text_input('시설물 검색','도로명 주소(시설명)을 입력하세요.')
    
    if ((title == '코엑스') | ('강남구 영동대로 513' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='코엑스')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        buuilding = seoul_data.loc[(seoul_data['시설명']=='코엑스')]
        if (building['빗물 이용시설 설치 적합여부[0/1]']==0):
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 15px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 15px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '서울광장') | ('중구 세종대로 110' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='서울광장')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='서울광장')])
    elif ((title == '성동도로사업소') | ('성동구 자동차시장길 41' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='성동도로사업소')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='성동도로사업소')])    
    elif ((title == '스타시티') | ('광진구 아차산로 262' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='스타시티')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='스타시티')])
    elif ((title == 'DDP') | ('중구 을지로7가 을지로 281' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='DDP')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='DDP')])
    elif (('리본타워' in title) | ('중랑구 묵1동 7' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='묵동리본타워')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='묵동리본타워')])
    elif ((title == '한국과학기술원') | ('성북구 월곡2동 화랑로14길 5' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='한국과학기술원')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='한국과학기술원')])
    elif ((title == '국회') | ('영등포구 의사당대로 1' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='국회')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='국회')])
    elif ((title == '호반건설 신사옥') | ('서초구 양재대로2길 18' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='호반건설 신사옥')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='호반건설 신사옥')])
    elif (('테라타워' in title) | ('송파구 송파대로 167' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='문정역테라타워')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='문정역테라타워')])
    elif ((title == '순명빌딩') | ('송파구 삼전로 66' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='순명빌딩')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='순명빌딩')])
    elif ((title == '향군타워') | ('송파구 올림픽로35길 123' in title) ):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='향군타워')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        st.dataframe(seoul_data.loc[(seoul_data['시설명']=='향군타워')])
        
        
pages_names_to_funcs = {'지역 검색🗺': region_searching, '시설물 검색🏢': building_searching}

selected_page = st.sidebar.selectbox('검색 방법을 골라주세요.', pages_names_to_funcs.keys())

pages_names_to_funcs[selected_page]()
# 파일실행: File > New > Terminal(anaconda prompt) - 빅프로젝트\rain.py
