# This code keeps track of rainfall over a number of years.
year = int(input("Enter the number of years tracked: "))
total_rainfall = 0
for year in range(1, year + 1):
    print(f"Year {year}:")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        print(f"Month {month}: {rainfall} inches")
        total_rainfall += rainfall

print(f"Number of months: {year * 12}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {total_rainfall / (year * 12):.2f} inches")