def average(array):
    new_arr = set(array)
    avg = sum(new_arr)/len(new_arr)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)