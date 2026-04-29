from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    question: str
    data: List[Dict]
    use_tool: bool
    response: str