from fastapi import APIRouter
from app.agent.graph import graph
from app.schemas.query_schema import QuestionRequest

router = APIRouter()

@router.post("/ask")
def ask(request: QuestionRequest):
    try:
        print("\n====================")
        print("PERGUNTA:", request.question)

        result = graph.invoke({
            "question": request.question
        })

        print("\nMODO:", result.get("mode"))
        print("\nDADOS:", result.get("data"))

        print("\nRESPOSTA DO MODELO:\n")
        print(result["response"])
        print("====================\n")

        return {
            "response": result["response"]
        }

    except Exception as e:
        print("ERRO:", str(e))
        return {"error": str(e)}
