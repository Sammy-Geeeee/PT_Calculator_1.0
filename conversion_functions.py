# Conversion Functions for the PT Calculator program

from math import pi


# Unit Conversion Functions
# Mass Conversions
def mass_to_kg(given_unit, quantity):  # To change masses to kg
    if given_unit == 'kg':
        return quantity
    elif given_unit == 'mg':
        return quantity / 1000**2
    elif given_unit == 'g':
        return quantity / 1000
    elif given_unit == 'T':
        return quantity * 1000
    elif given_unit == 'oz':
        return quantity / 35.274
    elif given_unit == 'lb':
        return quantity / 2.205
    elif given_unit == 'st':
        return quantity * 6.35029


def mass_from_kg(quantity):  # To change masses from kg
    kg = quantity
    mg = quantity * 1000**2
    g = quantity * 1000
    t = quantity / 1000
    oz = quantity * 35.274
    lb = quantity * 2.205
    st = quantity / 6.35029
    return {'kg': kg, 'mg': mg, 'g': g, 'T': t, 'oz': oz, 'lb': lb, 'st': st}


# Time Conversions
def time_to_s(given_unit, quantity):  # To change Times to s
    if given_unit == 's':
        return quantity
    elif given_unit == 'ms':
        return quantity / 1000
    elif given_unit == 'min':
        return quantity * 60
    elif given_unit == 'hr':
        return quantity * 60**2


def time_from_s(quantity):  # To change Times from s
    s = quantity
    ms = quantity * 1000
    min = quantity / 60
    hr = quantity / 60**2
    return {'s': s, 'ms': ms, 'min': min, 'hr': hr}


# Distance Conversions
def distance_to_m(given_unit, quantity):  # To change distance to m
    if given_unit == 'm':
        return quantity
    elif given_unit == 'mm':
        return quantity / 1000
    elif given_unit == 'cm':
        return quantity / 100
    elif given_unit == 'in':
        return quantity / 39.3701
    elif given_unit == 'yd':
        return quantity / 1.09361
    elif given_unit == 'km':
        return quantity * 1000
    elif given_unit == 'mi':
        return quantity * 1609.34


def distance_from_m(quantity):  # To change distances from m
    m = quantity
    mm = quantity * 1000
    cm = quantity * 100
    inch = quantity * 39.3701
    yd = quantity * 1.09361
    km = quantity / 1000
    mi = quantity / 1609.34
    return {'m': m, 'mm': mm, 'cm': cm, 'in': inch, 'yd': yd, 'km': km, 'mi': mi}


# Speed Conversions
def lin_speed_to_m_s(given_unit, quantity):  # To change speeds to m/s
    if given_unit == 'm/s':
        return quantity
    elif given_unit == 'm/min':
        return quantity / 60
    elif given_unit == 'mm/s':
        return quantity / 1000
    elif given_unit == 'mm/min':
        return quantity / 1000 / 60
    elif given_unit == 'km/hr':
        return quantity / 3.6
    elif given_unit == 'mi/hr':
        return quantity / 2.23694


def lin_speed_from_m_s(quantity):  # To change speeds from m/s
    m_s = quantity
    m_min = quantity * 60
    mm_s = quantity * 1000
    mm_min = quantity * 60 * 1000
    km_hr = quantity * 3.6
    mi_hr = quantity * 2.23694
    return {'m/s': m_s, 'm/min': m_min, 'mm/s': mm_s, 'mm/min': mm_min, 'km/hr': km_hr, 'mi/hr': mi_hr}


#  Rotational Speed Conversions
def rot_speed_to_rad_s(given_unit, quantity):  # To change angular velocity to rad/s
    if given_unit == 'rad/s':
        return quantity
    elif given_unit == 'rad/min':
        return quantity / 60
    elif given_unit == 'deg/s':
        return quantity * (pi/180)
    elif given_unit == 'deg/min':
        return quantity * (pi/180) / 60
    elif given_unit == 'rev/s':
        return quantity * (2*pi)
    elif given_unit == 'rev/min':
        return quantity * (2*pi) / 60
    elif given_unit == 'rev/hr':
        return quantity * (2*pi) / 60**2


def rot_speed_from_rad_s(quantity):  # To change angular velocities from rad/s
    rad_s = quantity
    rad_min = quantity * 60
    deg_s = quantity / (pi/180)
    deg_min = quantity / (pi/180) * 60
    rev_s = quantity / (2*pi)
    rev_min = quantity / (2*pi) * 60
    rev_hr = quantity / (2*pi) * 60**2
    return {'rad/s': rad_s, 'rad/min': rad_min, 'deg/s': deg_s, 'deg/min': deg_min, 'rev/s': rev_s, 'rev/min': rev_min, 'rev/hr': rev_hr}


# Acceleration Conversions
def lin_accel_to_m_s2(given_unit, quantity):  # To change acceleration to m/s2
    if given_unit == 'm/s2':
        return quantity
    elif given_unit == 'ft/s2':
        return quantity / 3.28084
    elif given_unit == 'km/hr/s':
        return quantity / 3.6
    elif given_unit == 'mi/hr/s':
        return quantity / 2.23694


def lin_accel_from_m_s2(quantity):  # To change acceleration from m/s2
    m_s2 = quantity
    ft_s2 = quantity * 3.28084
    km_hr_s = quantity * 3.6
    mi_hr_s = quantity * 23694
    return {'m/s2': m_s2, 'ft/s2': ft_s2, 'km/hr/s': km_hr_s, 'mi/hr/s': mi_hr_s}


# Force Conversions
def force_to_n(given_unit, quantity):  # To change force to N
    if given_unit == 'N':
        return quantity
    elif given_unit == 'kN':
        return quantity * 1000
    elif given_unit == 'kg.f':
        return quantity * 9.80665
    elif given_unit == 'lb.f':
        return quantity * 4.44822


def force_from_n(quantity):  # To change force from N
    n = quantity
    kn = quantity / 1000
    kg_f = quantity / 9.80665
    lb_f = quantity / 4.44822
    return {'N': n, 'kN': kn, 'kg.f': kg_f, 'lb.f': lb_f}


# Torque Conversions
def torque_to_n_m(given_unit, quantity):  # To change torque to Nm
    if given_unit == 'N.m':
        return quantity
    elif given_unit == 'kN.m':
        return quantity * 1000
    elif given_unit == 'kg.f.m':
        return quantity * 9.80665
    elif given_unit == 'lb.f.ft':
        return quantity * 1.35582
    elif given_unit == 'lb.f.in':
        return quantity * 8.85074


def torque_from_n_m(quantity):  # To change torque from Nm
    n_m = quantity
    kn_m = quantity / 1000
    kg_f_m = quantity / 9.80665
    lb_f_ft = quantity / 1.35582
    lb_f_in = quantity / 8.85074
    return {'N.m': n_m, 'kN.m': kn_m, 'kg.f.m': kg_f_m, 'lb.f.ft': lb_f_ft, 'lb.f.in': lb_f_in}


# Power Conversions
def power_to_w(given_unit, quantity):  # To change force to N
    if given_unit == 'W':
        return quantity
    elif given_unit == 'kW':
        return quantity * 1000
    elif given_unit == 'hp':
        return quantity * 745.7


def power_from_w(quantity):  # To change force from N
    w = quantity
    kw = quantity / 1000
    hp = quantity / 745.7
    return {'W': w, 'kW': kw, 'hp': hp}
