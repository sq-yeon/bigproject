import numpy as np
import pandas as pd
import streamlit as st
import folium as g
from streamlit_folium import folium_static

seoul = pd.read_csv('빅프로젝트/seoul_predict_2.csv')

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
            s_map = g.Map(location=[37.58, 127.0], zoom_start=11)
            for i in range(len(df)):
                marker01 = g.Marker([df.iloc[i]['lat'], df.iloc[i]['lon']], tooltip=df.iloc[i]['시설명']).add_to(s_map)
            folium_static(s_map)
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
                jr_map = g.Map(location=[37.57037778, 126.9816417], zoom_start=13)
                for i in range(len(df_jr)):
                    marker01 = g.Marker([df_jr.iloc[i]['lat'], df_jr.iloc[i]['lon']], tooltip=df_jr.iloc[i]['시설명']).add_to(jr_map)
                folium_static(jr_map)
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
                sp_map = g.Map(location=[37.51175556, 127.1079306], zoom_start=13)
                for i in range(len(df_sp)):
                    marker01 = g.Marker([df_sp.iloc[i]['lat'], df_sp.iloc[i]['lon']], tooltip=df_sp.iloc[i]['시설명']).add_to(sp_map)
                folium_static(sp_map)
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
                sd_map = g.Map(location=[37.51175556, 127.1079306], zoom_start=13)
                for i in range(len(df_sp)):
                    marker01 = g.Marker([df_sp.iloc[i]['lat'], df_sp.iloc[i]['lon']], tooltip=df_sp.iloc[i]['시설명']).add_to(sd_map)
                folium_static(sd_map)
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
                kj_map = g.Map(location=[37.53573889, 127.0845333], zoom_start=13)
                for i in range(len(df_kj)):
                    marker01 = g.Marker([df_kj.iloc[i]['lat'], df_kj.iloc[i]['lon']], tooltip=df_kj.iloc[i]['시설명']).add_to(kj_map)
                folium_static(kj_map)
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
                jk_map = g.Map(location=[37.56100278, 126.9996417], zoom_start=13)
                for i in range(len(df_jk)):
                    marker01 = g.Marker([df_jk.iloc[i]['lat'], df_jk.iloc[i]['lon']], tooltip=df_jk.iloc[i]['시설명']).add_to(jk_map)
                folium_static(jk_map)
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
                jrk_map = g.Map(location=[37.60380556, 127.0947778], zoom_start=13)
                for i in range(len(df_jrk)):
                    marker01 = g.Marker([df_jrk.iloc[i]['lat'], df_jrk.iloc[i]['lon']], tooltip=df_jrk.iloc[i]['시설명']).add_to(jrk_map)
                folium_static(jrk_map)
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
                sb_map = g.Map(location=[37.58638333, 127.0203333], zoom_start=13)
                for i in range(len(df_sb)):
                    marker01 = g.Marker([df_sb.iloc[i]['lat'], df_sb.iloc[i]['lon']], tooltip=df_sb.iloc[i]['시설명']).add_to(sb_map)
                folium_static(sb_map)
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
                ydp_map = g.Map(location=[37.52361111, 126.8983417], zoom_start=13)
                for i in range(len(df_ydp)):
                    marker01 = g.Marker([df_ydp.iloc[i]['lat'], df_ydp.iloc[i]['lon']], tooltip=df_ydp.iloc[i]['시설명']).add_to(ydp_map)
                folium_static(ydp_map)
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
                sc_map = g.Map(location=[37.48078611, 127.0348111], zoom_start=13)
                for i in range(len(df_sc)):
                    marker01 = g.Marker([df_sc.iloc[i]['lat'], df_sc.iloc[i]['lon']], tooltip=df_sc.iloc[i]['시설명']).add_to(sc_map)
                folium_static(sc_map)
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
                yc_map = g.Map(location=[37.51423056, 126.8687083], zoom_start=13)
                for i in range(len(df_yc)):
                    marker01 = g.Marker([df_yc.iloc[i]['lat'], df_yc.iloc[i]['lon']], tooltip=df_yc.iloc[i]['시설명']).add_to(yc_map)
                folium_static(yc_map)
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
                kn_map = g.Map(location=[37.514575, 127.0495556], zoom_start=13)
                for i in range(len(df_kn)):
                    marker01 = g.Marker([df_kn.iloc[i]['lat'], df_kn.iloc[i]['lon']], tooltip=df_kn.iloc[i]['시설명']).add_to(kn_map)
                folium_static(kn_map)
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
                kd_map = g.Map(location=[37.52736667, 127.1258639], zoom_start=13)
                for i in range(len(df_kd)):
                    marker01 = g.Marker([df_kd.iloc[i]['lat'], df_kd.iloc[i]['lon']], tooltip=df_kd.iloc[i]['시설명']).add_to(kd_map)
                folium_static(kd_map)
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
                kb_map = g.Map(location=[37.63695556, 127.0277194], zoom_start=13)
                for i in range(len(df_kb)):
                    marker01 = g.Marker([df_kb.iloc[i]['lat'], df_kb.iloc[i]['lon']], tooltip=df_kb.iloc[i]['시설명']).add_to(kb_map)
                folium_static(kb_map)
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
                ks_map = g.Map(location=[37.54815556, 126.851675], zoom_start=13)
                for i in range(len(df_ks)):
                    marker01 = g.Marker([df_ks.iloc[i]['lat'], df_ks.iloc[i]['lon']], tooltip=df_ks.iloc[i]['시설명']).add_to(ks_map)
                folium_static(ks_map)
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
                ka_map = g.Map(location=[37.47538611, 126.9538444], zoom_start=13)
                for i in range(len(df_ka)):
                    marker01 = g.Marker([df_ka.iloc[i]['lat'], df_ka.iloc[i]['lon']], tooltip=df_ka.iloc[i]['시설명']).add_to(ka_map)
                folium_static(ka_map)
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
                kr_map = g.Map(location=[37.49265, 126.8895972], zoom_start=13)
                for i in range(len(df_kr)):
                    marker01 = g.Marker([df_kr.iloc[i]['lat'], df_kr.iloc[i]['lon']], tooltip=df_kr.iloc[i]['시설명']).add_to(kr_map)
                folium_static(kr_map)
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
                kc_map = g.Map(location=[37.44910833, 126.9041972], zoom_start=13)
                for i in range(len(df_kc)):
                    marker01 = g.Marker([df_kc.iloc[i]['lat'], df_kc.iloc[i]['lon']], tooltip=df_kc.iloc[i]['시설명']).add_to(kc_map)
                folium_static(kc_map)
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
                nw_map = g.Map(location=[37.65146111, 127.0583889], zoom_start=13)
                for i in range(len(df_nw)):
                    marker01 = g.Marker([df_nw.iloc[i]['lat'], df_nw.iloc[i]['lon']], tooltip=df_nw.iloc[i]['시설명']).add_to(nw_map)
                folium_static(nw_map)
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
                s_map = g.Map(location=[37.66583333, 127.0495222], zoom_start=13)
                for i in range(len(df_db)):
                    marker01 = g.Marker([df_db.iloc[i]['lat'], df_db.iloc[i]['lon']], tooltip=df_db.iloc[i]['시설명']).add_to(s_map)
                folium_static(s_map)
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
                s_map = g.Map(location=[37.571625, 127.0421417], zoom_start=13)
                for i in range(len(df_ddm)):
                    marker01 = g.Marker([df_ddm.iloc[i]['lat'], df_ddm.iloc[i]['lon']], tooltip=df_ddm.iloc[i]['시설명']).add_to(s_map)
                folium_static(s_map)
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
                s_map = g.Map(location=[37.50965556, 126.941575], zoom_start=13)
                for i in range(len(df_dj)):
                    marker01 = g.Marker([df_dj.iloc[i]['lat'], df_dj.iloc[i]['lon']], tooltip=df_dj.iloc[i]['시설명']).add_to(s_map)
                folium_static(s_map)
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
                s_map = g.Map(location=[37.56070556, 126.9105306], zoom_start=13)
                for i in range(len(df_mp)):
                    marker01 = g.Marker([df_mp.iloc[i]['lat'], df_mp.iloc[i]['lon']], tooltip=df_mp.iloc[i]['시설명']).add_to(s_map)
                folium_static(s_map)
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
                s_map = g.Map(location=[37.57636667, 126.9388972], zoom_start=13)
                for i in range(len(df_sdm)):
                    marker01 = g.Marker([df_sdm.iloc[i]['lat'], df_sdm.iloc[i]['lon']], tooltip=df_sdm.iloc[i]['시설명']).add_to(s_map)
                folium_static(s_map)
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
                s_map = g.Map(location=[37.53609444, 126.9675222], zoom_start=13)
                for i in range(len(df_ys)):
                    marker01 = g.Marker([df_ys.iloc[i]['lat'], df_ys.iloc[i]['lon']], tooltip=df_ys.iloc[i]['시설명']).add_to(s_map)
                folium_static(s_map)
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
                s_map = g.Map(location=[37.59996944, 126.9312417], zoom_start=13)
                for i in range(len(df_ep)):
                    marker01 = g.Marker([df_ep.iloc[i]['lat'], df_ep.iloc[i]['lon']], tooltip=df_ep.iloc[i]['시설명']).add_to(s_map)
                folium_static(s_map)
                st.dataframe(seoul_ep)

def building_searching():
    st.title('시설물 검색')
    title = st.text_input('시설물 검색','')
    
    if ((title == '코엑스') | ('강남구 영동대로 513' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='코엑스')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='코엑스')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '현대백화점 무역센터점') | ('강남구 테헤란로 517' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='현대백화점 무역센터점')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='현대백화점 무역센터점')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '미아동복합청사') | ('강북구 솔매로49길14' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='미아동복합청사')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='미아동복합청사')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '장원빌딩') | ('강북구 도봉로 323' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='장원빌딩')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='장원빌딩')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '엘디타운') | ('관악구 청룡1길 27' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='엘디타운')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='엘디타운')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '서울대역 해담채') | ('관악구 관악로15길 23-12' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='서울대역 해담채')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='서울대역 해담채')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '건국대학교 부동산학관') | ('광진구 능동로120 부동산학관' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='건국대학교 부동산학관')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='건국대학교 부동산학관')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '건국대학교 신공학관') | ('광진구 능동로120 신공학관' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='건국대학교 신공학관')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='건국대학교 신공학관')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '구로아트밸리') | ('구로구 가마산로25길 9-24' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='구로아트밸리')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='구로아트밸리')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '벽산디지털밸리7차') | ('구로구 디지털로33길 50' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='벽산디지털밸리7차')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='벽산디지털밸리7차')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '사라유치원') | ('노원구 동일로198가길 13' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='사라유치원')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='사라유치원')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '성실유치원') | ('노원구 한글비석로1길 28' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='성실유치원')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='성실유치원')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '서울신화초등학교') | ('도봉구 우이천로 120' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='서울신화초등학교')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='서울신화초등학교')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '도봉기적의도서관') | ('도봉구 마들로 797' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='도봉기적의도서관')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='도봉기적의도서관')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '청계한신휴플러스') | ('동대문구 서울시립대로 14' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']=='청계한신휴플러스')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='청계한신휴플러스')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '대성스카이렉스 Ⅱ') | ('동대문구 청계천로 471' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '대성스카이렉스 Ⅱ')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='대성스카이렉스 Ⅱ')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '서울상현초등학교') | ('동작구 상도로58길 21' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '서울상현초등학교')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='서울상현초등학교')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '에스알호텔 사당') | ('동작구 동작대로1길 15' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '에스알호텔 사당')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='에스알호텔 사당')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '트루텍빌딩') | ('마포구 월드컵북로 56길 12' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '트루텍빌딩')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='트루텍빌딩')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '창업복지관') | ('마포구 매봉산로 18' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '창업복지관')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='창업복지관')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == 'KT 가좌지사') | ('서대문구 응암로 121' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== 'KT 가좌지사')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='KT 가좌지사')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '스위스그랜드호텔') | ('서대문구 연희로 353' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '스위스그랜드호텔')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='스위스그랜드호텔')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '파크빌딩') | ('서초구 반포대로27길 16' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '파크빌딩')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='파크빌딩')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '내곡동주민센터') | ('서초구 염곡말길 9' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '내곡동주민센터')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='내곡동주민센터')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '서울숲더샵') | ('성동구 왕십리로 241' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '서울숲더샵')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='서울숲더샵')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '성동도로사업소') | ('성동구 자동차시장길 41' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '성동도로사업소')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='성동도로사업소')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '센트럴타운 근린상가') | ('성북구 월계로40길 7' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '센트럴타운 근린상가')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='센트럴타운 근린상가')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '한국과학기술원') | ('성북구 월곡2동 화랑로14길 5' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '한국과학기술원')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='한국과학기술원')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '아산병원신관') | ('송파구 올림픽로43길 88' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '아산병원신관')]
        st.map(df, zoom=13)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='아산병원신관')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '잠실더샵스타파크') | ('송파구 올림픽로35가길 10' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '잠실더샵스타파크')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='잠실더샵스타파크')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == 'KT ICC 목동센터') | ('양천구 목동동로 233-5' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== 'KT ICC 목동센터')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='KT ICC 목동센터')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '성문교회비전센타') | ('양천구 목동중앙북로24길 15' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '성문교회비전센타')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='성문교회비전센타')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '코레일유통본사사옥') | ('영등포구 국회대로 612' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '코레일유통본사사옥')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='코레일유통본사사옥')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '롯지호텔') | ('영등포구 영등포로 264-11' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '롯지호텔')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='롯지호텔')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '국립중앙박물관') | ('용산구 서빙고로 137' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '국립중앙박물관')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='국립중앙박물관')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '파크타워') | ('용산구 서빙고로 67' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '파크타워')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='파크타워')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '불광동 롯데캐슬아파트') | ('은평구 불광로 64' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '불광동 롯데캐슬아파트')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='불광동 롯데캐슬아파트')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '신사두산위브') | ('은평구 갈현로1길 36' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '신사두산위브')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='신사두산위브')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == 'KT광화문빌딩East') | ('종로구 종로3길 33' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== 'KT광화문빌딩East')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='KT광화문빌딩East')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == 'KT광화문빌딩West') | ('종로구 세종대로 178' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== 'KT광화문빌딩West')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='KT광화문빌딩West')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '묵동자이아파트1단지') | ('중랑구 숙선옹주로 6-9' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '묵동자이아파트1단지')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='묵동자이아파트1단지')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '홈플러스 신내점') | ('중랑구 신내로 201' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '홈플러스 신내점')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='홈플러스 신내점')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == '서울광장') | ('중구 세종대로 110' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== '서울광장')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='서울광장')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif ((title == 'DDP') | ('중구 을지로7가 을지로 281' in title)):
        st.header('검색 결과')
        df = seoul.loc[(seoul['시설명']== 'DDP')]
        s_map = g.Map(location=[df['lat'], df['lon']], zoom_start=15)
        seoul_data = seoul[['지역', '시설명', '빗물 이용 예측량(mm/1년)', '빗물 이용시설 설치 적합여부[0/1]']]
        building = seoul_data.loc[(seoul_data['시설명']=='DDP')]
        do = building.loc[(building['빗물 이용시설 설치 적합여부[0/1]']==0)]
        check = do.shape[0]
        if (check == 1):
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='red')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(255,0,0); font-weight: bold; font-size: 25px; text-align: left;">부적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        else:
            marker01 = g.Marker([df['lat'], df['lon']], tooltip=title, icon=g.Icon(color='blue')).add_to(s_map)
            folium_static(s_map)
            texts = """<h2 style = "color: rgb(0,0, 255); font-weight: bold; font-size: 25px; text-align: left;">적합</h2>"""
            st.markdown(texts, unsafe_allow_html=True)
        st.dataframe(building)
    elif (title == ''):
        st.subheader('도로명 주소(시설명)을 입력하세요.')
    else:
        st.header('검색 결과가 없습니다.')
        st.subheader('다른 시설물을 검색해 주세요.')
        
pages_names_to_funcs = {'지역 검색🗺': region_searching, '시설물 검색🏢': building_searching}

selected_page = st.sidebar.selectbox('검색 방법을 골라주세요.', pages_names_to_funcs.keys())

pages_names_to_funcs[selected_page]()
# 파일실행: File > New > Terminal(anaconda prompt) - 빅프로젝트\rain.py