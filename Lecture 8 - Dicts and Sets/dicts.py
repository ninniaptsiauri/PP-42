empty_dct = {}
print(type(empty_dct))

empty_dct = dict()
print(type(empty_dct))

txt = 'I\'m learning Python'

txt2 = "I'm learning \"Python\""

scores = {
    "Python": 97,
    "Java": 90,
    "C++": 80
}

print(scores)


scores = dict(python=97, java=90, c=80)

print(scores)


person = {
    "name": "John",
    "age": 20,
    "city": "Tbilisi",
    "scores": [78, 90, 86],
    "is_active": True,
    "hobbies": ("coding", "reading", "skiing")
}

print(person["name"])
print(person["scores"])
print(person["country"])

first_name = person.get("name", "not found")
print(first_name)

country = person.get("country", "not found")
print(country)



scores = {
    "Python": 97,
    "Java": 90
}

scores["C++"] = 85

print(scores)

scores["Java"] = 100
print(scores)

scores.setdefault("C++", 85)
print(scores)

scores.setdefault("Java", 100)
print(scores)

scores.clear()
print(scores)

del scores["Java"]
print(scores)

removed = scores.pop("Java")
print(removed)
print(scores)


removed = scores.pop("C++", None)
print(removed)
print(scores)


removed_items = scores.popitem()
print(removed_items)

language, score = removed_items
print(language)
print(score)


scores = {
    "Python": 97,
    "Java": 90,
    "C++": 80
}

print(scores.keys())
print(scores.values())
print(scores.items())

print(len(scores))
print("Python" in scores)
print("JS" in scores)


scores = {
    "Python": 97,
    "Java": 90,
    "C++": 80
}

for i in scores:
    print(i)

for i in scores.values():
    print(i)

for key, value in scores.items():
    print(f"key: {key}, value: {value}")


lst = [i for i in range(1, 6)]
print(lst)

dct = {i: i ** 2 for i in range(1, 6) if i % 2 == 0}
print(dct)


person = {
    "name": "Anna",
    "age": 20,
    "scores": {
        "Python": 97,
        "Java": 90
    }
}

scores = person["scores"]
print(scores)

python_score = scores["Python"]
print(python_score)

print(person["scores"]["Java"])


dct1 = {"name": "John", "age": 22}
dct2 = {"name": "Anna", "city": "Tbilisi"}

dct1.update(dct2)
print(dct1)