def cal_avg(one, two, three, four, five):
    avg = one + two + three + four + five
    return avg / 5

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

test1 = int(input('Enter your first grade: '))
test2 = int(input('Enter your second grade: '))
test3 = int(input('Enter your third grade: '))
test4 = int(input('Enter your fourth grade: '))
test5 = int(input('Enter your fith grade: '))

print(f'First grade: \t{get_grade(test1)}')
print(f'Second grade: \t{get_grade(test2)}')
print(f'Third grade: \t{get_grade(test3)}')
print(f'Fourth grade: \t{get_grade(test4)}')
print(f'Fifth grade: \t{get_grade(test5)}')

print(f'Average: \t{cal_avg(test1, test2, test3, test4, test5)}')