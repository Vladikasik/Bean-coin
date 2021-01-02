# some_file.py
import json
import sys
import hashlib

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../models')

from block import Block
from chain import Chain
from user import User

print('-------------------------------------------\n'
      '|                                         |\n'
      '|           Welcome to Beancoin           |\n'
      '|                                         |\n'
      '-------------------------------------------\n')


def write_session(session, password):
    exit_str = session + '\n' + password
    with open('user.session', 'w') as f:
        f.write(exit_str)


with open('user.session', 'r') as file:
    try:
        session = json.loads(file.readline())
        hash_pass_from_session = file.readline()
    except:
        session = []


if not session:
    print('Do you wanna to make a new account?')
    ans = input('1 - Yes, 2 - no\n')
    if ans == '2':
        exit(0)
    else:
        username = input('Input our username\n')

        password = input('Input your password\n')

        hash = hashlib.sha1(password.encode())
        pas_hash = hash.hexdigest()

        user = User()

        user.create(username)

        print(f'Username : {user.username}')
        print(f'Address : {user.address}')

        write_session(user.get_text_to_session(), pas_hash)
else:
    user = User(session[0], session[1], session[2], session[3], session[4], session[5])
    password_inp = input(f'Write password for account {user.username}\n')
    input_pass = hashlib.sha1(password_inp.encode())
    if input_pass.hexdigest() == hash_pass_from_session:
        print('All is ok, you have successfully logged in')
        while 1:

            start = input('1 - Send money\n'
                          '2 - Watch balance\n'
                          '3 - Watch chain\n'
                          '0 - Exit\n')

            if start == '1':
                recv = input('Whom would you like to send money?\n'
                             'enter the wallet like MBkCEgCAQN2mofPACPwI47i5n5WnIwIDAQAB\n')
                am = input('What ammount of money would you like to send?\n'
                           'float number - 10.0 or 19.123123\n')

            elif start == '2':
                pass
            elif start == '3':
                pass
            elif start == '0':  # exiting from while
                break

            else:
                print('Try to choose correct number))')
