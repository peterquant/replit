 x=3
if x>14:
  print('она  долгожитель')
elif x==10:
  print('у неё юбелей' )
else:
  print("она не долгожитель")
print('финиш')


print('Сколько тебе лет')
t = input()
t = int(t)
print(t + 2)

n = input()
n= int(n)
if n==1 or n==2 or n==12:
  print("зима")
elif n==3 or n==4 or n==5:
  print("весна")
elif n==6 or n==7 or n==8:
  print("лето")
else:
  print("осень")


x1=input()
x1=int(x1)
x2=input()
x2=int(x2)
x3=input()
x3=int(x3)
y=0
if x1>0:
  y=y+1
if x2>0:
  y=y+1
if x3>0:
  y=y+1
print(y)

print('                  Добро пожаловать - КАЛЬКУЛЯТОР    ')
print()
print('Введите первое число:')
x=input()
x=int(x)
print('Какую операцию проводим с числами? - + * /')
r=input()
print('Введите второе число:')
x1=input()
x1=int(x1)
print("Ваш ответ")
if r == '-':
  print(x-x1)
elif r=="+":
  print(x+x1)
elif r=="*":
  print(x*x1)
else:
  print(x/x1)



  ninjas=43
if ninjas>30 and ninjas<50:
  print("их слишком много")
elif ninjas<30 and ninjas>10:
  print("будет не просто но я с нисми разделаюсь")
else:
  print("я одалею этих нинзя")

  x=0
for t in range(1,6,1):
  if t%2==0:
  