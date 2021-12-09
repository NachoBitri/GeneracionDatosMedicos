# coding: utf-8
from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, DateTime, Integer, MetaData, Numeric, SmallInteger, String, Table, text

metadata_g = MetaData()

t_gn_equivalente = Table(
    'gn_equivalente', metadata_g,
    Column('id_antiguo',Integer,nullable=False),
    Column('id_nuevo',Integer,nullable=False),
    Column('dias_desplazados',Integer),
    schema='gn'
)