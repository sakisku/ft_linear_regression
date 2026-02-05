import csv
import matplotlib.pyplot as plt

mileage = []
price = []

with open("data.csv", "r") as file:
    r = csv.reader(file)
    next(r)
    for row in r:
        mileage.append(float(row[0]))
        price.append(float(row[1]))

exec(open("model.txt").read())

x_line = [0, max(mileage)]
y_line = [teta0, teta0 + teta1 * max(mileage) / max_m]
plt.title('Mileage vs Price with Linear Regression')
plt.scatter(mileage, price, color='blue', label='Data')
plt.plot(x_line, y_line, color='red', label='Regression')
plt.xlabel('Mileage (miles)')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()