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

## 🐳 使用 Docker Compose 模擬日誌

本專案提供 `docker-compose.yml`，可以快速啟動 Loki、Promtail 與一個產生測試日誌的容器。

```bash
docker compose up
```

執行後，`log-generator` 容器會每秒隨機輸出 INFO、WARNING 或 ERROR 訊息，Promtail 會將這些日誌轉送到 Loki。

Promtail 透過掛載的 `/var/run/docker.sock` 讀取所有容器的 STDOUT/STDERR，
並在傳送至 Loki 時依容器名稱設定 `job` 標籤。因此 `log-generator` 的日誌可
以 `{job="log-generator"}` 為條件在 Loki 中查詢。

Loki 預設監聽在 `http://localhost:3100`，請將 `nodes.py` 中的 `LOKI_BASE_URL` 改為此網址，即可執行 `main.py` 進行日誌分析。

