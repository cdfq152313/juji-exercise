from pydantic import BaseModel


class CreateTaskDto(BaseModel):
    text: str
