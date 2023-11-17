from pydantic import BaseModel
from typing import List
# from typing import Optional

# TODO 
# I could not for the life of me make the knowledgeGraph be an optional field.
# If you can see an easy solution I am missing, please lmk.
# Otherwise it isn't essential to the program so it's whatever.

class KnowledgeGraph(BaseModel):
    title: str | None = None
    type: str | None = None
    description: str | None = None

class SerperOrganic(BaseModel):
    title: str
    snippet: str

class SerperResponse(BaseModel):
    knowledgeGraph: KnowledgeGraph | None = None
    organic: List[SerperOrganic] | None = None

    class Config:
        # Set extra to "ignore" to ignore any extra fields not defined in the model
        extra = "ignore"