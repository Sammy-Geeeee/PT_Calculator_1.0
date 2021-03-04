# Calculation Functions for the PT Calculator program

from conversion_functions import *
from sympy import symbols, solve


# Fundamental Calculation Functions
# Force, Mass, Acceleration Calculations
def force_mass_accel_calculations(force_qty, force_unit, mass_qty, mass_unit, accel_qty, acc_unit):
    force = force_to_n(force_unit, force_qty)  # To convert all the units into Standard units
    mass = mass_to_kg(mass_unit, mass_qty)
    accel = lin_accel_to_m_s2(acc_unit, accel_qty)

    F, m, a = symbols('F m a')  # To make the symbols for the sympy equation
    equation = -F + m*a  # This needs to be equal to 0 to work here

    force_eq = solve(equation, F)[0]  # To make the equations for each variable
    mass_eq = solve(equation, m)[0]
    accel_eq = solve(equation, a)[0]

    force_calc = force_eq.subs({m: mass, a: accel})  # To sub all the values into the equations
    mass_calc = mass_eq.subs({F: force, a: accel})
    accel_calc = accel_eq.subs({F: force, m: mass})

    force_conv = force_from_n(force_calc)[force_unit]  # To convert all the units back into the user units
    mass_conv = mass_from_kg(mass_calc)[mass_unit]
    accel_conv = lin_accel_from_m_s2(accel_calc)[acc_unit]
    return {'force': force_conv, 'mass': mass_conv, 'lin_acc': accel_conv}


# Torque, Force, Diameter Calculations
def tor_force_dia_calculations(tor_qty, tor_unit, force_qty, force_unit, dia_qty, dia_unit):
    tor = torque_to_n_m(tor_unit, tor_qty)  # To convert all the units into Standard units
    force = force_to_n(force_unit, force_qty)
    dia = distance_to_m(dia_unit, dia_qty)

    T, F, D = symbols('T F D')  # To make the symbols for the sympy equation
    equation = -T + F*D/2

    tor_eq = solve(equation, T)[0]  # To make the equations for each variable
    force_eq = solve(equation, F)[0]
    dia_eq = solve(equation, D)[0]

    tor_calc = tor_eq.subs({F: force, D: dia})  # To sub all the values into the equations
    force_calc = force_eq.subs({T: tor, D: dia})
    dia_calc = dia_eq.subs({T: tor, F: force})

    tor_conv = torque_from_n_m(tor_calc)[tor_unit]  # To convert all the units back into the user units
    force_conv = force_from_n(force_calc)[force_unit]
    dia_conv = distance_from_m(dia_calc)[dia_unit]
    return {'torque': tor_conv, 'force': force_conv, 'dist': dia_conv}


# Linear Speed, Diameter, Rotational Speed Calculations
def linspd_dia_rotspd_calculations(linspd_qty, linspd_unit, dia_qty, dia_unit, rotspd_qty, rotspd_unit):
    linspd = lin_speed_to_m_s(linspd_unit, linspd_qty)  # To convert all the units into Standard units
    dia = distance_to_m(dia_unit, dia_qty)
    rotspd = rot_speed_to_rad_s(rotspd_unit, rotspd_qty)

    V, d, w = symbols('V d w')  # To make the symbols for the sympy equation
    equation = -V + (d/2)*w

    linspd_eq = solve(equation, V)[0]  # To make the equations for each variable
    dia_eq = solve(equation, d)[0]
    rotspd_eq = solve(equation, w)[0]

    linspd_calc = linspd_eq.subs({d: dia, w: rotspd})  # To sub all the values into the equations
    dia_calc = dia_eq.subs({V: linspd, w: rotspd})
    rotspd_calc = rotspd_eq.subs({V: linspd, d: dia})

    linspd_conv = lin_speed_from_m_s(linspd_calc)[linspd_unit]  # To convert all the units back into the user units
    dia_conv = distance_from_m(dia_calc)[dia_unit]
    rotspd_conv = rot_speed_from_rad_s(rotspd_calc)[rotspd_unit]
    return {'lin_spd': linspd_conv, 'diameter': dia_conv, 'rot_spd': rotspd_conv}


# Torque, Force, Diameter Calculations
def pow_tor_rotspd_calculations(pow_qty, pow_unit, tor_qty, tor_unit, rotspd_qty, rotspd_unit):
    pow = power_to_w(pow_unit, pow_qty)  # To convert all the units into Standard units
    tor = torque_to_n_m(tor_unit, tor_qty)
    rotspd = rot_speed_to_rad_s(rotspd_unit, rotspd_qty)

    P, T, w = symbols('P T w')  # To make the symbols for the sympy equation
    equation = -P + T*w

    pow_eq = solve(equation, P)[0]  # To make the equations for each variable
    tor_eq = solve(equation, T)[0]
    rotspd_eq = solve(equation, w)[0]

    pow_calc = pow_eq.subs({T: tor, w: rotspd})  # To sub all the values into the equations
    tor_calc = tor_eq.subs({P: pow, w: rotspd})
    rotspd_calc = rotspd_eq.subs({P: pow, T: tor})

    pow_conv = power_from_w(pow_calc)[pow_unit]  # To convert all the units back into the user selection
    tor_conv = torque_from_n_m(tor_calc)[tor_unit]
    rotspd_conv = rot_speed_from_rad_s(rotspd_calc)[rotspd_unit]
    return {'power': pow_conv, 'torque': tor_conv, 'rot_spd': rotspd_conv}


# PT Calculation Functions
# Belt length calculations
def belt_length_calculations(belt_length, belt_length_unit, cent_dist, cent_dist_unit, diameter_1, diameter_1_unit, diameter_2, diameter_2_unit):
    len = distance_to_m(belt_length_unit, belt_length)  # To convert all the units into Standard units
    dist = distance_to_m(cent_dist_unit, cent_dist)
    dia_1 = distance_to_m(diameter_1_unit, diameter_1)
    dia_2 = distance_to_m(diameter_2_unit, diameter_2)

    L, C, D1, D2 = symbols('L C D1 D2')  # To define all the symbols in the equation
    equation = (-L) + (2*C) + (pi*((D2+D1)/2)) + (((D2-D1)**2)/(4*C))

    len_eq = solve(equation, L)[0]  # To make the equations for each variable
    dist_eq = solve(equation, C)[1]
    dia_1_eq = solve(equation, D1)[1]
    dia_2_eq = solve(equation, D2)[1]

    len_calc = len_eq.subs({C: dist, D1: dia_1, D2: dia_2})  # To sub all the values into the equations
    dist_calc = dist_eq.subs({L: len, D1: dia_1, D2: dia_2})
    dia_1_calc = dia_1_eq.subs({L: len, C: dist, D2: dia_2})
    dia_2_calc = dia_2_eq.subs({L: len, C: dist, D1: dia_1})

    len_conv = distance_from_m(len_calc)[belt_length_unit]  # To convert all the units back into the user selection
    dist_conv = distance_from_m(dist_calc)[cent_dist_unit]
    dia_1_conv = distance_from_m(dia_1_calc)[diameter_1_unit]
    dia_2_conv = distance_from_m(dia_2_calc)[diameter_2_unit]
    return {'len': len_conv, 'dist': dist_conv, 'dia_1': dia_1_conv, 'dia_2': dia_2_conv}


# PCD, Pitch, Teeth Calculations
def pcd_pitch_teeth_calculations(pcd_dist, pcd_unit, pitch_dist, pitch_unit, teeth):
    pcd = distance_to_m(pcd_unit, pcd_dist)  # To convert all the units into Standard units
    pitch = distance_to_m(pitch_unit, pitch_dist)

    PCD, P, T = symbols('PCD P T')  # To define all the symbols in the equation
    equation = -PCD + (P * T)/pi

    pcd_eq = solve(equation, PCD)[0]  # To make the equations for each variable
    pitch_eq = solve(equation, P)[0]
    teeth_eq = solve(equation, T)[0]

    pcd_calc = pcd_eq.subs({P: pitch, T: teeth})  # To sub all the values into the equations
    pitch_calc = pitch_eq.subs({PCD: pcd, T: teeth})
    teeth_calc = teeth_eq.subs({PCD: pcd, P: pitch})

    pcd_conv = distance_from_m(pcd_calc)[pcd_unit]  # To convert all the units back into the user selection
    pitch_conv = distance_from_m(pitch_calc)[pitch_unit]
    return {'PCD': pcd_conv, 'pitch': pitch_conv, 'teeth': teeth_calc}


# Gearbox Output Calculations
def gearbox_output_calculations(tor_qty, tor_unit, pow_qty, pow_unit, rotspd_qty, rotspd_unit, ratio, eff):
    tor = torque_to_n_m(tor_unit, tor_qty)  # To convert all the units into Standard units
    pow = power_to_w(pow_unit, pow_qty)
    rotspd = rot_speed_to_rad_s(rotspd_unit, rotspd_qty)

    T, P, w, R, e = symbols('T P w R eff')  # To define all the symbols in the equation
    equation = -T + (P * R * (e/100))/w

    tor_eq = solve(equation, T)[0]  # To make the equations for each variable
    pow_eq = solve(equation, P)[0]
    rotspd_eq = solve(equation, w)[0]
    ratio_eq = solve(equation, R)[0]
    eff_eq = solve(equation, e)[0]

    tor_calc = tor_eq.subs({P: pow, w: rotspd, R: ratio, e: eff})  # To sub all the values into the equations
    pow_calc = pow_eq.subs({T: tor, w: rotspd, R: ratio, e: eff})
    rotspd_calc = rotspd_eq.subs({T: tor, P: pow, R: ratio, e: eff})
    ratio_calc = ratio_eq.subs({T: tor, P: pow, w: rotspd, e: eff})
    eff_calc = eff_eq.subs({T: tor, P: pow, w: rotspd, R: ratio})

    tor_conv = torque_from_n_m(tor_calc)[tor_unit]  # To convert all the units back into the user selection
    pow_conv = power_from_w(pow_calc)[pow_unit]
    rotspd_conv = rot_speed_from_rad_s(rotspd_calc)[rotspd_unit]
    return {'torque': tor_conv, 'power': pow_conv, 'rotspd': rotspd_conv, 'ratio': ratio_calc, 'eff': eff_calc}
