#python tiene funciones para crear, leer, actualizar y eliminar archivos

#abrir un archivo 
miArchivo= open('miArchivo.txt','w')
#obtener info de este archivo

print('Name:', miArchivo.name)
print('ESta cerrado:', miArchivo.closed)
print('MOdo abierto:', miArchivo.mode)

#EScribir algo en el archivo
miArchivo.write('holakk ')
miArchivo.write('popkko')
miArchivo.close()

#agregar el archivo
miArchivo= open('miArchivo.txt','a')

miArchivo.write('y tambien c++')

