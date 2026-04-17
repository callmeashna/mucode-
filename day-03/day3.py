def move_zeros():
    # Read N (size of array)
    try:
        data = input().split()
        if not data:
            return
        
        n = int(data[0])
        # Read the array elements (handling potential formatting)
        arr = list(map(int, data[1:]))
        
        # If the input was split into two lines
        if len(arr) < n:
            arr.extend(list(map(int, input().split())))

        # 1. Move non-zero elements forward
        pos = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        
        # 2. Fill the rest of the array with zeros
        while pos < len(arr):
            arr[pos] = 0
            pos += 1

        # Output the result
        print(*(arr))

    except EOFError:
        pass

if __name__ == "__main__":
    move_zeros()