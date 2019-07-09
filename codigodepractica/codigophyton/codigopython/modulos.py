#un modulo es basicamente un archivo que contiene un conjunto de funciones para incluir  en tu app.

import datetime
hoy=datetime.date.today()
print(hoy)

from datetime import date
hoy2=date.today()
print(hoy2)

import time
estampatemporal= time.time()
print(estampatemporal)

from time import time
estampatemporal2= time()
print(estampatemporal2)

#Modulo personalizado
import validador
from validador import validate_email

email= 'prummm@gmail.com'
if validate_email(email):
    print('el correo esta bien escrito')
else:
    print('el correo esta mal escrito')
