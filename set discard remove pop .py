num_of_elements = int(input())
s = set(map(int, input().split()))
num_of_command = int(input())
for i in range(num_of_command):
    command = input().strip().split()
    if command[0] == "pop":
        s.pop()
    if command[0] == "remove":
        s.remove(int(command[1]))
    if command[0] == "discard":
        s.discard(int(command[1]))
print (len(s))