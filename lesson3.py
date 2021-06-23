#1
# def f_div(a, b):
#     if b == 0:
#         print("Делить на ноль нельзя!!!")
#         exit()
#     res = a / b
#     return res
# n = int(input("Num1: "))
# m = int(input("Num2: "))
# k = f_div(n, m)
# print(k)


#2
# def my_dat(name, surname, age, email, phone):
#     return name, surname, age, email, phone
# print(my_dat(name = input("Имя: "), surname = input("Фамилия: "), age = input("Возраст: "), email = input("email: "), phone = input("Телефон:")))

#3
# def my_func(a, b):
#     c = a + b
#     return c
# n = int(input("Num1: "))
# m = int(input("Num2: "))
# k = int(input("Num3: "))
# s1 = my_func(n, m)
# s2 = my_func(n, k)
# s3 = my_func(m, k)
# x = max(s1, s2, s3)
# print(x)

#4.1
# def my_func(x, y):
#     z = x ** y
#     return z
# a = float(input("Введите действительное положительное число: "))
# if a <= 0:
#     print("Введено неверное 1e число")
# b = int(input("Введите целое отрицатальное число: "))
# if b >= 0:
#     print("Введено неверное 2e число")
# c = my_func(a, b)
# print(c)


#4.2
# def my_func(x, y):
#     n = 0
#     z = 1
#     while n > y:
#         z *= 1 / x
#         n -= 1
#     return z
# a = float(input("Введите действительное положительное число: "))
# if a <= 0:
#     print("Введено неверное 1e число")
# b = int(input("Введите целое отрицатальное число: "))
# if b >= 0:
#     print("Введено неверное 2e число")
# c = my_func(a, b)
# print(c)


#5 Не смог разобраться "0" прерывает выполнение программы, все выполняется согласно заданию, но цикл не прерывается.
# s = 0
# while True:
#     print(s)
#     a = input("Введите числа для сложения через пробел, для завершения операции введите ноль: ")
#     li = a.split()
#     for x in li:
#         x = int(x)
#
#         if x != 0:
#             s += x
#         else:
#          break



#6
def my_func(a):
    print(a.title())
my_func(input("Введите слово: "))