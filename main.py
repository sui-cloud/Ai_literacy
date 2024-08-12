# 스트림릿은 웹에서 실행된다. 
import streamlit as st
import electronic0806 as ec
import pybasic as pb
import project as pr

#로그인 화면
st.sidebar.title("로그인")
user_id = st.sidebar.text_input("아이디(ID) 입력", value='abc', max_chars=10)
user_pw = st.sidebar.text_input("패스워드 입력", value='',type="password")

if user_pw=="1234" and user_id=="abc":
    st.sidebar.title("★수이의 포트폴리오★")
    #st.image("빨간머리앤셜리.jpg")

    menu  =  st.sidebar.radio("메뉴선택", ["파이썬기초","탐색적 분석: 전기자동차", "머신러닝","팀별프로젝트","수이는"],index=None)
    st.sidebar.write(menu)

    if menu=="탐색적 분석: 전기자동차":
        ec.elec_exe()
    elif menu=="머신러닝":
        st.header("공사중")    
    elif menu=="파이썬기초":
        pb.basic()
    elif menu=="팀별프로젝트":
        pr.main_food()
    elif menu=="수이는":
        st.write("수이는 파이썬언어가 어렵지만 열심히 하고 있습니다.")

        st.write("★○★--------------------------------- ★○★")
        st.write("우: 우리들은 어쩌면 만날 운명이었는지 모릅니다.")
        st.write("수: 수많은 연들이 모여서 만나진거겠죠~")
        st.write("민: 민낯으로 인사드립니다. 수이의 첫 웹입니다. 만나서 반가워요")    
        st.image("초록머리앤.jpg")    
        mean  =  st.radio("메뉴선택", ["1:우","2:수", "3:민"],index=None)
        st.write("mean")
        if mean=="1:우":
            st.image("봄꽃먹기.jpg",width=150)
        elif mean=="2:수":
            st.image("갈치한상차림.jpg",width=150)
        elif mean=="3:민":
            st.image("맛있게 웃어요.jpg",width=150)
            st.write("수이수이수이수이수이수이수이수이수이수이사랑해사랑해사랑해")
            st.image("초록머리앤.jpg")    

