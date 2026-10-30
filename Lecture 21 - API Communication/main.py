import requests
from requests.exceptions import HTTPError, ConnectTimeout
from pydantic import BaseModel
from pydantic_core._pydantic_core import ValidationError


BASE_URL = 'https://crudcrud.com/api/29c0649e26e148939cf5c9f87273d38a'

student = {
    'name': 'John',
    'age': 25,
    'grade': 'A'
}


# response = requests.post(f'{BASE_URL}/students', json=student)
# print(response)
# print(response.json())

# response = requests.get(f'{BASE_URL}/students')
# print(response.json())

# response = requests.get(f'{BASE_URL}/students/6ae4d43b210e7703e894c10')
# print(response)
# print(response.status_code)
# response.raise_for_status()
# print(response.json())
# data = response.json()
# print(data['name'])
# print(data['age'])


class Student(BaseModel):
    name: str
    age: int
    grade: str


try:
    update_stud = {
    'name': 'John',
    'age': 25,
    'grade': 'B'
    }

    response = requests.get(f'{BASE_URL}/students/6ae4d9790e887f03e8536ec4', timeout=10)

    student = Student.model_validate(response.json())

    print(student.name)
    print(student.age)

    # response = requests.put(f'{BASE_URL}/students/6ae4d43b210e7703e894c10c', json=update_stud)

    # response = requests.delete(f'{BASE_URL}/students/6ae4d43b210e7703e894c10c')

    print(response.status_code)
    response.raise_for_status()
    # print(response.json())

except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print("Server took too long")

except ValidationError as e:
    print("Pydantic error")