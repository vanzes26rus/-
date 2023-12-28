import csv
import matplotlib.pyplot as plt
# Чтение заголовков, первой строки в файле
filename = 'sitka_weather_07-2014.csv'
highs = []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
# Извлечение максимальных температур из файла
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)

# отображение индексов каждого заголовка
for index, column_header in enumerate(header_row):
    pass
# Построение граффика максимальных температур
# Ввиденеи данны и измененние ширины линии
plt.plot(highs, c='red',  linewidth=1)
# Назначение имени диаграммы и размера ширифта
plt.title("Максимальныx температур за июль 2014 ", fontsize=20)
# название по оси Х
plt.xlabel("", fontsize=20)
# название по оси Y
plt.ylabel("Температуры F", fontsize=20)
# оформление дилений на граффике
plt.tick_params(axis='both', labelsize=14)
# вывод изображения граффика
plt.show()