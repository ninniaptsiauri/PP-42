print(bool(""))

print(list(range(1, 5)))

num = (5,)
print(type(num))

num = (5)
print(type(num))


d = {"a": 1}
print(d["b"])

print(d.get("b", "not found"))

d["b"] = 2
print(d)


nums = [1, 2, 3, 4]
removed_num = nums.pop()
print(removed_num)
print(nums)
