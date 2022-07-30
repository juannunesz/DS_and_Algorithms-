
alphabet = [
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def linear_search(arr, item):
    for i in range(len(arr)):
        if(arr[i] == item):
            return i
    
    return -1

print(linear_search(alphabet, 'J'))

