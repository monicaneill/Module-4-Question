#The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers
def is_power_of_two(n):
    #check if numb can be divided by 2 w/o remainder
    while n%2 == 0 and n!= 0: #the divisions by 0 were causing the infinite loop, fixed with and statement
        n = n/2
        #if after dividing by 2 the number is 1, it's a power of 2
    if n==1:
        return True
    return False

print(is_power_of_two(0))
print(is_power_of_two(1))
print(is_power_of_two(8))
print(is_power_of_two(9))
