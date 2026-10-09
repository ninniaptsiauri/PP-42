def user_profile(first_name: str, last_name: str, role: str = "student", is_active: bool = True) -> dict:
    user_info = {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "is_active": is_active 
    }

    return user_info

f_name: str = input("First name: ").capitalize()
l_name: str = input("Last name: ").capitalize()

user = user_profile(f_name, l_name, is_active=False, role="teacher")

print(user)



# wrong way
# def add_task(task_name: str, task_list: list = []) -> list:
#     task_list.append(task_name)
#     return task_list

# print(add_task("Do homework"))
# print(add_task("workout"))

# print(add_task("Do homework", ['workout', 'run']))



def add_task(task_name: str, task_list=None):
    if task_list is None:
        task_list = []

    task_list.append(task_name)
    return task_list

print(add_task("Do Homework"))
print(add_task("Running"))

print(add_task("Do Homework", ['workout', 'run']))