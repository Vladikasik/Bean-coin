# some_file.py
import json
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../models')

import block
import chain
from user import User

print('-------------------------------------------\n'
      '|                                         |\n'
      '|           Welcome to Beancoin           |\n'
      '|                                         |\n'
      '-------------------------------------------\n')


def create_account():
    username = input('Input our username\n')

    user = User()

    user.create(username)

    print(f'Username : {user.username}')
    print(f'Address : {user.address}')


with open('session.json', 'r') as file:
    session = json.load(file)

if not session:
    print('Do you wanna to make a new account?')
    ans = input('1 - Yes, 2 - no\n')
    if ans == '2':
        exit(0)
    else:
        create_account()

# while 1:
#
#     start = input('1 - Send money\n'
#                   '2 - Watch balance\n'
#                   '3 - Watch chain\n'
#                   '0 - Exit\n')
#
#     if start == '1':
#         pass
#     elif start == '2':
#         pass
#     elif start == '3':
#         pass
#     elif start == '0': # exiting from while
#         break
#
#     else:
#         print('Try to choose correct number))')
