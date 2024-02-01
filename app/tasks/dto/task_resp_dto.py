from pydantic import BaseModel


class TaskRespDto(BaseModel):
    id: int
    text: str
    status: int
