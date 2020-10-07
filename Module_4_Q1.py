#Iterate through keys and values of the car_prices dictionary, printing out information about each one.

def car_listing(car_prices):
    result = ""
    for model, price in car_prices.items():
        result += "{} costs {} dollars".format(model,price) + "\n"
    return result
print(car_listing({"Kia Soul" : 19000, "Lamborghini Diablo" : 55000}))


