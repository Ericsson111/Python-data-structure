def shift_nums():
    arr = []
    new_arr = []
    for _ in range(2):
        inp = input()
        arr.append(inp)
    current = arr[0]
    new_arr.append(int(arr[0]))
    for _ in range(1,int(arr[-1])+1):
        current = int(current) * 10
        new_arr.append(current)
    return sum(new_arr)
print(shift_nums())