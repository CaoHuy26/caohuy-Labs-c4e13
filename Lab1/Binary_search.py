numbers = [-10 , -6 , 1 , 5, 7, 20, 100]

x = int ( input("Enter a number: ") )

found_index = -1

start = 0
stop = len( numbers ) - 1

while start != stop:
    mid = (start + stop) // 2

    if x == numbers [mid]:
        found_index = mid
        break
    else:
        if mid == start or mid == stop:
            break

        elif x > numbers[mid]:
            start = mid

        else:
            stop = mid

if found_index == -1:
    print ("Not found")
else:
    print ("Found at: ", found_index)
