def add(x,y):
    z = x + y
    print(z)

print('Which numbers do you want to add?')
a = input('Enter A Number: ')
b = input('Enter Another Number: ')

try:
    a = int(a)
    b = int(b)
    add(a,b)
except ValueError:
    print('I can\'t add ' + str(a) + ' and ' + str(b) +  ' because one or both of those aren\'t numbers!')