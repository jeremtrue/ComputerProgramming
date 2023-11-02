widthone = int(input('What is the width of rectangle one: '))
heightone = int(input('What is the height of rectangle one: '))
widthtwo = int(input('What is the width of rectangle two: '))
heighttwo = int(input('What is the height of rectangle two: '))

areaone = widthone * heightone
areatwo = widthtwo * heighttwo

print(f'The area of rectangle one is',areaone)
print(f'The area of rectangle two is',areatwo)

if areaone > areatwo:
    print('Rectangle one is bigger.')
elif areatwo > areaone:
    print('Rectangle two is bigger.')
else:
    print('Both the areas are the same.')
