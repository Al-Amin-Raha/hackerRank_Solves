from itertools import product
a = list(map(int,input().split()))
b = list(map(int,input().split()))
lst= list(product(a,b))
for l in lst:
    print(l, end=' ')