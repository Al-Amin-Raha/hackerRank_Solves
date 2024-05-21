n, x = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(x)]
print (marks)
# transposed_marks = zip(*marks)
# average_scores = [sum(scores) / x for scores in transposed_marks]
# for score in average_scores:
#     print(score)
