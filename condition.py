#1).check odd even #
# num = int(input('Enter Numner'))

# if num%2 == 0:
#     print('even')
# else:
#     print('odd')

#2).check vowel #
# char = input('Enter a character: ').lower()

# if len(char) == 1 and char.isalpha():
#     if char in ['a', 'e', 'i', 'o', 'u']:
#         print('It\'s a vowel')
#     else:
#         print('It\'s a consonant')
# else:
#     print('Please enter a single alphabet character.')

#3). Check positive , negative , zero

# num = int(input('Enter Number to Check:'))

# if num == 0:
#     print('Zero')
# elif num > 0:
#     print('Positive')
# else:
#     print('Negative')

# 4). Find greatest among three

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a >= b and a >= c:
    print(f'A is greatest: {a}')
elif b >= a and b >= c:
    print(f'B is greatest: {b}')
else:
    print(f'C is greatest: {c}')

    




    