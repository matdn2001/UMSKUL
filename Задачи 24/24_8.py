f = open("Файлы/24_8.txt")  # Открываем файл
s = f.readline()  # Считываем строку
m = "LDR"  # Переменная под максимальную цепочку из символов LDR
while m in s:  # Пока цепочка находится в файле
    m += "LDR"  # Приписываем еще одно LDR
if m[:-1] in s:  # Если оканчивается на LD
    print(len(m[:-1]))  # Вывод ответа
elif m[:-2] in s:  # Если оканчивается на L
    print(len(m[:-2]))  # Вывод ответа
else:  # Если нет незаконченной цепочки
    print(len(m[:-3]))  # Вывод ответа
