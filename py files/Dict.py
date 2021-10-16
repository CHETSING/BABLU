d1 = {}
n = int(input('Enter number of name-age pairs: '))
for i in range(n):

    name = input('Enter Name: ')
    age = int(input('Enter Age: '))
    d1.update({name:age})
print(d1)

for i in d1:
    print('Name is: ', i, end = ' ')
    print('Age is: ', d1[i])

for k,v in d1.items():
    print('Name: {} Age: {}' .format(k,v))

l1 = ['Chetan', 'Shipra', 'Moni']
l2 = [20, 35, 30]
z = zip(l1, l2)
d2 = dict(z)
print(d2)