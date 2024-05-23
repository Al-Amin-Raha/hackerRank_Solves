n = int(input())
n_students = set(map(int, input().split()))

b = int(input())
b_students = set(map(int, input().split()))


intersection_set = n_students.intersection(b_students)

print(len(intersection_set))