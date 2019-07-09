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
