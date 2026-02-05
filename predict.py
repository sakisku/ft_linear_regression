mileage_input = input("Enter the mileage of the car: ")
if not mileage_input.replace('.', '', 1).isdigit():
    print("Please enter a valid number for mileage.")
    exit(1)
mileage = float(mileage_input)
if mileage < 0:
    print("Please enter a valid number for mileage.")
    exit(1)
    
exec(open("model.txt").read())
if 'teta0' not in locals() or 'teta1' not in locals():
    print("Model parameters are not properly defined.")
    exit(1)

if 'max_m' not in locals():
    prediction = teta0 + (teta1 * mileage)
elif 'max_m' in locals() and max_m > 0:
    prediction = teta0 + (teta1 * mileage / max_m)
print(f"Predicted price for a car with {int(mileage)} mileage is: {int(prediction)}")
