# "===================Логические и условные операторы==================="
# # логические операторы - выражения, которые возвращают True, если выражение верное, False - если не верное

# "равенство"
# 5 == 5 # True
# 4 == 5 # False

# "не равенство"
# 4 != 5 # True
# 5 != 5 # False

# "больше"
# 5 > 4 # True
# 5 > 10 # False
# 5 > 5 # False

# "меньше"
# 5 < 4 # False
# 5 < 10 # True
# 5 < 5 # False

# "больше или равно"
# 5 >= 10 # False
# 10 >= 5 # True
# 5 >= 5 # True

# "меньше или равно"
# 10 <= 5 # False
# 5 <= 10 # True
# 5 <= 5 # True

# '5' == 5 # False
# 'hello' == 'hello' # True
# 'Hello' == 'hello' # False

# "=========================And Or Not========================="
# # and - и
# # or - или
# # not - не

# a = 5
# b = 6

# # True and True
# a == 5 and b == 6 # True

# # True and False
# a == 5 and b == 5 # False

# # False and False
# a == 4 and b == 4 # False

# # если все части выражения возвращают True - будет True
# # если хотя бы одна часть выражения False - будет False


# # True or True
# a == 5 or b == 6 # True

# # True or False
# a == 5 or b == 5 # True

# # False or False
# a == 4 or b == 4 # False

# # если хотябы одна часть выражения возыращает True - будет True


# not True # False
# not False # True
# not a == 5 # False (потому что a == 5)
# not a == 4 # True (потому что a != 4)


# "=========================Boolean Type========================="
# # Булевый тип данных имеет всего 2 значения True и False

# bool(1) # True
# bool(0) # False
# bool(-122) # True

# bool('hello') # True
# bool(' ') # True
# bool('') # False

# bool(True) # True
# bool(False) # False


# "===========================None Type==========================="
# # None - неизменяемый тип данных с одним значением None, который используется для обозначения пустоты, отсутствия значения

# bool(None) # False
# bool('None') # True (потому что это строка)

# a = None
# a is None # True (is это проверка на полное соответствие, включая тип данных)


# "=========================Условные операторы========================="
# # условные операторы - конструкция, которая используется для того, чтобы при разных входных данных код работал по разному (в зависимости от условия)

# if условие1:
#     тело1
#     # тело1 будет выполняться только если условие1 верное

# if условие1:
#     тело1
#     # тело1 будет выполняться только если условие1 верное
# else:
#     тело2
#     # тело2 будет выполняться во всех других случаях

# if условие1:
#     тело1
#     # тело1 будет выполняться только если условие1 верное
# elif условие2:
#     тело2
#     # тело2 будет выполняться только если условие1 не верное и если условие2 верное

# if условие1:
#     тело1
#     # тело1 будет выполняться только если условие1 верное
# elif условие2:
#     тело2
#     # тело2 будет выполняться только если условие1 не верное и если условие2 верное
# else:
#     тело3
#     # тело3 будет выполняться только если все вышеуказанные условия не верные


# # в одной конструкции мы можем использовать только один if
# # в одной конструкции мы можем использовать неограниченное количество elif или не использовать вообще
# # в одной конструкции мы можем использовать только один else или не использовать вообще

# num = int(input("Введите число: "))

# if num > 0:
#     print(f"число {num} - положительное")
# elif num == 0:
#     print(f"число {num} - это 0")
# else:
#     print(f"число {num} - отрицательное")


# "======================Тернарные операторы======================"
# # тернарные операторы - условия в одну строку
# тело1 if условие else тело2

# num = int(input())
# res = "Hello" if num == 5 else "Bye"
# print(res)


# "===========================FizzBuzz==========================="
# примите число от пользователя
# выведите Fizz, если число кратно 3
# выведите Buzz, если число кратно 5
# выведите FizzBuzz, если число кратно и 3, и 5
# выведите число во всех остальных случаях

"1 вариант"
num = int(input())
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

"2 вариант"
num = int(input())
if num % 15 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

"3 вариант"
num = int(input())
if not num % 15:
    print("FizzBuzz")
elif not num % 3:
    print("Fizz")
elif not num % 5:
    print("Buzz")
else:
    print(num)

"4 вариант с циклом"
for num in range(1, 16):
    if not num % 15:
        print("FizzBuzz")
    elif not num % 3:
        print("Fizz")
    elif not num % 5:
        print("Buzz")
    else:
        print(num)