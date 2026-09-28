# lst = [1, 5, 7, 3, 0, 9, 6]

# lst.sort()
# print(lst)

# lst.reverse()
# print(lst)

# lst = sorted(lst)
# print(lst)


lst = []
for i in range(1, 6):
    lst.append(i)

print(lst)

lst1 = [i for i in range(1, 6) if i % 2 == 0]
print(lst1)