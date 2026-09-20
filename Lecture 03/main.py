######################################
# String Index
######################################

word = "Python"

print(word[0])
print(word[1])
print(word[-1])
# print(word[10]) # index error 
print(word[-2])




######################################
# String Slicing
######################################

text = "Python Programming"

# print(text[0:6])
# print(text[0:8])
# print(text[-11:-1])
# print(text[-11:])
# print(text[7:])
# print(text[:7])
# print(text[0:13:3])
# print(text[::2])
# print(text[::-1])

text2 = text[:]
print(text2)


word1 = "Python"
print(id(word1))

word1 += 'Programming'
print(id(word1))

print(word1)



######################################
# String Methods
######################################

txt = '     Python is programming language     '
txt = txt.upper()
print(txt)

print(txt.lower())
print(txt.capitalize())
print(txt.title())

print(txt.strip())
print(txt.lstrip())
print(txt.rstrip())

print(txt.strip().title())

print(txt.find('Python'))

print(txt.replace('Python', 'Java'))

print(txt.split())

print(txt.index('P'))

print(txt.count('i'))

print('Hello', 'World')



######################################
# F-Strings
######################################

name = input("Enter your name: ")
print(f"Hello, {name}")

num1 = 10
num2 = 20

print(f"{num1} + {num2} = {num1 + num2}")


print(f'{12.3454789:.3f}')
print(f'{0.85:.1%}')

