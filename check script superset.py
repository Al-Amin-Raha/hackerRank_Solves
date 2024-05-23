def check_strict_superset():
    A = set(map(int, input().split()))
    n = int(input())
    other_sets = [set(map(int, input().split())) for _ in range(n)]
    print(is_strict_superset(A, other_sets))

def is_strict_superset(A, other_sets):
    for s in other_sets:
        if not (A.issuperset(s) and A != s):
            return False
    return True

if __name__ == "__main__":
    check_strict_superset()
