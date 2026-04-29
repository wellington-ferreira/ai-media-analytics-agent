from app.tools.bigquery_tool import get_traffic_data
from app.prompts.analytic_prompt import analytic_prompt
from app.prompts.descriptive_prompt import descriptive_prompt
from app.validators.validator import validate

def decide_node(state):
    question = state["question"]

    use_tool = True

    return {**state, "use_tool": use_tool}


def tool_node(state):
    data = get_traffic_data.invoke(state["question"])
    return {**state, "data": data}


def response_node(state):
    question = state["question"]
    data = state["data"]

    if "melhor performance" in question:
        prompt = analytic_prompt
    else:
        prompt = descriptive_prompt

    response = prompt.invoke({
        "input": question,
        "data": data
    })

    validated = validate(response)

    return {**state, "response": validated}