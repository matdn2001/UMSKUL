f = open("Файлы/24_3.txt")  # Открываем файл
s = f.readline()  # Считываем строку
m = "Y"  # Переменная под максимальную цепочку из символов Y
while m in s:  # Пока цепочка находится в файле
    m += "Y"  # Приписываем еще одну Y
m = m[:-1]  # Срезаем одну лишнюю Y
print(len(m))  # Вывод ответа
