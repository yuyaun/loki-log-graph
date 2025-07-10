# Loki LangGraph Log Analysis

此專案示範如何使用 LangGraph 搭配 Loki 日誌系統與 OpenAI GPT，實現自動化錯誤分析流程。

## 📦 功能

- 查詢 Loki Logs
- GPT 自動摘要錯誤訊息
- 使用 LangGraph 流程可擴充、可維護

## 🚀 安裝與執行

```bash
git clone <repo>
cd loki_log_graph
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 設定 OpenAI API Key
export OPENAI_API_KEY=sk..

# 修改 nodes.py 中的 LOKI_BASE_URL
python main.py
```

## 🔧 範例輸出

```
✅ GPT 分析結果：發現多筆 API error，疑似資料庫連線失敗，建議檢查連線池。
```

## 🧱 架構

- `states.py`：定義流程狀態模型
- `nodes.py`：定義查詢 Loki 與分析節點
- `main.py`：組裝流程與執行
