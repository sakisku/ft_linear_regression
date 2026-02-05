import csv

try:
    learningRate = 0.1
    iter = 10000

    mileage = []
    price = []

    with open("data.csv", "r") as file:
        r = csv.reader(file)
        next(r)
        for row in r:
            mileage.append(float(row[0]))
            price.append(float(row[1]))

    m = len(mileage)
    max_m = max(mileage)
    teta0 = 0.0
    teta1 = 0.0

    for i in range(iter):

        err0 = 0
        err1 = 0
        for j in range(m):
            mileage_norm = mileage[j] / max_m
            prediction = teta0 + teta1 * mileage_norm
            err = prediction - price[j]
            err0 += err
            err1 += err * mileage_norm
        tmp0 = teta0 - learningRate * (1/m) * err0
        tmp1 = teta1 - learningRate * (1/m) * err1
    
        teta0 = tmp0
        teta1 = tmp1

    with open("model.txt", "w") as file:
        file.write(f"teta0 = {teta0}\n")
        file.write(f"teta1 = {teta1}\n")
        file.write(f"max_m = {max_m}")

except FileNotFoundError:
    print("Data file not found. Please create 'data.csv' with the appropriate data.")
except Exception as e:
    print(f"An error occurred: {e}")