#The add prices function returns the total price of all the groceries in the dictionary.

def add_prices(basket):
    total = 0 #initialize the variable that will be used for the calculation
    for price in basket.values(): #iterating through the dictionary items
        total += price
    return round(total, 2) #limits the return value to 2 decimal places

groceries = {"bananas":1.56, "apples":2.50, "oranges":0.99, "cheese":5.44}
print(add_prices(groceries))

