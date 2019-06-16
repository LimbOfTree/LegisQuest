import time

print('What is your age?')
age = input('> ')
age = int(age)

print('Some facts about you:')

time.sleep(1)
if age > 14:
    print('You can start learning how to drive.')
else:
    print('You can\'t start learning how to drive.')

time.sleep(1)
if age > 17:
    print('You can vote.')
else:
    print('You can\'t vote.')

time.sleep(1)
if age > 20:
    print('You can drink alcohol.')
else:
    print('You can\'t drink alcohol.')

time.sleep(1)
print('You are a pleb.')