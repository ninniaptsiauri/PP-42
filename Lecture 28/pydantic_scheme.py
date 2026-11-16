from pydantic import BaseModel, Field, field_validator
from pydantic_core._pydantic_core import ValidationError
import requests

class UserRegistration(BaseModel):
    username: str
    first_name: str
    age: int = Field(ge=18, le=100)
    email: str = Field(min_length=10, max_length=50)

    @field_validator('first_name')
    @classmethod
    def validate_first_name(cls, value):
        for char in value:
            if not char.isalpha():
                raise ValueError("First name should only contain alphabetic characters")
            
        return value

try:
    user = UserRegistration(username='John12', first_name='1John', age=20, email="john@example.com")
    print(user)
except ValidationError as e:
    print(e)


print('a'.isalpha())
print('1'.isalpha())
print('@'.isalpha())


class ToDo(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool

BASE_URL = 'https://jsonplaceholder.typicode.com/todos/1'

try:
    response = requests.get(BASE_URL)
    todos = ToDo.model_validate(response.json())
    print(todos)
except ValidationError as e:
    print(e)