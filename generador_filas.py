import string
import random
from random import randint
import datetime


def generador_nombre(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def generar_sector(id):
    code = str(id)
    sector_nombre = generador_nombre()
    # print(sector_nombre)
    # print(randint(0, 10))
    f_desde = datetime.datetime(1900, 1, 1)
    # print(f_desde)
    activo = True
    ver = 1
    abr = sector_nombre[0] + sector_nombre[1]
    # print(abr)

    fila_sector = {"id": id, "code": code, "descrip": sector_nombre,
                   "f_desde": f_desde, "activo": activo, "ver": ver,
                   "abr": abr}
    return fila_sector


def generar_zbs(id_zbs, tipo, sector):
    code = str(id_zbs)
    zbs_nombre = generador_nombre()
    s_id = sector["id"]
    s_cd = sector["code"]

    f_desde = datetime.datetime(2000, 1, 1)
    activo = True
    fila_zbs = {"id": id_zbs, "code": code, "descrip": zbs_nombre,
                "sector_id": s_id, "sector_code": s_cd,
                "tipo": tipo,
                "f_desde": f_desde, "activo": activo}
    return fila_zbs


def generar_cias(id_cias, especialidad, sector, zbs):
    f_start = datetime.datetime(2000, 1, 1)
    al_cd = "AP"
    al_st = "Equipo atencion primaria"
    f_cd = 1
    alt_f_cd = 1
    f_st = "x"
    fila_cias = {"code": id_cias, "descrip": id_cias, "start_dt": f_start,  # "end_dt": 1,
                 "speciality_cd": especialidad["code"],
                 "speciality_st": especialidad["st"], "assistlevel_cd": al_cd,
                 "assistlevel_st": al_st, "facility_cd": f_cd,
                 "alt_facility_cd": alt_f_cd, "facility_st": f_st, "sector_cd": sector["code"],
                 "sector_st": sector["descrip"], "zbs_cd": zbs["code"], "zbs_st": zbs["descrip"]}
    return fila_cias


def generar_usuario(id_u, sexo, nacimiento, zbs, sector, cias):
    fila_usuario = {"id": id_u, "active": True, "sexo": sexo, "nacimiento_dt": nacimiento,
                    "zbs": zbs, "sector_cd": sector, "cias_cd": cias}
    return fila_usuario


def generar_eq(id_o, id_n, dias):
    fila_eq = {"id_antiguo": id_o, "id_nuevo": id_n, "dias_desplazados": dias}
    return fila_eq


def generar_facility(id, nombre, sector, tipo):
    if tipo == "hospital":
        facility_st = "HOSPITAL " + nombre
        type_cd = "C11"
    else:
        facility_st = "C.S. " + nombre
        type_cd = "C231"

    fila_facility = {"facility_id": id, "facility_st": facility_st, "type_cd": type_cd,
                     "sector_cd": str(sector)}
    return fila_facility


def generar_diag_ap(id, episodio, diag_cd, diag_st, diag_dt, discharge_dt, existe_f):
    if existe_f:
        diag_ap = {"id": id, "episodio": episodio, "diag_cd": diag_cd, "diag_st": diag_st,
                   "diag_dt": diag_dt, "discharge_dt": discharge_dt}
    else:
        diag_ap = {"id": id, "episodio": episodio, "diag_cd": diag_cd, "diag_st": diag_st,
                   "diag_dt": diag_dt}
    return diag_ap


def generar_visits_pc(id, cod, especialidad, fecha, cod_consulta, consulta, attention):
    visits_pc = {"id": id, "cod_especialidad": cod, "especialidad": especialidad,
                 "año_visita": fecha.year, "fecha_visita": fecha, "cod_tipo_consulta": cod_consulta,
                 "tipo_consulta": consulta, "attentiontype_cd": attention}
    return visits_pc


def generar_visits_sc(id, cod_centro, desc_centro, fecha, realizada, unidad, solicitante,
                      cod_prestacion, prestacion, prestador_servicio, prestador,
                      cod_derivacion, procedencia, radiologia):
    visits_sc = {"id": id, "cod_centro": cod_centro, "desc_centro": desc_centro,
                 "cod_hospital": cod_centro, "hospital": desc_centro,
                 "fecha_visita": fecha, "realizada": realizada, "unidad_solicitante": unidad,
                 "solicitante": solicitante, "cod_prestacion": cod_prestacion,
                 "prestacion": prestacion, "prestador_servicio": prestador_servicio,
                 "prestador": prestador, "cod_derivacion": cod_derivacion,
                 "procedencia": procedencia, "radiologia": radiologia}
    return visits_sc


def generar_fila(columnas, lista):
    fila = {}
    i = 0
    for c in columnas:
        fila.update({c: lista[i]})
        i += 1
    return fila