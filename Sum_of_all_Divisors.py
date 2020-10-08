#Fill in the empty function so that it returns the sum of all divisors of a number, without including it. A divisor is a number that divides into another 
#without a remainder

def sum_divisors(n):
    sum = 0 #initialize variable to store denominators
    x = 1 # initialize denominator
    while n!=0 and x < n: #these 2 conditions must be true for the loop
        if n%x == 0: #this is to check if the modulo of n/x is zero
            sum = sum + x #if true, store x in variable sum
        x+=1
    return sum
print(sum_divisors(0))
print(sum_divisors(3))
print(sum_divisors(36)) # should be sum of 1+2+3+4+6+9+12+18 = 55
print(sum_divisors(102)) #should be sum of 2+3+6+17+34+51 = 114, finding out sum of the numbers that do divide by n without remainder result

