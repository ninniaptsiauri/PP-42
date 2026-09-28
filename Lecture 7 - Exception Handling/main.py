try:
    number1 = int(input("Enter a number1: "))
    number2 = int(input("Enter a number2: "))

    result = number1 / number2

    print(result)

except:
    print("Something went wrong")


try:
    for i in range(1000000000000):
        print(i)

except:
    print("Something went wrong")


for i in range(1000000000000):
    print("after exception")



try:
    number1 = float(input("Enter a number1: "))
    number2 = float(input("Enter a number2: "))

    # open("file.txt")

    result = number1 / number2

    print(result)

except ZeroDivisionError:
    print("You can't divide by zero")

except ValueError:
    print("Please enter a number")

except Exception as e:
    print(e)


try:
    lst = [1, 2, 3, 4, 5, 6, 7, 0]

    for i in lst:
        if i == 0:
            raise ValueError("Zero is not allowed")
        
except ValueError as e:
    print(e)



try:
    number1 = int(input("Enter a number1: "))
    number2 = int(input("Enter a number2: "))

    result = number1 / number2

    print(result)

except Exception as e:
    print(e)

else:
    print("Everything is fine")

finally:
    print("The code is done")


try:
    raise ArithmeticError("Something went wrong") from ZeroDivisionError("Divided by zero")

except ArithmeticError as e:
    print(e.__cause__)