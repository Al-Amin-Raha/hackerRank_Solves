M = int(input())
set_M = set(map(int, input().split()))

N = int(input())
set_N = set(map(int, input().split()))

sym_diff = set_M.symmetric_difference(set_N)

for elem in sorted(sym_diff):
    print(elem)
