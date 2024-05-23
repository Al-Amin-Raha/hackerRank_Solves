def is_subset(A, B):
    return A.issubset(B)
def check_subset():
    test_cases = int(input())
    for _ in range(test_cases):
        a_len = int(input())
        A = set(map(int, input().split()))
        b_len = int(input())
        B = set(map(int, input().split()))
        print(A.issubset(B))

if __name__ == "__main__":
    check_subset()
