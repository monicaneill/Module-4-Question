#The permissions of a file in a Linux system are split into three sets of three permissions: read, write and execute for the owner, group and others. Each of 
#the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write and 1 to execute or it can be written with
#a string using the letters r, w and x or - when the permission is not granted. For example: 640 is read/write for the owner, read for the group and no 
#permissions for the others; converted into a string it would be: "rw-r-----". Fill in the blanks to make the code convert a permission in octal format into string
#format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    #Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        #check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result

print(octal_to_string(755)) #should print rwxr-xr-x
print(octal_to_string(644)) #rw-r--r--

