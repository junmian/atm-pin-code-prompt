"""
ATM PIN Code Prompt Program

This program verifies the user's PIN number.
To use it, run 'python atm_pin_code_prompt.py'

"""

import sys

def main():
    """
    main method
    """

    correct_pin = '5289'
    user_attempt = ''
    attempts_remaining = 3
    count = 0

    print('|----------------------------------------|')
    print('|---- Welcome to the Bank of Python! ----|')
    print('|----------------------------------------|')
    print('')

    while attempts_remaining != 0:
        attempts_remaining -= 1
        count += 1
        user_attempt = input('Please enter your PIN number: ')
        if user_attempt == correct_pin:
            print('')
            print('Your account balance is: $1,263.82. ' \
            'Thank you for using the Bank of Python. Goodbye!')
            print('')
            sys.exit()
        if attempts_remaining == 2:
            print('')
            print(f'Attempt {count}: Invalid PIN. You have {attempts_remaining} attempts left.')
            print('---------------------------------------------------------')
            print('')
            continue
        if attempts_remaining == 1:
            print('')
            print(f'Attempt {count}: Invalid PIN. You have {attempts_remaining} last attempt left.')
            print('IMPORTANT: The next invalid PIN entry will lock your account.')
            print('---------------------------------------------------------')
            print('')
            continue
        if attempts_remaining == 0:
            print('')
            print(f'Attempt {count}: Invalid PIN. Maximum login attempts exceeded. Account locked.')
            print('Please contact your nearest branch to unlock your account.' \
            ' Goodbye!')
            sys.exit()

if __name__ == '__main__':
    main()
