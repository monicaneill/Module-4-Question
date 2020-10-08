#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of
#4097 bytes will use 4096*2 = 8192 bytes of storage. Knowing this, fill in the gaps in the calculate_storage function which calculates the total number
#of bytes needed to store a file of a given size

def calculate_storage(filesize):
    block_size = 4096
    #use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//block_size
    #use modulo operator to check if there's any remainder
    partial_block_remainder = filesize%block_size
    #Depending on whether there's a remainder or not, return the total number of bytes required to allocate enough blocks to store data
    if partial_block_remainder > 0:
        return 4096*(full_blocks+1)
    return full_blocks*4096
print(calculate_storage(1)) #should print 4096
print(calculate_storage(4096)) #should print 4096
print(calculate_storage(4097)) # should print 8192
print(calculate_storage(6000)) # should print 8192
