#In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have
#a dictionary called "wardrobe" with items of clothing and their colours. Fill in the blanks to print a line for each item of clothing with each colour.

wardrobe = {"shirt": ["red", "blue", "white"], "jeans":["blue", "black"]}
for clothes, colours in wardrobe.items(): #first iterate through elements of the dictionary, then the list (colours)
    for colour in colours:
        print("{} {}".format(colour, clothes)) #value and key respectively
