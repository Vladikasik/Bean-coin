import random
import string
data = []
i = 0
while len(data) < 100:
    letters_and_digits = string.ascii_letters + string.digits
    a = ''.join((random.choice(letters_and_digits) for i in range(32)))
    if '0' in a or 'O' in a or 'I' in a or 'l' in a:
        continue
    else:
        print(len(data))
        data.append(a)

print('[')
for i in data:
    print(f'"{i}",')

print(']')