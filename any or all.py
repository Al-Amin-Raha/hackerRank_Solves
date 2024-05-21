# Read input
n = int(input())
nums = input().split()
conditions = all(int(i) > 0 for i in nums) and any(int(i) == 5 for i in nums)
print(conditions)
    
    
# all_positive = all(int(x) > 0 for x in arr)
# any_palindrome = any(x == x[::-1] for x in arr)
# print(all_positive and any_palindrome)
