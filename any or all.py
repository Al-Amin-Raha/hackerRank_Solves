n = int(input())
nums = input().split()
conditions = all(int(i) > 0 for i in nums) and any(i == i[::-1] for i in nums)
print(conditions)
