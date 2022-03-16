name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != 5:
    print(f"\nYou have {MAX_TICKETS - count} seats left")
    name = input("What's your name? ").title()
    count += 1

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets.\nThere are still "
          f"{MAX_TICKETS - count} available.")
else:
    print("\nYou have sold all the available tickets.")
