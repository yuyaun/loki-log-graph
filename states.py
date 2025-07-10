from typing import TypedDict, List

class LogState(TypedDict):
    query: str
    start_time: str
    end_time: str
    logs: List[str]
    analysis: str
