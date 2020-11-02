import math
# 1. feladat:
print('\n 1. feladat: \n')

def divisible():
    numbers = []
    for i in range(2000,3200):
        if (i % 7 == 0) and (i != 5):
            numbers.append(i)
    return numbers

print(divisible())

#2. feladat:
print('\n 2. feladat: \n')

def counting_names():
    names = ['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']
    sum = 0
    for name in names:
        if name == 'Pista':
            sum += 1
    return sum

print(counting_names())

#3. feladat:
print('\n 3. feladat: \n')

def hellos():
    number = int(input('Adj meg egy szamot! \n'))
    for i in range(number):
        print('{0} hello'.format(i+1))

hellos()

#4. feladat:
print('\n 4. feladat: \n')
def circle():
    r = int(input('Add meg a kör sugarát! \n'))
    print(f'A kör területe: {2*r*math.pi}')
    print(f'A kör területe: {r**2*math.pi}')

circle()

#5. feladat:
print('\n 5. feladat: \n')
def sorted_list():
    names = ['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']
    names.sort()
    print('1. csoport:')
    for name in names[:int(len(names)/2)]:
        print(name)
    print('2. csoport:')
    for name in names[int(len(names)/2):]:
        print(name)

sorted_list()
