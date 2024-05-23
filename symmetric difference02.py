n = int(input())
n_students = set(map(int, input().split()))

b = int(input())
b_students = set(map(int, input().split()))


symmetric_diff_set = n_students.symmetric_difference(b_students)

print(len(symmetric_diff_set))