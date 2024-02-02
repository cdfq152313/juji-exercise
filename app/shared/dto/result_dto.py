from typing import TypeVar, Generic

from pydantic import BaseModel

T = TypeVar('T')


class ResultDto(BaseModel, Generic[T]):
    result: T
