import requests
from datetime import datetime
from states import LogState
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

LOKI_BASE_URL = "http://localhost:3100"  # <- 請改成你的 Loki 網址

# 初始化 LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

def iso_to_ns(ts: str) -> str:
    dt = datetime.fromisoformat(ts)
    return str(int(dt.timestamp() * 1e9))

def get_logs(state: LogState) -> LogState:
    start_ns = iso_to_ns(state["start_time"])
    end_ns = iso_to_ns(state["end_time"])

    params = {
        "query": state["query"],
        "limit": 100,
        "direction": "backward",
        "start": start_ns,
        "end": end_ns,
    }

    url = f"{LOKI_BASE_URL}/loki/api/v1/query_range"
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {
            **state,
            "logs": [f"Error fetching logs: {response.status_code} - {response.text}"]
        }

    result = response.json().get("data", {}).get("result", [])
    print(f"Fetched {len(result)} log streams.")
    logs = []
    for stream in result:
        for ts, message in stream.get("values", []):
            logs.append(f"{ts}: {message}")

    return {
        **state,
        "logs": logs
    }

def summarize_logs(state: LogState) -> LogState:
    logs = state.get("logs", [])
    if not logs:
        analysis = "查無 log 資料。"
    else:
        prompt = PromptTemplate.from_template(
            "請閱讀以下系統日誌，摘要出可能的錯誤原因，並且將錯誤相關參數盡可能描述：\n{logs}"
        )
        input_logs = "\n".join(logs[:20])  # 避免 token 太多
        print("Input logs for analysis:", input_logs)
        analysis = llm.predict(prompt.format(logs=input_logs))

    return {
        **state,
        "analysis": analysis
    }
