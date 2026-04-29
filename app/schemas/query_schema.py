from pydantic import BaseModel

class QueryResponse(BaseModel):
    answer: str
    
class QuestionRequest(BaseModel):
    question: str