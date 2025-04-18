#  check odd even #
# num = int(input('Enter Numner'))

# if num%2 == 0:
#     print('even')
# else:
#     print('odd')

#check vowel #

char = input('Enter a character: ').lower()

if len(char) == 1 and char.isalpha():
    if char in ['a', 'e', 'i', 'o', 'u']:
        print('It\'s a vowel')
    else:
        print('It\'s a consonant')
else:
    print('Please enter a single alphabet character.')





    