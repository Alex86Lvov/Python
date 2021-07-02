#1
# with open("text.txt", "w", encoding="utf-8") as f:
#     t = input("Введите несколько строк разделенных пробелами, для окончания ввода Enter")
#     li = t.split()
#     li_n = []
#     for i in li:
#         i = i + "\n"
#         li_n.append(i)
#     f.writelines(li_n)


#2
# with open("text2.txt", "r", encoding = "utf-8") as f:
#     n = 0
#     while True:
#         x = f.readline()
#         if len(x) == 0:
#             break
#         n += 1
#         t = x.split()
#         m = len(t)
#         print(m)
#     n = str(n)
#     print("Количество строк:" + n)


#3
# with open("text3.txt", "r", encoding = "utf-8") as f:
#     n = 0
#     s = 0
#     while True:
#         x = f.readline()
#         if len(x) == 0:
#             break
#         n += 1
#         t = x.split()
#         m = t[1]
#         m = int(m)
#         if m < 20000:
#             print(t[0])
#         s += m
#     p = s / n
#     print(p)


#4 получилось видимо не совсем то, что требовалось, если не преобразовывать в строку ругается, что write не работает со списком
# with open("text4.txt", "r", encoding = "utf-8") as f:
#     li = []
#     while True:
#         x = f.readline()
#         if len(x) == 0:
#             break
#         t = x.split()
#         if t[0] == "One":
#             t[0] = "Один"
#         elif t[0] == "Two":
#             t[0] = "Два"
#         elif t[0] == "Three":
#             t[0] = "Три"
#         elif t[0] == "Four":
#             t[0] = "Четыре"
#         li.append(t)
#     li = str(li)
#     with open("text4n.txt", "w", encoding="utf-8") as d:
#         d.writelines(li)


#5
# with open("text5.txt", "w", encoding="utf-8") as f:
#     s = 0
#     k = input("Введите ряд чисел разделенных пробелом, для завершения ввода Enter: ")
#     f.writelines(k)
#     x = k.split()
#     for i in x:
#         i = int(i)
#         s += i
# print(s)


#6
# with open("text6.txt", "r", encoding = "windows-1251") as f:
#     while True:
#         s = 0
#         x = f.readline()
#         if len(x) == 0:
#             break
#         k = x.split()
#         for i in k[1:]:
#             l = i.split("(")
#             n = l[0]
#             n = int(n)
#             s += n
#         s = str(s)
#         print(k[0] + s)


#7
with open("text7.txt", "r", encoding = "windows-1251") as f:
    n = 0
    s = 0
    dict_n = {}
    while True:
        x = f.readline()
        if len(x) == 0:
            break
        k = x.split()
        a = k[2]
        a = int(a)
        b = k[3]
        b = int(b)
        c = a - b
        if c > 0:
            s += c
            n += 1
        dict_n[k[0]] = c
    p = s / n
    dict_n["Average profit"] = p
    print(dict_n)
    import json
    with open("text7.json", "w", encoding = "windows-1251") as w_f:
        json.dump(dict_n, w_f)