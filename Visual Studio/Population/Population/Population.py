s = int(input("Starting number of organisms: "))
i = float(input("Average daily increase[%]: "))/100.0
d = int(input("Number of days to multiply: "))
first = True
print("Day Approximate\tPopulation")
for d in range(s, d + 1):
    if first:
        print(1, '\t', s)
        first = False
    add = s * i
    s = s + add
    print(d - 1, '\t', s)