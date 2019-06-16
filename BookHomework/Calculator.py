import time

def add(x,y):
    z = x + y
    print(z)

print('Which numbers do you want to add?')
input('Enter A Number: ')
print('Actually, nevermind.')
time.sleep(1)
print('You don\'t get to choose.')
time.sleep(1)
print('I\'m just going to add 45 and 55.')
time.sleep(1)

add(45,55)