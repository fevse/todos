from pydantic import BaseModel
from typing import List


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "for example"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Congig:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example schema 1"},
                    {"item": "Example schema 2"}
                ]
            }
        }
