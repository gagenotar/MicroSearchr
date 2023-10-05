from pydantic import BaseModel


class MicroSearchrResponse(BaseModel):
    message: str
