n = int(input())
n_students = set(map(int, input().split()))

b = int(input())
b_students = set(map(int, input().split()))


diff_set = n_students.difference(b_students)

print(len(diff_set))