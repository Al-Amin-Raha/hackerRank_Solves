n = int(input())
n_students = set(map(int, input().split()))

m = int(input())
m_students = set(map(int, input().split()))


union_set = n_students.union(m_students)

print(len(union_set))