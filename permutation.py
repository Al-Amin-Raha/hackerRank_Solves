from itertools import permutations
s, k =input().split()
k = int(k)
lst= permutations(sorted(s), k)
for l in lst:
    print(''.join(l))