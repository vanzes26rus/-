import csv
import matplotlib.pyplot as plt
from datetime import datetime
# Чтение заголовков, первой строки в файле
filename = 'sitka_weather_2014.csv'
highs = []
dates = []
fig = plt.figure()

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
# Извлечение максимальных температур из файла
# Чтение дат, и их форматирование
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
    print(dates)
    print(highs)

# отображение индексов каждого заголовка
for index, column_header in enumerate(header_row):
    pass

# Построение граффика максимальных температур
# Ввиденеи данны и измененние ширины линии
plt.plot(dates, highs, c='red',  linewidth=2)
# Назначение имени диаграммы и размера ширифта
plt.title("Максимальныx температур за 2014 год ", fontsize=20)
# название по оси Х
plt.xlabel("", fontsize=10)
# название по оси Y
plt.ylabel("Температуры F", fontsize=10)
# автоматическое выравнивание по X
fig.autofmt_xdate()
# оформление дилений на граффике
plt.tick_params(axis='both', labelsize=10)
# вывод изображения граффика
plt.show()
