#The counter function counts down from start to stop when start is BIGGER than stop and counts UP from start to stop otherwise. Fill in the blanks to make 
#this work correctly

def counter(start,stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x -= 1 #counting down
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x+=1 #counting up
    return return_string

print(counter(1,10))
print(counter(2,1))