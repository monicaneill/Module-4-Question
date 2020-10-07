def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
   #first 2 range minus 1, last is intervals
   print("{:>3} F   |   {:>6.2f} C".format(x, to_celsius(x)))
   #using greater than operator                 #f is float number, 2 f represents 2 digits because that is how many decimals celcius uses
   #to align text to the right so that the 
   #output is neatly alligned
