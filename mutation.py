input()
a = set(map(int, input().split()))

n = int(input())

for _ in range(n):
    command, _ = input().split() 
    other_set = set(map(int, input().split())) 
    if command == "update":
        a.update(other_set)
    elif command == "intersection_update":
        a.intersection_update(other_set)
    elif command == "difference_update":
        a.difference_update(other_set)
    elif command == "symmetric_difference_update":
        a.symmetric_difference_update(other_set)

print(sum(a))
