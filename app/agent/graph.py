from langgraph.graph import StateGraph
from typing import TypedDict

from app.core.llm import llm
from app.prompts.analytic_prompt import analytic_prompt
from app.prompts.descriptive_prompt import descriptive_prompt
from app.tools.bigquery_tool import get_media_data
from app.services.formatter import format_data

# =========================
# STATE (OBRIGATÓRIO)
# =========================
class AgentState(TypedDict):
    question: str
    mode: str
    data: list
    response: str


# =========================
# 1. CLASSIFICAÇÃO
# =========================
def classify_question(state: AgentState):
    question = state["question"].lower()

    if any(word in question for word in ["volume", "quantos", "total", "quantidade"]):
        return {"mode": "descriptive"}
    
    return {"mode": "analytic"}

# =========================
# NODE DA TOOL
# =========================
def fetch_data(state: AgentState):
    print("\n🔧 TOOL CALL: BigQuery")
    data = get_media_data()
    print("✅ Dados coletados:", data)
    return {"data": data}

# =========================
# 3. GERAÇÃO DE RESPOSTA
# =========================
def generate_response(state: AgentState):
    print("\n🧠 Gerando resposta...")
    if state["mode"] == "descriptive":
        chain = descriptive_prompt | llm
    else:
        chain = analytic_prompt | llm

    formatted_data = format_data(state["data"])

    final_input = f"""
Pergunta:
{state["question"]}

Use apenas os dados abaixo:

{formatted_data}
"""

    response = chain.invoke({
        "input": final_input
    })

    print("✅ Resposta gerada")
    return {"response": response.content}


# =========================
# 4. CONSTRUÇÃO DO GRAFO
# =========================
builder = StateGraph(AgentState)

builder.add_node("classify", classify_question)
builder.add_node("fetch_data", fetch_data)
builder.add_node("generate", generate_response)

builder.set_entry_point("classify")

builder.add_edge("classify", "fetch_data")
builder.add_edge("fetch_data", "generate")

graph = builder.compile()