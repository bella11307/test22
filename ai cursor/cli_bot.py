import requests
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

def chat_with_ai(message):
    try:
        response = requests.post(
            "http://localhost:5000/chat",
            json={"message": message}
        )
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"錯誤: {str(e)}"

def main():
    print("歡迎使用 Gemini AI 智慧問答機器人 CLI 版本！")
    print("輸入 'quit' 或 'exit' 結束對話")
    print("-" * 50)

    while True:
        user_input = input("\n您: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("\n感謝使用，再見！")
            break
            
        print("\nAI: ", end="")
        response = chat_with_ai(user_input)
        print(response)

if __name__ == "__main__":
    main() 