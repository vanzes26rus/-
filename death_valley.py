import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
max_temperature = []
dates = []
min_temperature = []

with open(filename) as file:
    reader = csv.reader(file)
    headings = next(reader)

    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            max_temperature_int = int(row[1])
            min_temperature_int = int(row[3])
        except ValueError:
            print("Отсутствие даты !")
        else:
            dates.append(date)
            max_temperature.append(max_temperature_int)
            min_temperature.append(min_temperature_int)
            print(date)



plt.plot(dates, min_temperature)
plt.plot(dates, max_temperature)
plt.fill_between(dates, min_temperature, max_temperature, facecolor='blue', alpha=0.1)
plt.ylabel("Температура F", fontsize=20)
plt.xlabel("Даты")
plt.title("Максималная и минимальная температура")
plt.show()