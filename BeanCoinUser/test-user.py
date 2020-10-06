# some_file.py
import json
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../models')

import block
import chain
import user

print('-------------------------------------------\n'
      '|                                         |\n'
      '|           Welcome to Beancoin           |\n'
      '|                                         |\n'
      '-------------------------------------------\n')

with open('session.json', 'r') as file:
    session = json.laod(file)

if session == []:
    print('Do you wanna to make a new account?')
    ans = input('1 - Yes, 2 - no')


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
