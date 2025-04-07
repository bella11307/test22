# Gemini AI 智慧問答機器人

這是一個使用 Python + Flask + Streamlit 開發的智慧問答機器人，提供 Web 介面和 CLI 版本。

## 功能特點

- Web 介面：使用 Streamlit 開發的現代化聊天介面
- CLI 版本：提供命令列介面進行測試
- 後端：使用 Flask 提供 API 服務
- AI 模型：使用 Google Gemini AI SDK 提供智能回答

## 安裝步驟

1. 克隆專案到本地
2. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方式

### 啟動後端服務

```bash
python api/app.py
```

### 啟動 Web 介面

```bash
streamlit run streamlit_app.py
```

### 使用 CLI 版本

```bash
python cli_bot.py
```

## 部署到 Vercel

1. 將專案推送到 GitHub
2. 在 Vercel 中導入專案
3. Vercel 會自動檢測配置並部署

## 注意事項

- 後端服務需要先啟動才能使用 Web 介面或 CLI 版本
- Web 介面預設在 http://localhost:8501
- 後端 API 預設在 http://localhost:5000
- API 金鑰和模型設定在 vercel.json 中配置

## 技術架構

- 後端：Python + Flask
- 前端：Streamlit
- AI 模型：Google Gemini AI SDK
- 部署：Vercel
- 其他：python-dotenv 