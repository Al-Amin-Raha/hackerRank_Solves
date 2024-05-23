import itertools

s, k = input().split()
k = int(k)
sorted_s = sorted(s)
combinations = itertools.combinations_with_replacement(sorted_s, k)

for com in combinations:
    print(''.join(com))
