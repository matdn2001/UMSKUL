f = open("Файлы/24_5.txt")  # Открываем файл
k = 0  # Переменная под количество строк
for s in f:  # Цикл на перебор всех строк файла
    if s.count("HZ") > s.count("DZ"):  # Проверка строки
        k += 1  # Увеличение количества подходящих строк на 1
print(k)  # Вывод ответа
