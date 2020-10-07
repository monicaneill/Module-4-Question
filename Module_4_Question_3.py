#The format_address function seperates out parts of the address string into new strings:
#house_number and street_name & returns "House number X is on street named Y". 

def format_address(address_string):

  address_list = address_string.split()
  number = address_list[0]
  address = address_list[1:]

  join_number = "".join(number)
  join_address = " ".join(address)
  
  return "House number {number} on street named {address}".format(number = join_number, address = join_address)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"