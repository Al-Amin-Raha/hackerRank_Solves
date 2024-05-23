import itertools

s, k = input().split()
k = int(k)
sorted_s = sorted(s)

for i in range(1, k + 1):
    combinations = itertools.combinations(sorted_s, i)
    for comb in combinations:
        print(''.join(comb))
