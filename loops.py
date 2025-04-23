#while
# program to continue sum with 1 using while loop and exit loop while user enters value to 0

num = 1
sum = 0

while num != 0  :
    num = int(input('Enter Number : '))
    sum = sum + num
    print(f'Sum = {sum}')
else :
    print('Loop Completed')