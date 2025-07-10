from langgraph.graph import StateGraph, END
from nodes import get_logs, summarize_logs
from states import LogState

builder = StateGraph(LogState)

builder.add_node("get_logs", get_logs)
builder.add_node("summarize_logs", summarize_logs)

builder.set_entry_point("get_logs")
builder.add_edge("get_logs", "summarize_logs")
builder.add_edge("summarize_logs", END)

graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke({
        "query": '{namespace="gdb-staging", container="supplier-api-server"} |= "update_3rd_logistics_status: channel_order_id:" |= "failed"',
        "start_time": "2025-07-03T00:00:00",
        "end_time": "2025-07-10T01:00:00",
        "logs": [],
        "analysis": ""
    })
    print("\n✅ GPT 分析結果：", result["analysis"])
