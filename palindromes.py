#given a string s return true if it is a palindrome or falso if not
#try1
'''string1 = 'mom'

def check_palindrome(string):
    if string == string[::-1]:
        print('Is a palindrome')
    else:
        print('Not  a palindrome')

check_palindrome(string1)'''

#efficient code
string1 = 'omau'

def check_palindrome(string):
    left = 0
    right = len(string) -1

    while left < right:
        if string[left] != string[right]:
            return 'not a palindrome'
        left = left + 1
        right = right- 1
        return 'is a palindrome'
print(check_palindrome(string1))