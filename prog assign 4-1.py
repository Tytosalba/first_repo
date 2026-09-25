# This code keeps track of bugs collected over 5 days using a loop.
bugs = 0
days = 1
while days <= 5:
    bugs_collected = int(input(f"Enter the number of bugs collected on day {days}: "))
    bugs += bugs_collected
    days += 1

print(f"Total bugs collected: {bugs}")