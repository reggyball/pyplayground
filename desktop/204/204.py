###################################################
#ARRAYS

#Show the indexes given that the number has more than one occurence
def find_x (arr, x):
    copy_arr = arr[:]
    count = copy_arr.count(x)
    location = []

    while x in copy_arr: 
        index = copy_arr.index(x)
        location.append(index)
        copy_arr[index] = 'x'
    return count, location
    
arr = [4, 8, 2, 8, 5, 2, 8, 3]
x = 8

count, location = find_x(arr, x)
print(f"Count of {x}: {count}")
print(f"Locations of {x}: {location}")