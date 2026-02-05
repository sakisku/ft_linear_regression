import csv
import matplotlib.pyplot as plt
import signal

try :
    signal.signal(signal.SIGINT,
                lambda *_: (print("\nUser interrupted the program"), 
                exit(1)))
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

except FileNotFoundError:
    print("Required file not found. Please ensure 'data.csv' and 'model.txt' are present.")
except Exception as e:
    print(f"An error occurred: {e}")