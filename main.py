a = 7
s = 'Eshkere'
st = [5, 6, 'i' , 'l', 'i', 7, 8]
sp = [1,17,3,6,1]
kortej = ('M', 'f', 'M', 'j', 'b')
print('Число:')
print(round(a),a+1,a*52,a**2,a%2,sep=' ')
print('Cлово:')
print(s[::-1],s[2],s.upper(),s + '52',s.replace('e','812'),sep=' ')
print('Строка:')
print(len(st),ord(st[4]),chr(st[0]),st[2:5],st[1],sep=' ')
print('Список:')
sp.sort()
print(sp[1]**2,len(sp),sp*4,sum(sp),sep=' ; ')
print('Кортеж:')
print(type(kortej),kortej[:3],len(kortej),kortej.index('f'),kortej.count('M'))

import math
def plus(a):
    print('Введите значения через знак "+":')
    sm = sum(list(map(float, input().split('+'))))
    return sm
def minus(a):
    print('Введите значения через знак "-":')
    mn = list(map(float, input().split('-')))
    mi = mn[0]
    for i in range(1, len(mn)):
        mi -= mn[i]
    return mi
def mult(a):
    print('Введите значения через знак "*":')
    mlt = list(map(float, input().split('*')))
    ml = mlt[0]
    for i in range(1, len(mlt)):
        ml *= mlt[i]
    return ml
def divide(a):
    print('Введите значения через знак "/":')
    dv = list(map(float, input().split('/')))
    d = dv[0]
    for i in range(1, len(dv)):
        d /= dv[i]
    return d
def log(a):
    print('Введите значение логарифма:')
    return math.log(int(input()))
def okrug(a):
    print('Введите значение до которого надо округлить после запятой:')
    n = int(input())
    print('Теперь введите само число:')
    return round(float(input()), n)
n = True
while n == True:
    a = input(
        'Введите цифру функции, которая вам нужна ([1]сложение, [2]вычитание, [3]умножение, [4]деление, [5]натур. логарифм, [6]округление\n'
    ).lower()
    if a == '0':
        n = False
        exit
    elif a == '1':
        print(plus(a))
    elif a == '2':
        print(minus(a))
    elif a == '3':
        print(mult(a))
    elif a == '4':
        print(divide(a))
    elif a == '5':
        print(log(a))
    elif a == '6':
        print(okrug(a))
    else:
        print('Функция отсутствует')

a = 1
b = 1
n = int(input())
print(a,b,end=' ')
for i in range(2,n):
    a,b = b,a + b
    print(b,end=' ')









