import string
import random
from random import randint
import datetime


def generador_nombre(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def generar_sector(id):
    code = str(id)
    sector_nombre = generador_nombre()
    #print(sector_nombre)
    #print(randint(0, 10))
    f_desde = datetime.datetime(1900, 1, 1)
    #print(f_desde)
    activo = True
    ver = 1
    abr = sector_nombre[0] + sector_nombre[1]
    #print(abr)

    fila_sector = {"id": id, "code": code, "descrip": sector_nombre,
                   "f_desde": f_desde, "activo": activo, "ver": ver,
                   "abr": abr}
    return fila_sector


def generar_zbs(id_zbs, tipo, sector):
    code = str(id_zbs)
    zbs_nombre = generador_nombre()
    s_id=sector["id"]
    s_cd=sector["code"]

    f_desde = datetime.datetime(2000, 1, 1)
    activo = True
    fila_zbs = {"id": id_zbs, "code": code, "descrip": zbs_nombre,
                "sector_id": s_id, "sector_code": s_cd,
                "tipo": tipo,
                "f_desde": f_desde, "activo": activo}
    return fila_zbs

def generar_cias(id_cias,especialidad,sector,zbs):

    f_start = datetime.datetime(2000, 1, 1)
    al_cd="AP"
    al_st="Equipo atencion primaria"
    f_cd=1
    alt_f_cd=1
    f_st="x"
    fila_cias = {"code": id_cias, "descrip": id_cias, "start_dt": f_start, #"end_dt": 1,
                 "speciality_cd": especialidad["code"],
                 "speciality_st": especialidad["st"], "assistlevel_cd": al_cd,
                 "assistlevel_st": al_st,"facility_cd": f_cd,
                 "alt_facility_cd": alt_f_cd, "facility_st": f_st, "sector_cd": sector["code"],
                 "sector_st": sector["descrip"], "zbs_cd": zbs["code"], "zbs_st":zbs["descrip"]}
    return fila_cias



