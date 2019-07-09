#un for loop es utilizado para iterar sobre una secuencia (puede ser una lista , un diccionario, un conjunto o un string

#simple loop
people=['Andres', 'Alejandra', 'Benito', 'Jose']
print('+++++Simple loop+++')
for person in people:
 print('Current person:{0}'.format(person))

#Break
print('++++Break loop+++')
for person in people:
    if person=='Benito':
      break
    print('Current person:{0}'.format(person))

#Continue
print('++++Continue loop+++')
for person in people:
    if person=='Benito':
       continue
    print('Current person: {0}'.format(person))
    print('Esta orden tiene que estar indentada')

#Range loop
print('++++Range loop++++')
for i in range(len(people)):
    print(people[i])

for i in range(0,18):
    print('Number:{0}'.format(i))

#While loops: hasta que se cumpla una condicion
count=0
while count<=12:
    print('Count:{0}'.format(count))
    count+=1
