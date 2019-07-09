#una clase es como un plano para crear objetos.
#un objeto tiene propiedades y metodos(funciones) asociadas a el

#create a class
class Usuario:

#Constructor (funcion que corre cuando haces una instalacion
	def __init__(self,nombre,email, edad):
    	    self.nombre=nombre
    	    self.email=email
            self.edad=edad
	def saludos(self,num1=1):
	    print(num1)
	    return 'Me llamo {0} y tengo {1}'.format(self.nombre,self.edad)
	def tengo_cumple(self):
	    self.edad+=1

#Init un objeto para el usuario
paloma = Usuario('PalomaTorres','palomat09@gmail.com',20)
print(type(paloma))
print(paloma.nombre)
print(paloma.saludos('d'))

paloma.tengo_cumple()
print(paloma.saludos())
print('----------')

#Extender la clase usuario
class Cliente(Usuario):
#Constructor (funcion que corre cuando haces una instanciacion de una clase) 
	def __init__(self, nombre, email, edad):
	    self.nombre= nombre
 	    self.email=email
            self.edad=edad
	    self.saldo=0

        def establecer_saldo(self,saldo):
            self.saldo=saldo
       
        def saludos(self)
            return 'Me llamo {0}, tengo {1} y mi saldo es {2}'.format(self.nombre,self.edad,self.saldo))	
#Init un cliente 

Rufina_usuario=Usuario('Rufina Madrid', 'rufinayahoo.com',2)
Rufina_cliente= Cliente('Rufina Madrid', 'rufinayahoo.com',2)
Rufina_cliente.establecer_saldo(5e10)
print(Rufina.cliente.saludos())
print(Rufina_usuario.saludos())
