'''
Write a program that uses nested loops to draw this pattern:

*******
******
*****
****
***
**
*

Add another nested loop to the same program to draw this pattern:

##
# #
#  #
#   #
#    #
#     #

'''

for i in range(7, 1, -1):
    for x in range(1, i):
        print('*', end='')
    print()
for r in range(7):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')