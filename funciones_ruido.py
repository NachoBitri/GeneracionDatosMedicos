import numpy as np
import datetime
import hashlib

def ruido():
    return np.random.randint(0, 2)

def ruidoHora():
    minuto=np.random.randint(0,59)
    segundo=np.random.randint(0,59)
    return datetime.timedelta(minutes=minuto,seconds=segundo)

def correrFecha(fecha,dias):
    nuevaFecha = fecha - datetime.timedelta(days=dias)
    return nuevaFecha

def aplicarHash(dato):
    h=hashlib.md5()
    h.update(dato.encode())
    return h.hexdigest()

