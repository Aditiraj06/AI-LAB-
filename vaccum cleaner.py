room_A = input("Enter status of Room A (Clean/Dirty): ")
room_B = input("Enter status of Room B (Clean/Dirty): ")

position = input("Enter vacuum cleaner position (A/B): ")

room_A = room_A.lower()
room_B = room_B.lower()
position = position.upper()

print("\nInitial Environment:")
print("Room A:", room_A)
print("Room B:", room_B)
print("Vacuum Position:", position)

while room_A == "dirty" or room_B == "dirty":

    if position == "A":

        if room_A == "dirty":
            print("\nVacuum is in Room A")
            print("Action: SUCK")
            room_A = "clean"

        else:
            print("\nRoom A is clean")
            print("Action: MOVE RIGHT")
            position = "B"

    elif position == "B":

        if room_B == "dirty":
            print("\nVacuum is in Room B")
            print("Action: SUCK")
            room_B = "clean"

        else:
            print("\nRoom B is clean")
            print("Action: MOVE LEFT")
            position = "A"

print("Final Environment:")
print("Room A:", room_A)
print("Room B:", room_B)
print("Vacuum Position:", position)
print("Both rooms are clean!")

