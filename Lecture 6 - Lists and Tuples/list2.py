lst = [1, 5, 7, 3, 0, 9, 6]

lst.sort()
print(lst)

lst.reverse()
print(lst)

lst = sorted(lst)
print(lst)


lst = []
for i in range(1, 6):
    lst.append(i)

print(lst)

lst1 = [i for i in range(1, 6) if i % 2 == 0]
print(lst1)


scores = [56, 67, 90, 38, 40, 79]

passed_scores = [i for i in scores if i >= 60]

passed_scores = [i if i >= 60 else f"{i} failed" for i in scores]

print(passed_scores)