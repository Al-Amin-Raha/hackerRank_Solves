n, x = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(x)]
total_marks = zip(*marks)
avg_marks = [sum(scores) / x for scores in total_marks]
for num in avg_marks:
    print(num)
