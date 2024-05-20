if __name__ == '__main__':
    N = int(input())
    list_item = []
    for _ in range(N):
        command = input().strip().split()
        if command[0] == "insert":
            list_item.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            list_item.remove(int(command[1]))
        elif command[0] == "append":
            list_item.append(int(command[1]))
        elif command[0] == "sort":
            list_item.sort()
        elif command[0] == "pop":
            list_item.pop()
        elif command[0] == "reverse":
            list_item.reverse()
        elif command[0] == "print":
            print(list_item)