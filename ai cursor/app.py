from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # 調用ChatGPT API
        response = requests.post(
            "https://chatgpt-api.shn.hk/v1/",
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "你是一個友善的AI助手，請用中文回答問題。"},
                    {"role": "user", "content": user_message}
                ]
            }
        )
        response.raise_for_status()
        
        # 獲取AI回應
        ai_response = response.json()["choices"][0]["message"]["content"]

        return jsonify({
            "response": ai_response
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 