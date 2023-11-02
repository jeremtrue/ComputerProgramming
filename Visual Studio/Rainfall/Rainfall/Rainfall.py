totalrainfall = 0

years = int(input("Enter the number of years being tracked."))

for i in range(1, years+1):
    print(f'Enter rainfall for each month in year {i}.')
    for month in range(1, 13):
        rainfall = int(input(f'Enter the ranfall for month {month}: '))
        totalrainfall += rainfall
avg = totalrainfall / (month * years)
print(avg)