#If/else son condicionales para decidir de hacer  algo basado en algo que es verdadero o falso 

x=10
y=5

#Podemos usar operadores de comparacion( ==, !=, >, <, <=, >=)

if x>y:
 # print(x)
	print('{0} es mas grande que {1}'.format(x,y))
else:
 # print(y)
	print('{0} es mas menor que {1}'.format(x,y))
	print('---------')

if x>y:
 # print(x)
	print('{0} es mas grande que {1}'.format(x,y))
elif x==y:
 # print('x y y son iguales')
	print('{0} es igual  que {1}'.format(x,y))
else:
 # print(y)
	print('{0} es menor que {1}'.format(x,y))
#if anidados
if x >2:
 if x<=10:
	print('{0} es mas grande que 2 e igual/menor a 10'.format(x))
#la mejor forma de hacerlo es uasando operadores logicos
#and
if x>2 and x<=10:
	print('{0} es mas grande que 2 e igual/menor a 10'.format(x))
#or
if x>2 or x<=10:
	print('{0} es mas grande que 2 e igual/menor a 10'.format(x))
if not(x==y):
	print('{0} no es igual a {1}'.format(x,y))
