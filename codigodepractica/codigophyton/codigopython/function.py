#UNa funcion es un bloque de codigo que solo corre cuando se le llama, en python no usamos cochetes, unamos indentaciones como tabs o espacio 

#Crear a function, esta function no regresa nada solo imprime

def decirhola(nombre=''):
    print('hola {0}'.format(nombre))

decirhola('Paloma')
decirhola()

#Function que me regresa un valor 
def hacersuma(num1, num2):
    total=num1+num2
    return float(total)
hacersuma(2,3)
print(hacersuma(2,3),type(hacersuma(2,3)))

x=2
y=2

total=hacersuma(x,y)
print(total, type(total))
