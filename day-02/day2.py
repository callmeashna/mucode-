def find_second_largest(N):
    arr = [10, 5, 20, 8, 20, 3]
    
    # Extract sub-array from 0 to N
    sub_arr = arr[:N+1]
    
    largest = -1
    second_largest = -1
    
    for num in sub_arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest

# Input handling
n_input = int(input())
print(find_second_largest(n_input))