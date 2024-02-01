from pydantic import BaseModel


class TaskEntity(BaseModel):
    id: int
    text: str
    status: bool
