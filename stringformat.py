_auth_='dev'
age = 24
print('my age is '+str(age)+' years')

print('my age is {0} years'.format(age))

print("there are {0} days in {1}, {2}".format(
    31,"Jan","March"))

print('''jan' ' ' 'feb''')

print('my age is %d %s' %(age,'years'))

for i in range(1,12):
    print("no. %2d squared is %4d and cubed is %4d"
          %(i,i**2,i**3))
print('pi is aprox %0.6f' %(22/7))


for i in range(1,12):
    print("no. {0:2} squared is {1:4} and cubed"
          "is {2:4}".format(i,i**2,i**3))

for i in range(1,12):
    print("no. {0:<2} squared is {1:<4} and cubed"
          "is {2:<4}".format(i,i**2,i**3))

    print('pi is aprox {0:0.12}'.format(22/7))

    print (5/5)