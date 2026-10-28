import json
# import datetime
from datetime import datetime

# date_1 = datetime.datetime(2026, 10, 28, 20, 50, 10)
# print(date_1)
# print(type(date_1))

# date_2 = datetime.datetime.now()
# print(date_2)

# date_3 = datetime.date(2026, 10, 28)
# print(date_3)


data = {
    "name": "ნინი",
    "age": 24,
    "scores": (98, 96, 100),
    "datetime": datetime.now()
}

print(data)
print(type(data))

serializable_data = {
    "name": data["name"],
    "age": data["age"],
    "scores": data["scores"],
    "datetime": data["datetime"].isoformat()
}

json_str = json.dumps(serializable_data, indent=4, sort_keys=True, ensure_ascii=False)
print(json_str)
print(type(json_str))


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        
        return super().default(obj)

json_str = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False, cls=CustomEncoder)
print(json_str)


def decode_types(obj: dict):
    for key, value in obj.items():
        if isinstance(value, str):
            try:
                obj[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return obj


python_data = json.loads(json_str, object_hook=decode_types)
print(python_data)


python_data = json.loads(json_str)
print(python_data)
print(type(python_data))


with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


with open('data.json', 'r', encoding='utf-8') as file:
    python_data = json.load(file)
    print(python_data)
    print(type(python_data))


try:
    json_str = '{"age": 24, "datetime": datetime.datetime(2026, 10, 28, 21, 24, 42, 892557), "name": "ნინი", "scores": [98, 96, 100}'
    python_data = json.loads(json_str)
    print(python_data)
except json.decoder.JSONDecodeError as e:
    print(e)


class Student:
    def __init__(self, name, grade, score):
        self.name = name
        self.grade = grade
        self.score = score


    def to_dict(self):
        return {'name': self.name, 'grade': self.grade, 'score': self.score}
    
    @classmethod
    def from_dict(cls, d):
        return cls(
            name = d['name'],
            grade = d['grade'],
            score = d['score']
        )
    

    def __repr__(self):
        return (f"Student(name={self.name!r}, "
                f"grade={self.grade!r}, "
                f"score={self.score})")


stud = Student("John", 'A', 100)
print(stud)

json_data = json.dumps(stud.to_dict())
print(json_data)

python_data = Student.from_dict(json.loads(json_data))
print(python_data)
print(type(python_data))


from dataclasses import dataclass, asdict

# @dataclass
# class Student:
#     name: str
#     grade: str
#     score: int

# stud = Student("John", "A", 99)
# # print(stud)

# data = asdict(stud)

# json_data = json.dumps(data)
# # print(json_data)

# python_data = json.loads(json_data)
# print(python_data)

# restored_student = Student(**python_data)
# print(restored_student)


# class Test:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def __repr__(self):
#         return f"Test(name={self.name}, grade={self.grade})"
    

# test = Test("John", "A")
# print(test)

# test_dict = {'name': "Ana", "grade": "B"}
# test = Test(**test_dict)
# print(test)
# print(type(test))


@dataclass
class Address:
    street: str
    city: str
    country: str = "GE"

@dataclass
class Human:
    name: str
    grade: str
    score: float
    address: Address | None = None


add = Address("123 London Road", "London", "UK")
stud = Human("John", "A", 98.5, add)
print(stud)

stud_dict = asdict(stud)
json_data = json.dumps(stud_dict)
# print(json_data)

python_data = json.loads(json_data)
# stud_restored = Student(**python_data)
# print(stud_restored)

restored = Human(
    **{k: v for k, v in python_data.items()
       if k != "address"},
    address=Address(**python_data["address"])
        if python_data["address"] else None,
)

print(restored)