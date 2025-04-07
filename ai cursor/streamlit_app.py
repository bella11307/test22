import streamlit as st
import requests
import json

# 設定頁面標題
st.set_page_config(page_title="Gemini AI 智慧問答機器人", page_icon="🤖")

# 設定標題
st.title("🤖 Gemini AI 智慧問答機器人")

# 初始化聊天歷史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 顯示聊天歷史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 用戶輸入
if prompt := st.chat_input("請輸入您的問題"):
    # 添加用戶訊息到聊天歷史
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 顯示AI思考中的訊息
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            try:
                # 發送請求到後端
                response = requests.post(
                    "http://localhost:5000/chat",
                    json={"message": prompt}
                )
                response.raise_for_status()
                ai_response = response.json()["response"]
                
                # 顯示AI回應
                st.markdown(ai_response)
                
                # 添加AI回應到聊天歷史
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                
            except Exception as e:
                st.error(f"發生錯誤: {str(e)}")

# 側邊欄
with st.sidebar:
    st.title("關於")
    st.markdown("""
    這是一個使用 Google Gemini AI 的智慧問答機器人。
    
    您可以：
    1. 在輸入框中輸入任何問題
    2. 等待AI回應
    3. 繼續對話
    
    注意：請確保後端服務（Flask）正在運行。
    """) 