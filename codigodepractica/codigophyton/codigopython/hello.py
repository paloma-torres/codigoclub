#hola mundo, mi primer programa

print("hola mundo")

#Variables

x=1 #name
y=2.5 #float
name='paloma' #str
is_cool=True #bool

#Multiple definicion 
x, y, name, is_cool= (1,2.5, 'paloma', True)

#matematicas basicas 
a= x+y
print(x,y,name,is_cool,a)

#checar el tipo 
print(type(x))

#cast, e.g. x a string

x = str(x) #passing x
y = int(y) #passing y
z = float(y)

print(type(y),y)
print(type(z),z)
