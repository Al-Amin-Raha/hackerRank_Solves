k = int(input())
room_numbers = list(map(int, input().split()))

unique_rooms = set(room_numbers)

total_sum = sum(room_numbers)

unique_sum = sum(unique_rooms)
captain_room = (unique_sum * k - total_sum) // (k - 1)

print(captain_room)
