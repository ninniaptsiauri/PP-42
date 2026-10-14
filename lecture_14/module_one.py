# import time
# import module_two
# from module_two import add

# from . import module_two
# from .module_two import add
# from . import divide

# # sum_numbers = module_two.add(2, 3)
# sum_numbers = add(2, 3)

# print(sum_numbers)

# div_numbers = divide(10, 2)
# print(div_numbers)


# import faker
from faker import Faker

fake = Faker()

print(fake.first_name())
print(fake.last_name())
print(fake.address())