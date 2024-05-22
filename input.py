x, k = map(int, input().split())
p = input()
e = p.replace('x', str(x))
result = eval(e)
if result == k:
    print(True)
else:
    print(False)
