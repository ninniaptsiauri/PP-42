test_list = [10, 2, 6, 5, 8, 9]

iter_list = iter(test_list)

print(iter_list)

first_item = next(iter_list)
print(first_item)

second_item = next(iter_list)
print(second_item)

for item in iter_list:
    print(item)


i = 0
while i < len(test_list):
    print(test_list[i])
    i += 1