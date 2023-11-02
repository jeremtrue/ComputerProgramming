import random
import time

def gettotal(num1, num2):
    total = num1 + num2
    return total

def ask():
    ans = int(input("Enter your answer:"))
    check(ans)

def check(ans):
    if ans == gettotal(num1, num2):
        print(f'You got it right!')
        time.sleep(2)
    else:
        print("You did not get it right. Try again")
        ask()

num1 = random.randint(100,999)
num2 = random.randint(100,999)

print(f'Math Quiz')
print(f'\t {num1}')
print(f'+\t {num2}')
print(f'------------')

answer = ask()

