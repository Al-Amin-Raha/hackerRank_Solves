n = int(input())
num = input().split()
conditions = all(int(i) > 0 for i in num) and any(i == i[::-1] for i in num)
print(conditions)
