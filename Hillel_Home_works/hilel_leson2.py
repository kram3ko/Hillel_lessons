print('lesson 2 excersise №1 склеить 3 цифвры в 1')
a = input('Please enter first number: ')
b = input('Please enter second number: ')
c = input('Please enter third number: ')
d=a+b+c
count=(len(d))
print('Reasult by adding strings:',d)
print('Result by delete space between numbers with sep :',a,b,c,sep='')
print('thay way print: First number: %s , second: %s, third: %s, amount %s, Fullnumber %s '%(a,b,c,count,d))
print('Please enter now 3 number with using space! example: 1 2 3')
a,b,c = map(int,input().split())
print('Умножение и сложение ввод только "int"',a*100+b*10+c*1)

print ('lesson 2 excersise №2 найти добуток 4 цифр')
a = input('Input number with 4 digit ')
b = (int(a[0])*int(a[1])*int(a[2])*int(a[-1]))
print(type(a),a,type(b),'Добуток чисел:',b)

print('lesson 2 excersise 3 перевод метов в величины ')
meters = int(input('Please input meters: '))
centimeter = meters * 100
decimetr = meters * 10
milimetr  = meters * 1000
mile = meters / 1609.34

print('In amount imputed meters: ',centimeter, 'are centimeters')
print('In amount imputed meters: ',decimetr,   'are decimetrs')
print('In amount imputed meters: ',milimetr, 'are milimeters')
print('In amount imputed meters: ',round(mile,9), 'are miles')

print('lesson 2 excersise 4 посик площади 3 угольника')
a = int(input('Введите основние треугольника '))
b = int(input('Введите высоту треугольника '))
s = (a*b)*0.5
print('Площадь треугольника равна =',s)
print('Second variant def')
def square3angle(l,h):
    return (l*h)*0.5
def vvod():
    a = int(input('Введите основние треугольника '))
    b = int(input('Введите высоту треугольника '))
    print('Площадь треугольника равна =',square3angle(a,b))
vvod()

print('lesson 2 excersise 5 разворот строки, цифр')
print('var1 type str')
a = input('Введите любое число: ')
b = a[::-1]
print(b)
print('var2 когда значние int')
a = int(input('Input 4 digit numbers: '))
b = a%10
c = a // 10 %10
d = a // 100 %10
e = a // 1000
print(b,c,d,e,sep="")
print(str(b)+str(c)+str(d)+str(e))
print('var3 просто цикличный разворот' )

a=input('enter any number, for exit type 0: ')
n = '0'
while a != n:
    print(a[::-1])
    a=input('Повторите ввод: ')

# a = 94 % 10 * 5 #'Выполнится сначала на остаток от деление потом умножение'
# x = 94 * 5 % 10 # Вот записано наоборот
# b = 4-5+2    #---------------->>>>> с лева на право
# d = 5+2-4   # **  <<<<<----- работает с права на лево
# print(a)
# print(b)
# print(x)
# print(d)