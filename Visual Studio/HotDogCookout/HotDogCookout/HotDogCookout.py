HOT_DOGS_PER_PACKAGE = 10
HOT_DOGS_BUNS_PER_PACKAGE = 8

attendees = int(input('Enter the number of guests: '))

hot_dogs_per_person = int(input('Hot dogs per person: '))

required_hot_dogs = attendees * hot_dogs_per_person
packages_of_hot_dogs = required_hot_dogs / HOT_DOGS_PER_PACKAGE

packages_of_hot_dog_buns = required_hot_dogs / HOT_DOGS_BUNS_PER_PACKAGE

print(f"You require {packages_of_hot_dogs} hot dog packages for the cookout.")
print(f"You require {packages_of_hot_dog_buns} buns for the cookout.")
remain_hotdogs =  required_hot_dogs % HOT_DOGS_PER_PACKAGE
if remain_hotdogs != 0:
    print(f'You have {remain_hotdogs} left over hot dogs')

remain_buns = required_hot_dogs % HOT_DOGS_BUNS_PER_PACKAGE
if remain_buns != 0:
    print(f'you have {remain_buns} left over hot dog buns. ')