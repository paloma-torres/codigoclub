#CREAR UNA LISTA 
numbers=[1,2,3,4,5]
fruits=['Manzanas','naranjas','uvas','pears']

print(numbers,fruits)

#get a value of a list
print(fruits[0])

#hola

#longitud
print(len(fruits))

#Append to the list
fruits.append('mangos')
print(fruits)

#remove from the list 
fruits.remove('uvas')
print(fruits)

#insert to position
fruits.insert(2,"fresas")
print(fruits)

#remove from a position, with pop
fruits.pop(2)
print(fruits)

#revers the list
fruits.reverse()
print(fruits)


#sort alphbetically
fruits.sort()
print(fruits)

