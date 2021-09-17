# coding: utf-8
from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, DateTime, Integer, MetaData, Numeric, SmallInteger, String, Table, text

metadata = MetaData()


t_mf_assistlevel = Table(
    'mf_assistlevel', metadata,
    Column('code', CHAR(1)),
    Column('descrip', String(60)),
    schema='mfm'
)


t_mf_cias_v1 = Table(
    'mf_cias_v1', metadata,
    Column('cias_id', Integer, nullable=False),
    Column('cias_cd', String(14)),
    Column('zona_cd', String(4)),
    Column('alta_dt', Date),
    Column('baja_dt', Date),
    schema='mfm'
)


t_mf_cias_v2 = Table(
    'mf_cias_v2', metadata,
    Column('code', String(30)),
    Column('descrip', String(30)),
    Column('start_dt', Date),
    Column('end_dt', Date),
    Column('speciality_cd', String(10)),
    Column('speciality_st', String(100)),
    Column('assistlevel_cd', String(255)),
    Column('assistlevel_st', String(255)),
    Column('facility_cd', Integer),
    Column('alt_facility_cd', String(100)),
    Column('facility_st', String(100)),
    Column('sector_cd', String(30)),
    Column('sector_st', String(30)),
    Column('zbs_cd', String(10)),
    Column('zbs_st', String(100)),
    schema='mfm'
)


t_mf_cias_zona = Table(
    'mf_cias_zona', metadata,
    Column('cias_cd', String(14)),
    Column('centro_cd', String(6)),
    Column('zbs_cd', String(4)),
    Column('cat_cd', String(1)),
    Column('activo', String(1)),
    Column('id', Integer, nullable=False),
    schema='mfm'
)


t_mf_cie9 = Table(
    'mf_cie9', metadata,
    Column('diag_id', BigInteger, nullable=False),
    Column('diag_cod', String(30)),
    Column('diag_desc', String(255)),
    Column('diag_gr2', String(255)),
    Column('diag_gr1', String(255)),
    Column('diag_cod_3d', String(10)),
    Column('diag_desc_3d', String(255)),
    Column('diag_cod_4d', String(10)),
    Column('diag_desc_4d', String(255)),
    Column('rare_bl', Boolean),
    schema='mfm'
)


t_mf_clinunit = Table(
    'mf_clinunit', metadata,
    Column('code', String(6)),
    Column('descrip', String(100)),
    Column('cmbd_ref_cd', String(4)),
    schema='mfm'
)


t_mf_cmbd_tipact = Table(
    'mf_cmbd_tipact', metadata,
    Column('ta_id', String, nullable=False),
    Column('ta_desc', String),
    Column('ta_id_nor', Integer),
    schema='mfm'
)


t_mf_countries = Table(
    'mf_countries', metadata,
    Column('id', Integer, nullable=False),
    Column('from_dt', Date),
    Column('to_dt', Date),
    Column('active', Boolean),
    Column('new_id', SmallInteger),
    Column('ver', SmallInteger),
    Column('code', CHAR(3)),
    Column('descrip', String(100)),
    Column('zonamundo_cd', SmallInteger),
    Column('estado', CHAR(3)),
    Column('estado_cd', SmallInteger),
    Column('esp_europ', Boolean),
    schema='mfm'
)


t_mf_cssservice = Table(
    'mf_cssservice', metadata,
    Column('code', String(8)),
    Column('descrip', String(250)),
    Column('comment_st', String(100)),
    schema='mfm'
)


t_mf_derivation = Table(
    'mf_derivation', metadata,
    Column('derivation_id', Integer, nullable=False),
    Column('derivation_st', String(60)),
    schema='mfm'
)


t_mf_dgps = Table(
    'mf_dgps', metadata,
    Column('dgp_id', String(20)),
    Column('dgp_st', String(100)),
    schema='mfm'
)


t_mf_er_uc = Table(
    'mf_er_uc', metadata,
    Column('uc_id', BigInteger, nullable=False),
    Column('fac_id', String(6)),
    Column('uchis_cd', String(4)),
    Column('uchis_st', String(30)),
    Column('ucnor_cd', String(4)),
    Column('ucnor_st', String(30)),
    Column('uccss_cd', String(4)),
    schema='mfm'
)


t_mf_erdischargetype = Table(
    'mf_erdischargetype', metadata,
    Column('code', BigInteger, nullable=False),
    Column('descrip', String(35)),
    schema='mfm'
)


t_mf_ertriage = Table(
    'mf_ertriage', metadata,
    Column('code', Integer, nullable=False),
    Column('level', String(3)),
    Column('descrip', String(60)),
    schema='mfm'
)


t_mf_erurgencytype = Table(
    'mf_erurgencytype', metadata,
    Column('code', BigInteger, nullable=False),
    Column('descrip', String(50)),
    schema='mfm'
)


t_mf_ervisittype = Table(
    'mf_ervisittype', metadata,
    Column('code', BigInteger, nullable=False),
    Column('descrip', String(50)),
    schema='mfm'
)


t_mf_facility = Table(
    'mf_facility', metadata,
    Column('facility_id', String(7)),
    Column('facility_st', String(70)),
    Column('type_cd', String(5)),
    Column('sector_cd', String(2)),
    Column('cite_cd', String(8)),
    Column('cite_head_cd', String(8)),
    Column('hospital_bl', Boolean),
    Column('bigan_lg', Boolean),
    Column('facility_ref_cd', String(6)),
    schema='mfm'
)


t_mf_finan_cmbd = Table(
    'mf_finan_cmbd', metadata,
    Column('id', SmallInteger, nullable=False),
    Column('descrip', String(75)),
    Column('grupo', SmallInteger),
    Column('tipo', String(3)),
    schema='mfm'
)


t_mf_geo_porpk = Table(
    'mf_geo_porpk', metadata,
    Column('id_porpk', String(12)),
    Column('codvia_id', String(12)),
    Column('tipovia_cd', String(15)),
    Column('via_st', String(50)),
    Column('numero_st', String(5)),
    Column('extension', String(5)),
    Column('poblacion_id', String(12)),
    Column('poblacion_st', String(50)),
    Column('codpos_cd', String(5)),
    Column('tipoporpk_cd', String(10)),
    Column('utm30x_coord', String(20)),
    Column('utm30y_coord', String(20)),
    schema='mfm'
)


t_mf_grp_socecon = Table(
    'mf_grp_socecon', metadata,
    Column('id', Integer, nullable=False),
    Column('descrip', String(50)),
    Column('activo', Boolean),
    schema='mfm'
)


t_mf_medord = Table(
    'mf_medord', metadata,
    Column('code', String(8)),
    Column('descrip', String(60)),
    schema='mfm'
)


t_mf_neighbour = Table(
    'mf_neighbour', metadata,
    Column('cuenta', BigInteger),
    Column('ine11_cd', CHAR(11)),
    Column('ncodpos', BigInteger),
    Column('codpos', CHAR(5)),
    Column('neighbour_cd', String(20)),
    Column('comarca', String(3)),
    schema='mfm'
)


t_mf_nom_pres = Table(
    'mf_nom_pres', metadata,
    Column('codnal', String(6)),
    Column('forma_farma', String(5)),
    Column('ctaem1', Numeric),
    Column('ctaem2', Numeric),
    schema='mfm'
)


t_mf_nomenclator = Table(
    'mf_nomenclator', metadata,
    Column('id', Integer, nullable=False),
    Column('code', String(10)),
    Column('descrip', String(150)),
    Column('cod_tipo_medicamento', String(2)),
    Column('cod_principio_activo', String(7)),
    Column('cod_codigo_doe', String(6)),
    Column('cod_codigo_h', String(6)),
    Column('cod_grupo_terapeutico', String(10)),
    Column('cod_grupo_atc', String(5)),
    Column('dosis', Numeric),
    Column('unidad_dosis', String(50)),
    Column('contenido', Numeric(19, 2)),
    Column('unidad_contenido', String(60)),
    Column('cod_via_administracion', String(3)),
    Column('cod_laboratorio', String(5)),
    Column('pvp', Numeric(19, 2)),
    Column('pvl', Numeric(19, 2)),
    Column('uso_excl_hospital', BigInteger),
    Column('diag_hospital', BigInteger),
    Column('diag_hosp_sin_cpd', BigInteger),
    Column('estupefaciente', BigInteger),
    Column('generico', BigInteger, nullable=False),
    Column('sit', String(2)),
    Column('fraccion', BigInteger),
    Column('multiplo', BigInteger),
    Column('unienv', String(2)),
    Column('fecha_act', DateTime),
    Column('fecha_ini', DateTime),
    Column('fecha_fin', DateTime),
    Column('version', Integer),
    Column('ddd', Numeric(19, 4)),
    Column('imputa', String(1)),
    Column('forma_far_cd', String(5)),
    Column('ctaem1', Numeric),
    Column('ctaem2', Numeric),
    schema='mfm'
)


t_mf_nucleus = Table(
    'mf_nucleus', metadata,
    Column('ine11_cd', CHAR(11)),
    Column('ine11_st', String(50)),
    Column('town_cd', CHAR(5)),
    Column('town_st', String(50)),
    Column('county_cd', CHAR(2)),
    Column('county_st', String(50)),
    Column('x_coord', Integer),
    Column('y_coord', Integer),
    Column('height_nm', Integer),
    Column('sector_cd', CHAR(2)),
    Column('zbs_cd', CHAR(4)),
    schema='mfm'
)


t_mf_pharactivesubs = Table(
    'mf_pharactivesubs', metadata,
    Column('id', Integer, nullable=False),
    Column('desc', String(150)),
    Column('code', String(10)),
    schema='mfm'
)


t_mf_pharadmroute = Table(
    'mf_pharadmroute', metadata,
    Column('code', String(3)),
    Column('descrip', String(200)),
    schema='mfm'
)


t_mf_pharatc = Table(
    'mf_pharatc', metadata,
    Column('code', String(10)),
    Column('descrip', String(150)),
    schema='mfm'
)


t_mf_pharcode = Table(
    'mf_pharcode', metadata,
    Column('phar_id', Integer, nullable=False),
    Column('code', String(10)),
    Column('descrip', String(150)),
    Column('presentation_cd', String(10)),
    Column('presentation_st', String(250)),
    Column('pharactivesubs_cd', String(7)),
    Column('phardoe_cd', String(6)),
    Column('pharhospcode_cd', String(6)),
    Column('phartherapgrp_cd', String(10)),
    Column('pharatc_cd', String(5)),
    Column('ctaem1_cd', Numeric),
    Column('ctaem2_cd', Numeric),
    Column('hospitalary_bl', Integer),
    Column('hosp_diag_bl', Integer),
    Column('hosp_diag_no_cpd_bl', Integer),
    Column('narcotic_bl', Integer),
    Column('psycotropic_bl', Integer),
    Column('generic_bl', Integer),
    Column('situation_cd', String(2)),
    Column('impute_cd', String(1)),
    Column('phartype_cd', String(2)),
    Column('pharadmroute_cd', String(3)),
    Column('pharform_cd', String(5)),
    Column('activesubs_nm', Integer),
    Column('dose_qty_nm', Numeric),
    Column('dose_unit_cd', String(50)),
    Column('content_qty_nm', Numeric(19, 2)),
    Column('content_unit_cd', String(60)),
    Column('fraction_nm', BigInteger),
    Column('multiple_nm', BigInteger),
    Column('box_unit_cd', String(2)),
    Column('ddd_nm', Numeric(19, 4)),
    Column('dddperbox_nm', Numeric(19, 4)),
    Column('laboratory_id', String(10)),
    Column('price_public_nm', Numeric(19, 2)),
    Column('price_limited_nm', Numeric(19, 2)),
    Column('last_update_dt', DateTime),
    Column('start_dt', DateTime),
    Column('end_dt', DateTime),
    Column('version_id', Integer),
    schema='mfm'
)


t_mf_phardoe = Table(
    'mf_phardoe', metadata,
    Column('code', String(6)),
    Column('descr', String(70)),
    Column('pharactivesubs_cd', String(7)),
    Column('dose_qty_nm', Numeric(255, 10)),
    Column('dose_unit_cd', String(4)),
    Column('content_nm', Numeric(255, 10)),
    Column('content_unit_cd', String(4)),
    Column('pharpresentation_cd', String(5)),
    Column('activesubs_nm', Integer),
    Column('ddd_nm', Numeric(10, 4)),
    Column('dddbybox_nm', Numeric(10, 4)),
    Column('psycotropic_bl', Integer),
    Column('narcotic_bl', CHAR(1)),
    Column('pharadmroute_cd', String(6)),
    Column('hospitalary_bl', Integer),
    Column('ctaem1_cd', Numeric),
    Column('ctaem2_cd', Numeric),
    schema='mfm'
)


t_mf_pharpresctype = Table(
    'mf_pharpresctype', metadata,
    Column('code', CHAR(1)),
    Column('descrip', String(60)),
    schema='mfm'
)


t_mf_pharpresentation = Table(
    'mf_pharpresentation', metadata,
    Column('code', String(10)),
    Column('descr', String(150)),
    schema='mfm'
)


t_mf_phartherapgrp = Table(
    'mf_phartherapgrp', metadata,
    Column('code', String(10)),
    Column('descrip', String(150)),
    schema='mfm'
)


t_mf_phartype = Table(
    'mf_phartype', metadata,
    Column('code', String(2)),
    Column('descrip', String(50)),
    schema='mfm'
)


t_mf_population_3112 = Table(
    'mf_population_3112', metadata,
    Column('yr', Integer),
    Column('users', BigInteger),
    Column('age_nm', Numeric),
    Column('sex_cd', SmallInteger),
    Column('zbs_cd', CHAR(4)),
    Column('sector_cd', String(2)),
    Column('situser_cd', SmallInteger),
    Column('grsocecon_cd', SmallInteger),
    schema='mfm'
)


t_mf_pres_grupo_atc = Table(
    'mf_pres_grupo_atc', metadata,
    Column('gratcodigogrupoatc', Integer, nullable=False),
    Column('gratnombrelargogrupoatc', String(150)),
    Column('gratnombrecortogrupoatc', String(10)),
    schema='mfm'
)


t_mf_sector = Table(
    'mf_sector', metadata,
    Column('id', Integer, nullable=False),
    Column('code', String(2)),
    Column('descrip', String(25)),
    Column('f_desde', Date),
    Column('f_hasta', Date),
    Column('activo', Boolean),
    Column('nuevo_id', String(100)),
    Column('ver', SmallInteger),
    Column('abr', String(2)),
    schema='mfm'
)


t_mf_seram_2004 = Table(
    'mf_seram_2004', metadata,
    Column('code', String(10)),
    Column('descripcion', String(400)),
    schema='mfm'
)


t_mf_sex = Table(
    'mf_sex', metadata,
    Column('code', SmallInteger, nullable=False),
    Column('descrip', String(15)),
    Column('code_es', String(1)),
    Column('code_en', String(1)),
    schema='mfm'
)


t_mf_source = Table(
    'mf_source', metadata,
    Column('code', String(15)),
    Column('descrip', String(60)),
    Column('type_st', String(15)),
    schema='mfm'
)


t_mf_speciality = Table(
    'mf_speciality', metadata,
    Column('code', String(3)),
    Column('clinunit_cd', String(20)),
    Column('descrip', String(80)),
    schema='mfm'
)


t_mf_stroke = Table(
    'mf_stroke', metadata,
    Column('icd_version', String, nullable=False),
    Column('code', String, nullable=False),
    Column('type', CHAR(1)),
    schema='mfm'
)


t_mf_stroke_diags = Table(
    'mf_stroke_diags', metadata,
    Column('catalog_version', String, nullable=False),
    Column('code', String, nullable=False),
    Column('clean_code', String, nullable=False),
    Column('description', String),
    Column('type', String(1)),
    Column('subtype', String(3)),
    schema='mfm'
)


t_mf_stroke_procs = Table(
    'mf_stroke_procs', metadata,
    Column('\ufefficd_version', String(10)),
    Column('code', String(12)),
    Column('clean_code', String(12)),
    Column('description', String(255)),
    schema='mfm'
)


t_mf_tp_usuario = Table(
    'mf_tp_usuario', metadata,
    Column('tpusu_cd', String(5)),
    Column('tpsusu_st', String(50)),
    Column('sit_cd', BigInteger, nullable=False),
    Column('apmo_cd', String(1)),
    schema='mfm'
)


t_mf_usuarios = Table(
    'mf_usuarios', metadata,
    Column('id', Integer, nullable=False),  # , server_default=text("nextval('mfm.mf_usuarios_id_seq'::regclass)")),
    Column('from_dt', Date),
    Column('to_dt', Date),
    Column('active', Boolean),
    Column('ver', SmallInteger),
    Column('usuario_id', BigInteger),
    Column('sexo', SmallInteger),
    Column('nacimiento_dt', Date),
    Column('nacionalidad', BigInteger),
    Column('paisnac', BigInteger),
    Column('altasns_dt', Date),
    Column('altabdu_dt', Date),
    Column('zbs', Integer, nullable=False),
    Column('sector_cd', Integer),
    Column('activo_bdu', Boolean),
    Column('bajabdu_dt', Date),
    Column('exitus_dt', Date),
    Column('tpusuario', CHAR(5)),
    Column('cias_cd', BigInteger),
    Column('residencia', Boolean),
    Column('x', Numeric),
    Column('y', Numeric),
    schema='mfm'
)


t_mf_usuarios_situsuario = Table(
    'mf_usuarios_situsuario', metadata,
    Column('code', Integer, nullable=False),
    Column('descrip', String),
    schema='mfm'
)


t_mf_visittype = Table(
    'mf_visittype', metadata,
    Column('code', String(5)),
    Column('descrip', String(50)),
    schema='mfm'
)


t_mf_zbs = Table(
    'mf_zbs', metadata,
    Column('id', Integer, nullable=False),
    Column('code', String(4)),
    Column('descrip', String(50)),
    Column('sector_id', Integer),
    Column('sector_code', String(2)),
    Column('tipo', String(2)),
    Column('grado_disp', String(2)),
    Column('cod_cite', String(4)),
    Column('f_desde', Date),
    Column('f_hasta', Date),
    Column('activo', Boolean),
    Column('nuevo_id', String(100)),
    Column('ver', SmallInteger),
    schema='mfm'
)

