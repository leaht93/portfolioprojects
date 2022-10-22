# Bubble sort algorithm

def bubble(list_1):
    indexing_length = len(list_1) - 1
    sorted = False
    
    while not sorted:
        # Will break out of the while loop after all items are sorted
        sorted = True
        for i in range(0, indexing_length):
            # if item in list to the left is greater than an item to the right
            if list_1[i] > list_1[i+1]:
                # Says sorted variable is false
                sorted = False
                # Flips the items
                list_1[i], list_1[i+1] = list_1[i+1], list_1[i]
    return list_1

print(bubble([4,9,2,7,6]))

                