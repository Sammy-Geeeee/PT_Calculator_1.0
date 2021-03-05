# PT Calculator Program

# To make a better version of the messy excel spreadsheet version of this that we use at work

from tkinter import *  # To import all the tkinter functions
from tkinter.ttk import *  # To import all the ttk widgets
from calculation_functions import *  # To import all the functions I've made for doing calculations, this also imports the conversion functions as they are needed in this module too


# Program functions
# Conversion Functions
def mass_conversion(given_unit, quantity):  # Function to be passed to the entry fields to do converting
    calculated = mass_to_kg(given_unit, quantity)  # To find the base unit
    conversions = mass_from_kg(calculated)  # To change from base unit to other units

    entries = {'kg': conv_mass_entry_kg, 'mg': conv_mass_entry_mg, 'g': conv_mass_entry_g, 'T': conv_mass_entry_t, 'oz': conv_mass_entry_oz, 'lb': conv_mass_entry_lb, 'st': conv_mass_entry_st}
    del entries[given_unit]  # This will exclude the currently active unit from being edited
    for unit, entry in entries.items():
        conversion = conversions[unit]
        entry.delete(0, END)
        entry.insert(0, f'{conversion:.2f}')


def time_conversion(given_unit, quantity):  # Function to be passed to the entry fields to do converting
    calculated = time_to_s(given_unit, quantity)  # To find the base unit
    conversions = time_from_s(calculated)  # To change from base unit to other units

    entries = {'s': conv_time_entry_s, 'ms': conv_time_entry_ms, 'min': conv_time_entry_min, 'hr': conv_time_entry_hr}
    del entries[given_unit]  # This will exclude the currently active unit from being edited
    for unit, entry in entries.items():
        conversion = conversions[unit]
        entry.delete(0, END)
        entry.insert(0, f'{conversion:.2f}')


def distance_conversion(given_unit, quantity):  # Function to be passed to the entry fields to do converting
    calculated = distance_to_m(given_unit, quantity)  # To find the base unit
    conversions = distance_from_m(calculated)  # To change from base unit to other units

    entries = {'m': conv_dist_entry_m, 'mm': conv_dist_entry_mm, 'cm': conv_dist_entry_cm, 'in': conv_dist_entry_in, 'yd': conv_dist_entry_yd, 'km': conv_dist_entry_km, 'mi': conv_dist_entry_mi}
    del entries[given_unit]  # This will exclude the currently active unit from being edited
    for unit, entry in entries.items():
        conversion = conversions[unit]
        entry.delete(0, END)
        entry.insert(0, f'{conversion:.2f}')


def linear_speed_conversion(given_unit, quantity):  # This is the function that will be passed to all the speed entry fields to do the converting
    calculated = lin_speed_to_m_s(given_unit, quantity)  # This will be the m/s speed that has been calculated
    conversions = lin_speed_from_m_s(calculated)  # This will be a dictionary of all the conversions calculated

    entries = {'m/s': conv_speed_entry_m_s, 'm/min': conv_speed_entry_m_min, 'mm/s': conv_speed_entry_mm_s, 'mm/min': conv_speed_entry_mm_min, 'km/hr': conv_speed_entry_km_hr, 'mi/hr': conv_speed_entry_mi_hr}
    del entries[given_unit]  # This will exclude the currently active unit from being edited
    for unit, entry in entries.items():
        conversion = conversions[unit]
        entry.delete(0, END)
        entry.insert(0, f'{conversion:.2f}')


def rotational_speed_conversion(given_unit, quantity):  # This is the function that will be passed to all the rotational speed entry fields that need converting
    calculated = rot_speed_to_rad_s(given_unit, quantity)  # This will be the rad/s that has been calculated
    conversions = rot_speed_from_rad_s(calculated)  # This will be a dictionary of all the conversions calculated

    entries = {'rad/s': conv_rot_speed_entry_rad_s, 'rad/min': conv_rot_speed_entry_rad_min, 'deg/s': conv_rot_speed_entry_deg_s, 'deg/min': conv_rot_speed_entry_deg_min, 'rev/s': conv_rot_speed_entry_rev_s, 'rev/min': conv_rot_speed_entry_rev_min, 'rev/hr': conv_rot_speed_entry_rev_hr}
    del entries[given_unit]  # This will exclude the currently active unit from being edited
    for unit, entry in entries.items():
        conversion = conversions[unit]
        entry.delete(0, END)
        entry.insert(0, f'{conversion:.2f}')


def linear_accel_conversion(given_unit, quantity):  # This is the function that will be passed to all the rotational speed entry fields that need converting
    calculated = lin_accel_to_m_s2(given_unit, quantity)  # This will be the m/s2
    conversions = lin_accel_from_m_s2(calculated)  # This will be a dictionary of all the conversions calculated

    entries = {'m/s2': conv_lin_accel_entry_m_s2, 'ft/s2': conv_lin_accel_entry_ft_s2, 'km/hr/s': conv_lin_accel_entry_km_hr_s, 'mi/hr/s': conv_lin_accel_entry_mi_hr_s}
    del entries[given_unit]  # This will exclude the currently active unit from being edited
    for unit, entry in entries.items():
        conversion = conversions[unit]
        entry.delete(0, END)
        entry.insert(0, f'{conversion:.2f}')


def force_conversion(given_unit, quantity):  # This is the function that will be passed to all the rotational speed entry fields that need converting
    calculated = force_to_n(given_unit, quantity)  # This will be the N that has been calculated
    conversions = force_from_n(calculated)  # This will be a dictionary of all the conversions calculated

    entries = {'N': conv_force_entry_n, 'kN': conv_force_entry_kn, 'kg.f': conv_force_entry_kg_f, 'lb.f': conv_force_entry_lb_f}
    del entries[given_unit]  # This will exclude the currently active unit from being edited
    for unit, entry in entries.items():
        conversion = conversions[unit]
        entry.delete(0, END)
        entry.insert(0, f'{conversion:.2f}')


def torque_conversion(given_unit, quantity):  # This is the function that will be passed to all the rotational speed entry fields that need converting
    calculated = torque_to_n_m(given_unit, quantity)  # This will be the Nm that has been calculated
    conversions = torque_from_n_m(calculated)  # This will be a dictionary of all the conversions calculated

    entries = {'N.m': conv_torque_entry_n_m, 'kN.m': conv_torque_entry_kn_m, 'kg.f.m': conv_torque_entry_kg_f_m, 'lb.f.ft': conv_torque_entry_lb_f_ft, 'lb.f.in': conv_torque_entry_lb_f_in}
    del entries[given_unit]  # This will exclude the currently active unit from being edited
    for unit, entry in entries.items():
        conversion = conversions[unit]
        entry.delete(0, END)
        entry.insert(0, f'{conversion:.2f}')


def power_conversion(given_unit, quantity):  # This is the function that will be passed to all the rotational speed entry fields that need converting
    calculated = power_to_w(given_unit, quantity)  # This will be the W that has been calculated
    conversions = power_from_w(calculated)  # This will be a dictionary of all the conversions calculated

    entries = {'W': conv_power_entry_w, 'kW': conv_power_entry_kw, 'hp': conv_power_entry_hp}
    del entries[given_unit]  # This will exclude the currently active unit from being edited
    for unit, entry in entries.items():
        conversion = conversions[unit]
        entry.delete(0, END)
        entry.insert(0, f'{conversion:.2f}')


# Fundamental Calculation Functions
def force_mass_accel_calc(current_entry, force_qty, force_unit, mass_qty, mass_unit, accel_qty, accel_unit):
    if current_entry == 'force':  # To provide a dummy value so the calculations can be performed
        force_qty = 1
    elif current_entry == 'mass':
        mass_qty = 1
    elif current_entry == 'lin_acc':
        accel_qty = 1

    ans_dict = force_mass_accel_calculations(float(force_qty), force_unit, float(mass_qty), mass_unit, float(accel_qty), accel_unit)  # To calculate all the values

    if current_entry == 'force':
        fund_for_mass_acc_entry_for.delete(0, END)
        fund_for_mass_acc_entry_for.insert(0, f"{ans_dict['force']:.2f}")
    elif current_entry == 'mass':
        fund_for_mass_acc_entry_mass.delete(0, END)
        fund_for_mass_acc_entry_mass.insert(0, f"{ans_dict['mass']:.2f}")
    elif current_entry == 'lin_acc':
        fund_for_mass_acc_entry_acc.delete(0, END)
        fund_for_mass_acc_entry_acc.insert(0, f"{ans_dict['lin_acc']:.2f}")


def torque_force_diameter_calc(current_entry, torque_qty, torque_unit, force_qty, force_unit, diameter_qty, diameter_unit):
    if current_entry == 'torque':  # To provide a dummy value so the calculations can be performed
        torque_qty = 1
    elif current_entry == 'force':
        force_qty = 1
    elif current_entry == 'dist':
        diameter_qty = 1

    ans_dict = tor_force_dia_calculations(float(torque_qty), torque_unit, float(force_qty), force_unit, float(diameter_qty), diameter_unit)  # To calculate all the values

    if current_entry == 'torque':
        fund_tor_for_dia_entry_tor.delete(0, END)
        fund_tor_for_dia_entry_tor.insert(0, f"{ans_dict['torque']:.2f}")
    elif current_entry == 'force':
        fund_tor_for_dia_entry_for.delete(0, END)
        fund_tor_for_dia_entry_for.insert(0, f"{ans_dict['force']:.2f}")
    elif current_entry == 'dist':
        fund_tor_for_dia_entry_dia.delete(0, END)
        fund_tor_for_dia_entry_dia.insert(0, f"{ans_dict['dist']:.2f}")


def linspd_dia_rotspd_calc(current_entry, linspd_qty, linspd_unit, dia_qty, dia_unit, rotspd_qty, rotspd_unit):
    if current_entry == 'lin_spd':  # To provide a dummy value so the calculations can be performed
        linspd_qty = 1
    elif current_entry == 'diameter':
        dia_qty = 1
    elif current_entry == 'rot_spd':
        rotspd_qty = 1

    ans_dict = linspd_dia_rotspd_calculations(float(linspd_qty), linspd_unit, float(dia_qty), dia_unit, float(rotspd_qty), rotspd_unit)  # To calculate all the values

    if current_entry == 'lin_spd':
        fund_linspd_dia_rotspd_entry_linspd.delete(0, END)
        fund_linspd_dia_rotspd_entry_linspd.insert(0, f"{ans_dict['lin_spd']:.2f}")
    elif current_entry == 'diameter':
        fund_linspd_dia_rotspd_entry_dia.delete(0, END)
        fund_linspd_dia_rotspd_entry_dia.insert(0, f"{ans_dict['diameter']:.2f}")
    elif current_entry == 'rot_spd':
        fund_linspd_dia_rotspd_entry_rotspd.delete(0, END)
        fund_linspd_dia_rotspd_entry_rotspd.insert(0, f"{ans_dict['rot_spd']:.2f}")


def power_torque_rotationspeed_calc(current_entry, power_qty, power_unit, torque_qty, torque_unit, rotationspeed_qty, rotationspeed_unit):
    if current_entry == 'power':  # To provide a dummy value so the calculations can be calculated
        power_qty = 1
    elif current_entry == 'torque':
        torque_qty = 1
    elif current_entry == 'rotationspeed':
        rotationspeed_qty = 1

    ans_dict = pow_tor_rotspd_calculations(float(power_qty), power_unit, float(torque_qty), torque_unit, float(rotationspeed_qty), rotationspeed_unit)  # To calculate all the values

    if current_entry == 'power':
        fund_pow_tor_rotspd_entry_pow.delete(0, END)
        fund_pow_tor_rotspd_entry_pow.insert(0, f"{ans_dict['power']:.2f}")
    elif current_entry == 'torque':
        fund_pow_tor_rotspd_entry_tor.delete(0, END)
        fund_pow_tor_rotspd_entry_tor.insert(0, f"{ans_dict['torque']:.2f}")
    elif current_entry == 'rotationspeed':
        fund_pow_tor_rotspd_entry_rotspd.delete(0, END)
        fund_pow_tor_rotspd_entry_rotspd.insert(0, f"{ans_dict['rot_spd']:.2f}")


# PT Calculation Functions
def belt_length_calc(current_entry, belt_length, belt_length_unit, cent_dist, cent_dist_unit, diameter_1, diameter_1_unit, diameter_2, diameter_2_unit):
    if current_entry == 'len':  # To provide a dummy value so the calculations can be calculated
        belt_length = 1
    elif current_entry == 'dist':
        cent_dist = 1
    elif current_entry == 'dia_1':
        diameter_1 = 1
    elif current_entry == 'dia_2':
        diameter_2 = 1

    ans_dict = belt_length_calculations(float(belt_length), belt_length_unit, float(cent_dist), cent_dist_unit, float(diameter_1), diameter_1_unit, float(diameter_2), diameter_2_unit)  # To calculate all the values

    if current_entry == 'len':
        calc_belt_len_entry_len.delete(0, END)
        calc_belt_len_entry_len.insert(0, f"{ans_dict['len']:.2f}")
    elif current_entry == 'dist':
        calc_belt_len_entry_dist.delete(0, END)
        calc_belt_len_entry_dist.insert(0, f"{ans_dict['dist']:.2f}")
    elif current_entry == 'dia_1':
        calc_belt_len_entry_dia_1.delete(0, END)
        calc_belt_len_entry_dia_1.insert(0, f"{ans_dict['dia_1']:.2f}")
    elif current_entry == 'dia_2':
        calc_belt_len_entry_dia_2.delete(0, END)
        calc_belt_len_entry_dia_2.insert(0, f"{ans_dict['dia_2']:.2f}")


def pcd_pitch_teeth_calc(current_entry, pcd_dist, pcd_unit, pitch_dist, pitch_unit, teeth):
    if current_entry == 'PCD':  # To provide a dummy value so the calculations can be calculated
        pcd_dist = 1
    elif current_entry == 'pitch':
        pitch_dist = 1
    elif current_entry == 'teeth':
        teeth = 1

    ans_dict = pcd_pitch_teeth_calculations(float(pcd_dist), pcd_unit, float(pitch_dist), pitch_unit, float(teeth))  # To calculate all the values

    if current_entry == 'PCD':
        calc_pcd_pitch_teeth_entry_pcd.delete(0, END)
        calc_pcd_pitch_teeth_entry_pcd.insert(0, f"{ans_dict['PCD']:.2f}")
    elif current_entry == 'pitch':
        calc_pcd_pitch_teeth_entry_pitch.delete(0, END)
        calc_pcd_pitch_teeth_entry_pitch.insert(0, f"{ans_dict['pitch']:.2f}")
    elif current_entry == 'teeth':
        calc_pcd_pitch_teeth_entry_teeth.delete(0, END)
        calc_pcd_pitch_teeth_entry_teeth.insert(0, f"{ans_dict['teeth']:.2f}")


def gearbox_output_calc(current_entry, tor_qty, tor_unit, pow_qty, pow_unit, rotspd_qty, rotspd_unit, ratio, eff):
    if current_entry == 'torque':  # To provide a dummy value so the calculations can be calculated
        tor_qty = 1
    elif current_entry == 'power':
        pow_qty = 1
    elif current_entry == 'rotspd':
        rotspd_qty = 1
    elif current_entry == 'ratio':
        ratio = 1
    elif current_entry == 'eff':
        eff = 1

    ans_dict = gearbox_output_calculations(float(tor_qty), tor_unit, float(pow_qty), pow_unit, float(rotspd_qty), rotspd_unit, ratio, eff)  # To calculate all the values

    if current_entry == 'torque':
        calc_gbox_output_entry_tor.delete(0, END)
        calc_gbox_output_entry_tor.insert(0, f"{ans_dict['torque']:.2f}")
    elif current_entry == 'power':
        calc_gbox_output_entry_pow.delete(0, END)
        calc_gbox_output_entry_pow.insert(0, f"{ans_dict['power']:.2f}")
    elif current_entry == 'rotspd':
        calc_gbox_output_entry_rotspd.delete(0, END)
        calc_gbox_output_entry_rotspd.insert(0, f"{ans_dict['rotspd']:.2f}")
    elif current_entry == 'ratio':
        calc_gbox_output_entry_ratio.delete(0, END)
        calc_gbox_output_entry_ratio.insert(0, f"{ans_dict['ratio']:.2f}")
    elif current_entry == 'eff':
        calc_gbox_output_entry_eff.delete(0, END)
        calc_gbox_output_entry_eff.insert(0, f"{ans_dict['eff']:.2f}")


# Universal variables
entry_width = 15
label_unit_width = 10
optionmenu_unit_width = 8

padding_ext = 5
padding_int = 2
padding_separator_ext_x = 15
padding_separator_ext_y = (0, 10)

conv_entry_padding_ext_x = (10, 0)  # Padding for all the conversion widgets
conv_entry_padding_ext_y = (10, 5)
conv_label_padding_ext_x = (5, 50)
conv_label_padding_ext_y = (10, 5)

calcs_label_padding_ext_x = (25, 0)  # Padding for all the calculation widgets
calcs_label_padding_ext_y = (10, 0)
calcs_entry_padding_ext_x = (25, 0)
calcs_entry_padding_ext_y = (0, 35)
calcs_optionmenu_padding_ext_x = (0, 50)
calcs_optionmenu_padding_ext_y = (0, 35)

# Creating the main window and defining it
window = Tk()
window.title('PT Calculator')
window.geometry('1200x600')

notebook_main = Notebook(master=window)  # Creating and packing the main notebook
notebook_main.pack(expand=1, fill='both', padx=padding_ext, pady=padding_ext)

tab_conversions = Frame(master=notebook_main)  # Creating all the Frames
tab_calculations = Frame(master=notebook_main)

notebook_main.add(tab_conversions, text='Conversions')  # Adding all the main tabs to the main notebook
notebook_main.add(tab_calculations, text='Calculations')


units_dict = {  # Dictionary of all the units for each type of value
    'mass': ['kg', 'mg', 'g', 'T', 'oz', 'lb', 'st'],
    'time': ['s', 'ms', 'min', 'hr'],
    'dist': ['m', 'mm', 'cm', 'in', 'yd', 'km', 'mi'],
    'lin_spd': ['m/s', 'm/min', 'mm/s', 'mm/min', 'km/hr', 'mi/hr'],
    'rot_spd': ['rad/s', 'rad/min', 'deg/s', 'deg/min', 'rev/s', 'rev/min', 'rev/hr'],
    'lin_acc': ['m/s2', 'ft/s2', 'km/hr/s', 'mi/hr/s'],
    'force': ['N', 'kN', 'kg.f', 'lb.f'],
    'torque': ['N.m', 'kN.m', 'kg.f.m', 'lb.f.ft', 'lb.f.in'],
    'power': ['W', 'kW', 'hp']
}


# Conversion Tab
notebook_conversion = Notebook(master=tab_conversions)  # Creating and packing the units notebook
notebook_conversion.pack(expand=1, fill='both', padx=padding_ext, pady=padding_ext)

# Conversion Tab Frames
tab_mass = Frame(master=notebook_conversion)  # To create all the conversion tab frames
tab_time = Frame(master=notebook_conversion)
tab_distance = Frame(master=notebook_conversion)
tab_lin_speed = Frame(master=notebook_conversion)
tab_rot_speed = Frame(master=notebook_conversion)
tab_lin_accel = Frame(master=notebook_conversion)
tab_force = Frame(master=notebook_conversion)
tab_torque = Frame(master=notebook_conversion)
tab_power = Frame(master=notebook_conversion)

notebook_conversion.add(tab_mass, text='Mass')  # Adding all the conversion tabs to the units notebook
notebook_conversion.add(tab_time, text='Time')
notebook_conversion.add(tab_distance, text='Distance')
notebook_conversion.add(tab_lin_speed, text='Linear Speed')
notebook_conversion.add(tab_rot_speed, text='Rotational Speed')
notebook_conversion.add(tab_lin_accel, text='Linear Acceleration')
notebook_conversion.add(tab_force, text='Force')
notebook_conversion.add(tab_torque, text='Torque')
notebook_conversion.add(tab_power, text='Power')

# Calculation Tab
notebook_calculations = Notebook(master=tab_calculations)  # Creating and packing the calculation notebook
notebook_calculations.pack(expand=1, fill='both', padx=padding_ext, pady=padding_ext)

# Calculation Tab Frames
tab_fundamentals = Frame(master=notebook_calculations)  # To create all the calculation tab frames
tab_pt_calcs = Frame(master=notebook_calculations)

notebook_calculations.add(tab_fundamentals, text='Fundamentals')  # Adding all the calculation tabs to the notebook
notebook_calculations.add(tab_pt_calcs, text='PT Calculations')

# Fundamental Frames
frame_for_mass_acc = Frame(master=tab_fundamentals)  # Creating the frames for each calculation
frame_tor_for_dia = Frame(master=tab_fundamentals)
frame_linspd_dia_rotspd = Frame(master=tab_fundamentals)
frame_pow_tor_rotspd = Frame(master=tab_fundamentals)

label_for_mass_acc = Label(master=tab_fundamentals, text='Force, Mass, Acceleration')
label_tor_for_dia = Label(master=tab_fundamentals, text='Torque, Force, Diameter')
label_linspd_dia_rotspd = Label(master=tab_fundamentals, text='Linear and Rotational Speed')
label_pow_tor_rotspd = Label(master=tab_fundamentals, text='Power, Torque, Rotational Speed')

separator_fundamentals_1 = Separator(master=tab_fundamentals, orient='horizontal')  # Separator lines for between each calculation
separator_fundamentals_2 = Separator(master=tab_fundamentals, orient='horizontal')
separator_fundamentals_3 = Separator(master=tab_fundamentals, orient='horizontal')

label_for_mass_acc.pack()  # Packing into tab frame
frame_for_mass_acc.pack(fill='both')
separator_fundamentals_1.pack(fill='both', padx=padding_separator_ext_x, pady=padding_separator_ext_y)
label_tor_for_dia.pack()
frame_tor_for_dia.pack(fill='both')
separator_fundamentals_2.pack(fill='both', padx=padding_separator_ext_x, pady=padding_separator_ext_y)
label_linspd_dia_rotspd.pack()
frame_linspd_dia_rotspd.pack(fill='both')
separator_fundamentals_3.pack(fill='both', padx=padding_separator_ext_x, pady=padding_separator_ext_y)
label_pow_tor_rotspd.pack()
frame_pow_tor_rotspd.pack(fill='both')

# PT Calc Frames
frame_belt_len = Frame(master=tab_pt_calcs)  # Creating the frames for each calculation
frame_pcd_pitch_teeth = Frame(master=tab_pt_calcs)
frame_gbox_output = Frame(master=tab_pt_calcs)

label_belt_len = Label(master=tab_pt_calcs, text='Belt Length & Centres')
label_pcd_pitch_teeth = Label(master=tab_pt_calcs, text='PCD, Pitch, Teeth')
label_for_gbox_output = Label(master=tab_pt_calcs, text='Gearbox Outputs')

separator_pt_calcs_1 = Separator(master=tab_pt_calcs, orient='horizontal')  # Separator lines for between each calculation
separator_pt_calcs_2 = Separator(master=tab_pt_calcs, orient='horizontal')

label_belt_len.pack()
frame_belt_len.pack(fill='both')
separator_pt_calcs_1.pack(fill='both', padx=padding_separator_ext_x, pady=padding_separator_ext_y)
label_pcd_pitch_teeth.pack()
frame_pcd_pitch_teeth.pack(fill='both')
separator_pt_calcs_2.pack(fill='both', padx=padding_separator_ext_x, pady=padding_separator_ext_y)
label_for_gbox_output.pack()
frame_gbox_output.pack(fill='both')


# Conversion widgets
# Mass Conversion
# Entry Fields
conv_mass_entry_kg = Entry(master=tab_mass, width=entry_width)  # Creating all the entry fields
conv_mass_entry_mg = Entry(master=tab_mass, width=entry_width)
conv_mass_entry_g = Entry(master=tab_mass, width=entry_width)
conv_mass_entry_t = Entry(master=tab_mass, width=entry_width)
conv_mass_entry_oz = Entry(master=tab_mass, width=entry_width)
conv_mass_entry_lb = Entry(master=tab_mass, width=entry_width)
conv_mass_entry_st = Entry(master=tab_mass, width=entry_width)

conv_mass_entry_kg.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)  # Positioning all the entry fields
conv_mass_entry_mg.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_mass_entry_g.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_mass_entry_t.grid(row=2, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_mass_entry_oz.grid(row=3, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_mass_entry_lb.grid(row=4, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_mass_entry_st.grid(row=5, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)

conv_mass_entry_kg.bind('<KeyRelease>', lambda event: mass_conversion('kg', float(conv_mass_entry_kg.get())))  # Function bindings for all the entry fields
conv_mass_entry_mg.bind('<KeyRelease>', lambda event: mass_conversion('mg', float(conv_mass_entry_mg.get())))
conv_mass_entry_g.bind('<KeyRelease>', lambda event: mass_conversion('g', float(conv_mass_entry_g.get())))
conv_mass_entry_t.bind('<KeyRelease>', lambda event: mass_conversion('T', float(conv_mass_entry_t.get())))
conv_mass_entry_oz.bind('<KeyRelease>', lambda event: mass_conversion('oz', float(conv_mass_entry_oz.get())))
conv_mass_entry_lb.bind('<KeyRelease>', lambda event: mass_conversion('lb', float(conv_mass_entry_lb.get())))
conv_mass_entry_st.bind('<KeyRelease>', lambda event: mass_conversion('st', float(conv_mass_entry_st.get())))

# Labels
conv_mass_label_kg = Label(master=tab_mass, text='kg', width=label_unit_width)  # Creating all the labels
conv_mass_label_mg = Label(master=tab_mass, text='mg', width=label_unit_width)
conv_mass_label_g = Label(master=tab_mass, text='g', width=label_unit_width)
conv_mass_label_t = Label(master=tab_mass, text='T', width=label_unit_width)
conv_mass_label_oz = Label(master=tab_mass, text='oz', width=label_unit_width)
conv_mass_label_lb = Label(master=tab_mass, text='lb', width=label_unit_width)
conv_mass_label_st = Label(master=tab_mass, text='st', width=label_unit_width)

conv_mass_label_kg.grid(row=0, column=1, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)  # Positioning of the Labels
conv_mass_label_mg.grid(row=0, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_mass_label_g.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_mass_label_t.grid(row=2, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_mass_label_oz.grid(row=3, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_mass_label_lb.grid(row=4, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_mass_label_st.grid(row=5, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)

# Time Conversion
# Entry Fields
conv_time_entry_s = Entry(master=tab_time, width=entry_width)  # Creating all the entry fields
conv_time_entry_ms = Entry(master=tab_time, width=entry_width)
conv_time_entry_min = Entry(master=tab_time, width=entry_width)
conv_time_entry_hr = Entry(master=tab_time, width=entry_width)

conv_time_entry_s.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)  # Positioning all the entry fields
conv_time_entry_ms.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_time_entry_min.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_time_entry_hr.grid(row=2, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)

conv_time_entry_s.bind('<KeyRelease>', lambda event: time_conversion('s', float(conv_time_entry_s.get())))  # Function bindings for all the entry fields
conv_time_entry_ms.bind('<KeyRelease>', lambda event: time_conversion('ms', float(conv_time_entry_ms.get())))
conv_time_entry_min.bind('<KeyRelease>', lambda event: time_conversion('min', float(conv_time_entry_min.get())))
conv_time_entry_hr.bind('<KeyRelease>', lambda event: time_conversion('hr', float(conv_time_entry_hr.get())))

# Labels
conv_time_label_s = Label(master=tab_time, text='s', width=label_unit_width)  # Creating all the labels
conv_time_label_ms = Label(master=tab_time, text='ms', width=label_unit_width)
conv_time_label_min = Label(master=tab_time, text='min', width=label_unit_width)
conv_time_label_hr = Label(master=tab_time, text='hr', width=label_unit_width)

conv_time_label_s.grid(row=0, column=1, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)  # Positioning of the Labels
conv_time_label_ms.grid(row=0, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_time_label_min.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_time_label_hr.grid(row=2, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)

# Distance Conversions
# Entry Fields
conv_dist_entry_m = Entry(master=tab_distance, width=entry_width)  # Creating all the entry fields
conv_dist_entry_mm = Entry(master=tab_distance, width=entry_width)
conv_dist_entry_cm = Entry(master=tab_distance, width=entry_width)
conv_dist_entry_in = Entry(master=tab_distance, width=entry_width)
conv_dist_entry_yd = Entry(master=tab_distance, width=entry_width)
conv_dist_entry_km = Entry(master=tab_distance, width=entry_width)
conv_dist_entry_mi = Entry(master=tab_distance, width=entry_width)

conv_dist_entry_m.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)  # Positioning all the entry fields
conv_dist_entry_mm.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_dist_entry_cm.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_dist_entry_in.grid(row=2, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_dist_entry_yd.grid(row=3, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_dist_entry_km.grid(row=4, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_dist_entry_mi.grid(row=5, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)

conv_dist_entry_m.bind('<KeyRelease>', lambda event: distance_conversion('m', float(conv_dist_entry_m.get())))  # Function bindings for all the entry fields
conv_dist_entry_mm.bind('<KeyRelease>', lambda event: distance_conversion('mm', float(conv_dist_entry_mm.get())))
conv_dist_entry_cm.bind('<KeyRelease>', lambda event: distance_conversion('cm', float(conv_dist_entry_cm.get())))
conv_dist_entry_in.bind('<KeyRelease>', lambda event: distance_conversion('in', float(conv_dist_entry_in.get())))
conv_dist_entry_yd.bind('<KeyRelease>', lambda event: distance_conversion('yd', float(conv_dist_entry_yd.get())))
conv_dist_entry_km.bind('<KeyRelease>', lambda event: distance_conversion('km', float(conv_dist_entry_km.get())))
conv_dist_entry_mi.bind('<KeyRelease>', lambda event: distance_conversion('mi', float(conv_dist_entry_mi.get())))

# Labels
conv_dist_label_m = Label(master=tab_distance, text='m', width=label_unit_width)  # Creating all the labels
conv_dist_label_mm = Label(master=tab_distance, text='mm', width=label_unit_width)
conv_dist_label_cm = Label(master=tab_distance, text='cm', width=label_unit_width)
conv_dist_label_in = Label(master=tab_distance, text='in', width=label_unit_width)
conv_dist_label_yd = Label(master=tab_distance, text='yd', width=label_unit_width)
conv_dist_label_km = Label(master=tab_distance, text='km', width=label_unit_width)
conv_dist_label_mi = Label(master=tab_distance, text='mi', width=label_unit_width)

conv_dist_label_m.grid(row=0, column=1, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)  # Positioning of the Labels
conv_dist_label_mm.grid(row=0, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_dist_label_cm.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_dist_label_in.grid(row=2, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_dist_label_yd.grid(row=3, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_dist_label_km.grid(row=4, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_dist_label_mi.grid(row=5, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)

# Linear Speed Conversion
# Entry Fields
conv_speed_entry_m_s = Entry(master=tab_lin_speed, width=entry_width)  # Creating all the entry fields
conv_speed_entry_m_min = Entry(master=tab_lin_speed, width=entry_width)
conv_speed_entry_mm_s = Entry(master=tab_lin_speed, width=entry_width)
conv_speed_entry_mm_min = Entry(master=tab_lin_speed, width=entry_width)
conv_speed_entry_km_hr = Entry(master=tab_lin_speed, width=entry_width)
conv_speed_entry_mi_hr = Entry(master=tab_lin_speed, width=entry_width)

conv_speed_entry_m_s.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)  # Positioning all the entry fields
conv_speed_entry_m_min.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_speed_entry_mm_s.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_speed_entry_mm_min.grid(row=2, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_speed_entry_km_hr.grid(row=3, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_speed_entry_mi_hr.grid(row=4, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)

conv_speed_entry_m_s.bind('<KeyRelease>', lambda event: linear_speed_conversion('m/s', float(conv_speed_entry_m_s.get())))  # Function bindings for all the entry fields
conv_speed_entry_m_min.bind('<KeyRelease>', lambda event: linear_speed_conversion('m/min', float(conv_speed_entry_m_min.get())))
conv_speed_entry_mm_s.bind('<KeyRelease>', lambda event: linear_speed_conversion('mm/s', float(conv_speed_entry_mm_s.get())))
conv_speed_entry_mm_min.bind('<KeyRelease>', lambda event: linear_speed_conversion('mm/min', float(conv_speed_entry_mm_min.get())))
conv_speed_entry_km_hr.bind('<KeyRelease>', lambda event: linear_speed_conversion('km/hr', float(conv_speed_entry_km_hr.get())))
conv_speed_entry_mi_hr.bind('<KeyRelease>', lambda event: linear_speed_conversion('mi/hr', float(conv_speed_entry_mi_hr.get())))

# Labels
conv_speed_label_m_s = Label(master=tab_lin_speed, text='m/s', width=label_unit_width)  # Creating all the labels
conv_speed_label_m_min = Label(master=tab_lin_speed, text='m/min', width=label_unit_width)
conv_speed_label_mm_s = Label(master=tab_lin_speed, text='mm/s', width=label_unit_width)
conv_speed_label_mm_min = Label(master=tab_lin_speed, text='mm/min', width=label_unit_width)
conv_speed_label_km_hr = Label(master=tab_lin_speed, text='km/h', width=label_unit_width)
conv_speed_label_mi_hr = Label(master=tab_lin_speed, text='mi/h', width=label_unit_width)

conv_speed_label_m_s.grid(row=0, column=1, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)  # Positioning of the Labels
conv_speed_label_m_min.grid(row=0, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_speed_label_mm_s.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_speed_label_mm_min.grid(row=2, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_speed_label_km_hr.grid(row=3, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_speed_label_mi_hr.grid(row=4, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)

# Rotational Speed Conversion
# Entry Fields
conv_rot_speed_entry_rad_s = Entry(master=tab_rot_speed, width=entry_width)  # Creating all the entry fields
conv_rot_speed_entry_rad_min = Entry(master=tab_rot_speed, width=entry_width)
conv_rot_speed_entry_deg_s = Entry(master=tab_rot_speed, width=entry_width)
conv_rot_speed_entry_deg_min = Entry(master=tab_rot_speed, width=entry_width)
conv_rot_speed_entry_rev_s = Entry(master=tab_rot_speed, width=entry_width)
conv_rot_speed_entry_rev_min = Entry(master=tab_rot_speed, width=entry_width)
conv_rot_speed_entry_rev_hr = Entry(master=tab_rot_speed, width=entry_width)

conv_rot_speed_entry_rad_s.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)  # Positioning all the entry fields
conv_rot_speed_entry_rad_min.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_rot_speed_entry_deg_s.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_rot_speed_entry_deg_min.grid(row=2, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_rot_speed_entry_rev_s.grid(row=3, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_rot_speed_entry_rev_min.grid(row=4, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_rot_speed_entry_rev_hr.grid(row=5, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)

conv_rot_speed_entry_rad_s.bind('<KeyRelease>', lambda event: rotational_speed_conversion('rad/s', float(conv_rot_speed_entry_rad_s.get())))  # Function bindings for all the entry fields
conv_rot_speed_entry_rad_min.bind('<KeyRelease>', lambda event: rotational_speed_conversion('rad/min', float(conv_rot_speed_entry_rad_min.get())))
conv_rot_speed_entry_deg_s.bind('<KeyRelease>', lambda event: rotational_speed_conversion('deg/s', float(conv_rot_speed_entry_deg_s.get())))
conv_rot_speed_entry_deg_min.bind('<KeyRelease>', lambda event: rotational_speed_conversion('deg/min', float(conv_rot_speed_entry_deg_min.get())))
conv_rot_speed_entry_rev_s.bind('<KeyRelease>', lambda event: rotational_speed_conversion('rev/s', float(conv_rot_speed_entry_rev_s.get())))
conv_rot_speed_entry_rev_min.bind('<KeyRelease>', lambda event: rotational_speed_conversion('rev/min', float(conv_rot_speed_entry_rev_min.get())))
conv_rot_speed_entry_rev_hr.bind('<KeyRelease>', lambda event: rotational_speed_conversion('rev/hr', float(conv_rot_speed_entry_rev_hr.get())))

# Labels
conv_rot_speed_label_rad_s = Label(master=tab_rot_speed, text='rad/s', width=label_unit_width)  # Creating all the labels
conv_rot_speed_label_rad_min = Label(master=tab_rot_speed, text='rad/min', width=label_unit_width)
conv_rot_speed_label_deg_s = Label(master=tab_rot_speed, text='deg/s', width=label_unit_width)
conv_rot_speed_label_deg_min = Label(master=tab_rot_speed, text='deg/min', width=label_unit_width)
conv_rot_speed_label_rev_s = Label(master=tab_rot_speed, text='rev/s', width=label_unit_width)
conv_rot_speed_label_rev_min = Label(master=tab_rot_speed, text='rev/min', width=label_unit_width)
conv_rot_speed_label_rev_hr = Label(master=tab_rot_speed, text='rev/hr', width=label_unit_width)

conv_rot_speed_label_rad_s.grid(row=0, column=1, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)  # Positioning of the Labels
conv_rot_speed_label_rad_min.grid(row=0, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_rot_speed_label_deg_s.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_rot_speed_label_deg_min.grid(row=2, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_rot_speed_label_rev_s.grid(row=3, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_rot_speed_label_rev_min.grid(row=4, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_rot_speed_label_rev_hr.grid(row=5, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)

# Linear Acceleration Conversion
# Entry Fields
conv_lin_accel_entry_m_s2 = Entry(master=tab_lin_accel, width=entry_width)  # Creating all the entry fields
conv_lin_accel_entry_ft_s2 = Entry(master=tab_lin_accel, width=entry_width)
conv_lin_accel_entry_km_hr_s = Entry(master=tab_lin_accel, width=entry_width)
conv_lin_accel_entry_mi_hr_s = Entry(master=tab_lin_accel, width=entry_width)

conv_lin_accel_entry_m_s2.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)  # Positioning all the entry fields
conv_lin_accel_entry_ft_s2.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_lin_accel_entry_km_hr_s.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_lin_accel_entry_mi_hr_s.grid(row=2, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)

conv_lin_accel_entry_m_s2.bind('<KeyRelease>', lambda event: linear_accel_conversion('m/s2', float(conv_lin_accel_entry_m_s2.get())))  # Function bindings for all the entry fields
conv_lin_accel_entry_ft_s2.bind('<KeyRelease>', lambda event: linear_accel_conversion('ft/s2', float(conv_lin_accel_entry_ft_s2.get())))
conv_lin_accel_entry_km_hr_s.bind('<KeyRelease>', lambda event: linear_accel_conversion('km/hr/s', float(conv_lin_accel_entry_km_hr_s.get())))
conv_lin_accel_entry_mi_hr_s.bind('<KeyRelease>', lambda event: linear_accel_conversion('mi/hr/s', float(conv_lin_accel_entry_mi_hr_s.get())))

# Labels
conv_lin_accel_label_m_s2 = Label(master=tab_lin_accel, text='m/s2', width=label_unit_width)  # Creating all the labels
conv_lin_accel_label_ft_s2 = Label(master=tab_lin_accel, text='ft/s2', width=label_unit_width)
conv_lin_accel_label_km_hr_s = Label(master=tab_lin_accel, text='km/hr/s', width=label_unit_width)
conv_lin_accel_label_mi_hr_s = Label(master=tab_lin_accel, text='mi/hr/s', width=label_unit_width)

conv_lin_accel_label_m_s2.grid(row=0, column=1, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)  # Positioning of the Labels
conv_lin_accel_label_ft_s2.grid(row=0, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_lin_accel_label_km_hr_s.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_lin_accel_label_mi_hr_s.grid(row=2, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)

# Force Conversion
# Entry Fields
conv_force_entry_n = Entry(master=tab_force, width=entry_width)  # Creating all the entry fields
conv_force_entry_kn = Entry(master=tab_force, width=entry_width)
conv_force_entry_kg_f = Entry(master=tab_force, width=entry_width)
conv_force_entry_lb_f = Entry(master=tab_force, width=entry_width)

conv_force_entry_n.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)  # Positioning all the entry fields
conv_force_entry_kn.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_force_entry_kg_f.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_force_entry_lb_f.grid(row=2, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)

conv_force_entry_n.bind('<KeyRelease>', lambda event: force_conversion('N', float(conv_force_entry_n.get())))  # Function bindings for all the entry fields
conv_force_entry_kn.bind('<KeyRelease>', lambda event: force_conversion('kN', float(conv_force_entry_kn.get())))
conv_force_entry_kg_f.bind('<KeyRelease>', lambda event: force_conversion('kg.f', float(conv_force_entry_kg_f.get())))
conv_force_entry_lb_f.bind('<KeyRelease>', lambda event: force_conversion('lb.f', float(conv_force_entry_lb_f.get())))

# Labels
conv_force_label_n = Label(master=tab_force, text='N', width=label_unit_width)  # Creating all the labels
conv_force_label_kn = Label(master=tab_force, text='kN', width=label_unit_width)
conv_force_label_kg_f = Label(master=tab_force, text='kg.f', width=label_unit_width)
conv_force_label_lb_f = Label(master=tab_force, text='lb.f', width=label_unit_width)

conv_force_label_n.grid(row=0, column=1, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)  # Positioning of the Labels
conv_force_label_kn.grid(row=0, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_force_label_kg_f.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_force_label_lb_f.grid(row=2, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)

# Torque Conversion
# Entry Fields
conv_torque_entry_n_m = Entry(master=tab_torque, width=entry_width)  # Creating all the entry fields
conv_torque_entry_kn_m = Entry(master=tab_torque, width=entry_width)
conv_torque_entry_kg_f_m = Entry(master=tab_torque, width=entry_width)
conv_torque_entry_lb_f_ft = Entry(master=tab_torque, width=entry_width)
conv_torque_entry_lb_f_in = Entry(master=tab_torque, width=entry_width)

conv_torque_entry_n_m.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)  # Positioning all the entry fields
conv_torque_entry_kn_m.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_torque_entry_kg_f_m.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_torque_entry_lb_f_ft.grid(row=2, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_torque_entry_lb_f_in.grid(row=3, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)

conv_torque_entry_n_m.bind('<KeyRelease>', lambda event: torque_conversion('N.m', float(conv_torque_entry_n_m.get())))  # Function bindings for all the entry fields
conv_torque_entry_kn_m.bind('<KeyRelease>', lambda event: torque_conversion('kN.m', float(conv_torque_entry_kn_m.get())))
conv_torque_entry_kg_f_m.bind('<KeyRelease>', lambda event: torque_conversion('kg.f.m', float(conv_torque_entry_kg_f_m.get())))
conv_torque_entry_lb_f_ft.bind('<KeyRelease>', lambda event: torque_conversion('lb.f.ft', float(conv_torque_entry_lb_f_ft.get())))
conv_torque_entry_lb_f_in.bind('<KeyRelease>', lambda event: torque_conversion('lb.f.in', float(conv_torque_entry_lb_f_in.get())))

# Labels
conv_torque_label_n_m = Label(master=tab_torque, text='N.m', width=label_unit_width)  # Creating all the labels
conv_torque_label_kn_m = Label(master=tab_torque, text='kN.m', width=label_unit_width)
conv_torque_label_kg_f_m = Label(master=tab_torque, text='kg.f.m', width=label_unit_width)
conv_torque_label_lb_f_ft = Label(master=tab_torque, text='lb.f.ft', width=label_unit_width)
conv_torque_label_lb_f_in = Label(master=tab_torque, text='lb.f.in', width=label_unit_width)

conv_torque_label_n_m.grid(row=0, column=1, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)  # Positioning of the Labels
conv_torque_label_kn_m.grid(row=0, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_torque_label_kg_f_m.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_torque_label_lb_f_ft.grid(row=2, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_torque_label_lb_f_in.grid(row=3, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)

# Power Conversion
# Entry Fields
conv_power_entry_w = Entry(master=tab_power, width=entry_width)  # Creating all the entry fields
conv_power_entry_kw = Entry(master=tab_power, width=entry_width)
conv_power_entry_hp = Entry(master=tab_power, width=entry_width)

conv_power_entry_w.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)  # Positioning all the entry fields
conv_power_entry_kw.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)
conv_power_entry_hp.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=conv_entry_padding_ext_x, pady=conv_entry_padding_ext_y)

conv_power_entry_w.bind('<KeyRelease>', lambda event: power_conversion('W', float(conv_power_entry_w.get())))  # Function bindings for all the entry fields
conv_power_entry_kw.bind('<KeyRelease>', lambda event: power_conversion('kW', float(conv_power_entry_kw.get())))
conv_power_entry_hp.bind('<KeyRelease>', lambda event: power_conversion('hp', float(conv_power_entry_hp.get())))

# Labels
conv_power_label_w = Label(master=tab_power, text='W', width=label_unit_width)  # Creating all the labels
conv_power_label_kw = Label(master=tab_power, text='kW', width=label_unit_width)
conv_power_label_hp = Label(master=tab_power, text='hp', width=label_unit_width)

conv_power_label_w.grid(row=0, column=1, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)  # Positioning of the Labels
conv_power_label_kw.grid(row=0, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)
conv_power_label_hp.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=conv_label_padding_ext_x, pady=conv_label_padding_ext_y)


# Fundamental Widgets
# Force, Mass, Acceleration Calculations
# Labels
fund_for_mass_acc_label_for = Label(master=frame_for_mass_acc, width=entry_width, text='Force')  # Creates all the entry labels
fund_for_mass_acc_label_mass = Label(master=frame_for_mass_acc, width=entry_width, text='Mass')
fund_for_mass_acc_label_acc = Label(master=frame_for_mass_acc, width=entry_width, text='Acceleration')

fund_for_mass_acc_label_for.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)  # Positioning all the labels
fund_for_mass_acc_label_mass.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
fund_for_mass_acc_label_acc.grid(row=0, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)

# Entries
fund_for_mass_acc_entry_for = Entry(master=frame_for_mass_acc, width=entry_width)  # Create all the entry fields
fund_for_mass_acc_entry_mass = Entry(master=frame_for_mass_acc, width=entry_width)
fund_for_mass_acc_entry_acc = Entry(master=frame_for_mass_acc, width=entry_width)

frame_for_mass_acc.grid_columnconfigure([0, 2, 4], weight=1)  # Column configurations to allow for expansion

fund_for_mass_acc_entry_for.grid(row=1, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)  # Positioning of all the entries
fund_for_mass_acc_entry_mass.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
fund_for_mass_acc_entry_acc.grid(row=1, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)

fund_for_mass_acc_entry_for.bind('<Return>', lambda event: force_mass_accel_calc('force', fund_for_mass_acc_entry_for.get(), fund_for_mass_acc_chosen_for.get(), fund_for_mass_acc_entry_mass.get(), fund_for_mass_acc_chosen_mass.get(), fund_for_mass_acc_entry_acc.get(), fund_for_mass_acc_chosen_acc.get()))  # Function bindings for all the entry fields
fund_for_mass_acc_entry_mass.bind('<Return>', lambda event: force_mass_accel_calc('mass', fund_for_mass_acc_entry_for.get(), fund_for_mass_acc_chosen_for.get(), fund_for_mass_acc_entry_mass.get(), fund_for_mass_acc_chosen_mass.get(), fund_for_mass_acc_entry_acc.get(), fund_for_mass_acc_chosen_acc.get()))
fund_for_mass_acc_entry_acc.bind('<Return>', lambda event: force_mass_accel_calc('lin_acc', fund_for_mass_acc_entry_for.get(), fund_for_mass_acc_chosen_for.get(), fund_for_mass_acc_entry_mass.get(), fund_for_mass_acc_chosen_mass.get(), fund_for_mass_acc_entry_acc.get(), fund_for_mass_acc_chosen_acc.get()))

# OptionMenus
fund_for_mass_acc_chosen_for, fund_for_mass_acc_chosen_mass, fund_for_mass_acc_chosen_acc = StringVar(), StringVar(), StringVar()  # StringVars for all the lists

fund_for_mass_acc_options_for = OptionMenu(frame_for_mass_acc, fund_for_mass_acc_chosen_for, units_dict['force'][0], *units_dict['force'])  # OptionMenus for all the units
fund_for_mass_acc_options_mass = OptionMenu(frame_for_mass_acc, fund_for_mass_acc_chosen_mass, units_dict['mass'][0], *units_dict['mass'])
fund_for_mass_acc_options_acc = OptionMenu(frame_for_mass_acc, fund_for_mass_acc_chosen_acc, units_dict['lin_acc'][0], *units_dict['lin_acc'])

fund_for_mass_acc_options_for.config(width=optionmenu_unit_width)  # Setting the optionmenu widths
fund_for_mass_acc_options_mass.config(width=optionmenu_unit_width)
fund_for_mass_acc_options_acc.config(width=optionmenu_unit_width)

fund_for_mass_acc_options_for.grid(row=1, column=1, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)  # Positioning of all the OptionMenus
fund_for_mass_acc_options_mass.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)
fund_for_mass_acc_options_acc.grid(row=1, column=5, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)

# Torque, Force, Diameter Calculations
# Labels
fund_tor_for_dia_label_tor = Label(master=frame_tor_for_dia, width=entry_width, text='Torque')  # Creates all the entry labels
fund_tor_for_dia_label_for = Label(master=frame_tor_for_dia, width=entry_width, text='Force')
fund_tor_for_dia_label_dia = Label(master=frame_tor_for_dia, width=entry_width, text='Diameter')

fund_tor_for_dia_label_tor.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)  # Positioning all the labels
fund_tor_for_dia_label_for.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
fund_tor_for_dia_label_dia.grid(row=0, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)

# Entries
fund_tor_for_dia_entry_tor = Entry(master=frame_tor_for_dia, width=entry_width)  # Create all the entry fields
fund_tor_for_dia_entry_for = Entry(master=frame_tor_for_dia, width=entry_width)
fund_tor_for_dia_entry_dia = Entry(master=frame_tor_for_dia, width=entry_width)

frame_tor_for_dia.grid_columnconfigure([0, 2, 4], weight=1)  # Column configurations to allow for expansion

fund_tor_for_dia_entry_tor.grid(row=1, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)  # Positioning of all the entries
fund_tor_for_dia_entry_for.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
fund_tor_for_dia_entry_dia.grid(row=1, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)

fund_tor_for_dia_entry_tor.bind('<Return>', lambda event: torque_force_diameter_calc('torque', fund_tor_for_dia_entry_tor.get(), fund_tor_for_dia_chosen_tor.get(), fund_tor_for_dia_entry_for.get(), fund_tor_for_dia_chosen_for.get(), fund_tor_for_dia_entry_dia.get(), fund_tor_for_dia_chosen_dia.get()))  # Function bindings for all the entry fields
fund_tor_for_dia_entry_for.bind('<Return>', lambda event: torque_force_diameter_calc('force', fund_tor_for_dia_entry_tor.get(), fund_tor_for_dia_chosen_tor.get(), fund_tor_for_dia_entry_for.get(), fund_tor_for_dia_chosen_for.get(), fund_tor_for_dia_entry_dia.get(), fund_tor_for_dia_chosen_dia.get()))
fund_tor_for_dia_entry_dia.bind('<Return>', lambda event: torque_force_diameter_calc('dist', fund_tor_for_dia_entry_tor.get(), fund_tor_for_dia_chosen_tor.get(), fund_tor_for_dia_entry_for.get(), fund_tor_for_dia_chosen_for.get(), fund_tor_for_dia_entry_dia.get(), fund_tor_for_dia_chosen_dia.get()))

# OptionMenus
fund_tor_for_dia_chosen_tor, fund_tor_for_dia_chosen_for, fund_tor_for_dia_chosen_dia = StringVar(), StringVar(), StringVar()  # StringVars for all the lists

fund_tor_for_dia_options_tor = OptionMenu(frame_tor_for_dia, fund_tor_for_dia_chosen_tor, units_dict['torque'][0], *units_dict['torque'])  # OptionMenus for all the units
fund_tor_for_dia_options_for = OptionMenu(frame_tor_for_dia, fund_tor_for_dia_chosen_for, units_dict['force'][0], *units_dict['force'])
fund_tor_for_dia_options_dia = OptionMenu(frame_tor_for_dia, fund_tor_for_dia_chosen_dia, units_dict['dist'][0], *units_dict['dist'])

fund_tor_for_dia_options_tor.config(width=optionmenu_unit_width)  # Setting the optionmenu widths
fund_tor_for_dia_options_for.config(width=optionmenu_unit_width)
fund_tor_for_dia_options_dia.config(width=optionmenu_unit_width)

fund_tor_for_dia_options_tor.grid(row=1, column=1, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)  # Positioning of all the OptionMenus
fund_tor_for_dia_options_for.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)
fund_tor_for_dia_options_dia.grid(row=1, column=5, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)

# Linear Velocity, diameter, Rotational Velocity Calculations
# Labels
fund_linspd_dia_rotspd_label_linspd = Label(master=frame_linspd_dia_rotspd, width=entry_width, text='Linear Speed')  # Creates all the entry labels
fund_linspd_dia_rotspd_label_dia = Label(master=frame_linspd_dia_rotspd, width=entry_width, text='Diameter')
fund_linspd_dia_rotspd_label_rotspd = Label(master=frame_linspd_dia_rotspd, width=entry_width, text='Rotational Speed')

fund_linspd_dia_rotspd_label_linspd.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)  # Positioning all the labels
fund_linspd_dia_rotspd_label_dia.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
fund_linspd_dia_rotspd_label_rotspd.grid(row=0, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)

# Entries
fund_linspd_dia_rotspd_entry_linspd = Entry(master=frame_linspd_dia_rotspd, width=entry_width)  # Create all the entry fields
fund_linspd_dia_rotspd_entry_dia = Entry(master=frame_linspd_dia_rotspd, width=entry_width)
fund_linspd_dia_rotspd_entry_rotspd = Entry(master=frame_linspd_dia_rotspd, width=entry_width)

frame_linspd_dia_rotspd.grid_columnconfigure([0, 2, 4], weight=1)  # Column configurations to allow for expansion

fund_linspd_dia_rotspd_entry_linspd.grid(row=1, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)  # Positioning of all the entries
fund_linspd_dia_rotspd_entry_dia.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
fund_linspd_dia_rotspd_entry_rotspd.grid(row=1, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)

fund_linspd_dia_rotspd_entry_linspd.bind('<Return>', lambda event: linspd_dia_rotspd_calc('lin_spd', fund_linspd_dia_rotspd_entry_linspd.get(), fund_linspd_dia_rotspd_chosen_linspd.get(), fund_linspd_dia_rotspd_entry_dia.get(), fund_linspd_dia_rotspd_chosen_dia.get(), fund_linspd_dia_rotspd_entry_rotspd.get(), fund_linspd_dia_rotspd_chosen_rotspd.get()))  # Function bindings for all the entry fields
fund_linspd_dia_rotspd_entry_dia.bind('<Return>', lambda event: linspd_dia_rotspd_calc('diameter', fund_linspd_dia_rotspd_entry_linspd.get(), fund_linspd_dia_rotspd_chosen_linspd.get(), fund_linspd_dia_rotspd_entry_dia.get(), fund_linspd_dia_rotspd_chosen_dia.get(), fund_linspd_dia_rotspd_entry_rotspd.get(), fund_linspd_dia_rotspd_chosen_rotspd.get()))
fund_linspd_dia_rotspd_entry_rotspd.bind('<Return>', lambda event: linspd_dia_rotspd_calc('rot_spd', fund_linspd_dia_rotspd_entry_linspd.get(), fund_linspd_dia_rotspd_chosen_linspd.get(), fund_linspd_dia_rotspd_entry_dia.get(), fund_linspd_dia_rotspd_chosen_dia.get(), fund_linspd_dia_rotspd_entry_rotspd.get(), fund_linspd_dia_rotspd_chosen_rotspd.get()))

# OptionMenus
fund_linspd_dia_rotspd_chosen_linspd, fund_linspd_dia_rotspd_chosen_dia, fund_linspd_dia_rotspd_chosen_rotspd = StringVar(), StringVar(), StringVar()  # StringVars for all the lists

fund_linspd_dia_rotspd_options_linspd = OptionMenu(frame_linspd_dia_rotspd, fund_linspd_dia_rotspd_chosen_linspd, units_dict['lin_spd'][0], *units_dict['lin_spd'])  # OptionMenus for all the units
fund_linspd_dia_rotspd_options_dia = OptionMenu(frame_linspd_dia_rotspd, fund_linspd_dia_rotspd_chosen_dia, units_dict['dist'][0], *units_dict['dist'])
fund_linspd_dia_rotspd_options_rotspd = OptionMenu(frame_linspd_dia_rotspd, fund_linspd_dia_rotspd_chosen_rotspd, units_dict['rot_spd'][0], *units_dict['rot_spd'])

fund_linspd_dia_rotspd_options_linspd.config(width=optionmenu_unit_width)  # Setting the optionmenu widths
fund_linspd_dia_rotspd_options_dia.config(width=optionmenu_unit_width)
fund_linspd_dia_rotspd_options_rotspd.config(width=optionmenu_unit_width)

fund_linspd_dia_rotspd_options_linspd.grid(row=1, column=1, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)  # Positioning of all the OptionMenus
fund_linspd_dia_rotspd_options_dia.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)
fund_linspd_dia_rotspd_options_rotspd.grid(row=1, column=5, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)

# Power, Torque, Rotational Speed Calculations
# Labels
fund_pow_tor_rotspd_label_pow = Label(master=frame_pow_tor_rotspd, width=entry_width, text='Power')  # Creates all the entry labels
fund_pow_tor_rotspd_label_tor = Label(master=frame_pow_tor_rotspd, width=entry_width, text='Torque')
fund_pow_tor_rotspd_label_rotspd = Label(master=frame_pow_tor_rotspd, width=entry_width, text='Rotational Speed')

fund_pow_tor_rotspd_label_pow.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)  # Positioning all the labels
fund_pow_tor_rotspd_label_tor.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
fund_pow_tor_rotspd_label_rotspd.grid(row=0, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)

# Entries
fund_pow_tor_rotspd_entry_pow = Entry(master=frame_pow_tor_rotspd, width=entry_width)  # Create all the entry fields
fund_pow_tor_rotspd_entry_tor = Entry(master=frame_pow_tor_rotspd, width=entry_width)
fund_pow_tor_rotspd_entry_rotspd = Entry(master=frame_pow_tor_rotspd, width=entry_width)

frame_pow_tor_rotspd.grid_columnconfigure([0, 2, 4], weight=1)  # Column configurations to allow for expansion

fund_pow_tor_rotspd_entry_pow.grid(row=1, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)  # Positioning of all the entries
fund_pow_tor_rotspd_entry_tor.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
fund_pow_tor_rotspd_entry_rotspd.grid(row=1, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)

fund_pow_tor_rotspd_entry_pow.bind('<Return>', lambda event: power_torque_rotationspeed_calc('power', fund_pow_tor_rotspd_entry_pow.get(), fund_pow_tor_rotspd_chosen_pow.get(), fund_pow_tor_rotspd_entry_tor.get(), fund_pow_tor_rotspd_chosen_tor.get(), fund_pow_tor_rotspd_entry_rotspd.get(), fund_pow_tor_rotspd_chosen_rotspd.get()))  # Function bindings for all the entry fields
fund_pow_tor_rotspd_entry_tor.bind('<Return>', lambda event: power_torque_rotationspeed_calc('torque', fund_pow_tor_rotspd_entry_pow.get(), fund_pow_tor_rotspd_chosen_pow.get(), fund_pow_tor_rotspd_entry_tor.get(), fund_pow_tor_rotspd_chosen_tor.get(), fund_pow_tor_rotspd_entry_rotspd.get(), fund_pow_tor_rotspd_chosen_rotspd.get()))
fund_pow_tor_rotspd_entry_rotspd.bind('<Return>', lambda event: power_torque_rotationspeed_calc('rotationspeed', fund_pow_tor_rotspd_entry_pow.get(), fund_pow_tor_rotspd_chosen_pow.get(), fund_pow_tor_rotspd_entry_tor.get(), fund_pow_tor_rotspd_chosen_tor.get(), fund_pow_tor_rotspd_entry_rotspd.get(), fund_pow_tor_rotspd_chosen_rotspd.get()))

# OptionMenus
fund_pow_tor_rotspd_chosen_pow, fund_pow_tor_rotspd_chosen_tor, fund_pow_tor_rotspd_chosen_rotspd = StringVar(), StringVar(), StringVar()  # StringVars for all the lists

fund_pow_tor_rotspd_options_pow = OptionMenu(frame_pow_tor_rotspd, fund_pow_tor_rotspd_chosen_pow, units_dict['power'][0], *units_dict['power'])  # OptionMenus for all the units
fund_pow_tor_rotspd_options_tor = OptionMenu(frame_pow_tor_rotspd, fund_pow_tor_rotspd_chosen_tor, units_dict['torque'][0], *units_dict['torque'])
fund_pow_tor_rotspd_options_rotspd = OptionMenu(frame_pow_tor_rotspd, fund_pow_tor_rotspd_chosen_rotspd, units_dict['rot_spd'][0], *units_dict['rot_spd'])

fund_pow_tor_rotspd_options_pow.config(width=optionmenu_unit_width)  # Setting the optionmenu widths
fund_pow_tor_rotspd_options_tor.config(width=optionmenu_unit_width)
fund_pow_tor_rotspd_options_rotspd.config(width=optionmenu_unit_width)

fund_pow_tor_rotspd_options_pow.grid(row=1, column=1, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)  # Positioning of all the OptionMenus
fund_pow_tor_rotspd_options_tor.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)
fund_pow_tor_rotspd_options_rotspd.grid(row=1, column=5, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)


# PT Calc Widgets
# Belt Length Calculations
# Labels
calc_belt_len_label_len = Label(master=frame_belt_len, width=entry_width, text='Belt Length')  # Creates all the entry labels
calc_belt_len_label_dist = Label(master=frame_belt_len, width=entry_width, text='Centre Distance')
calc_belt_len_label_dia_1 = Label(master=frame_belt_len, width=entry_width, text='Diameter 1')
calc_belt_len_label_dia_2 = Label(master=frame_belt_len, width=entry_width, text='Diameter 2')

calc_belt_len_label_len.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)  # Positioning all the labels
calc_belt_len_label_dist.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
calc_belt_len_label_dia_1.grid(row=0, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
calc_belt_len_label_dia_2.grid(row=0, column=6, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)

# Entries
calc_belt_len_entry_len = Entry(master=frame_belt_len, width=entry_width)  # Create all the entry fields
calc_belt_len_entry_dist = Entry(master=frame_belt_len, width=entry_width)
calc_belt_len_entry_dia_1 = Entry(master=frame_belt_len, width=entry_width)
calc_belt_len_entry_dia_2 = Entry(master=frame_belt_len, width=entry_width)

frame_belt_len.grid_columnconfigure([0, 2, 4, 6], weight=1)  # Column configurations to allow for expansion

calc_belt_len_entry_len.grid(row=1, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)  # Positioning of all the entries
calc_belt_len_entry_dist.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
calc_belt_len_entry_dia_1.grid(row=1, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
calc_belt_len_entry_dia_2.grid(row=1, column=6, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)

calc_belt_len_entry_len.bind('<Return>', lambda event: belt_length_calc('len', calc_belt_len_entry_len.get(), calc_belt_len_chosen_len.get(), calc_belt_len_entry_dist.get(), calc_belt_len_chosen_dist.get(), calc_belt_len_entry_dia_1.get(), calc_belt_len_chosen_dia_1.get(), calc_belt_len_entry_dia_2.get(), calc_belt_len_chosen_dia_2.get()))  # Function bindings for all the entry fields
calc_belt_len_entry_dist.bind('<Return>', lambda event: belt_length_calc('dist', calc_belt_len_entry_len.get(), calc_belt_len_chosen_len.get(), calc_belt_len_entry_dist.get(), calc_belt_len_chosen_dist.get(), calc_belt_len_entry_dia_1.get(), calc_belt_len_chosen_dia_1.get(), calc_belt_len_entry_dia_2.get(), calc_belt_len_chosen_dia_2.get()))
calc_belt_len_entry_dia_1.bind('<Return>', lambda event: belt_length_calc('dia_1', calc_belt_len_entry_len.get(), calc_belt_len_chosen_len.get(), calc_belt_len_entry_dist.get(), calc_belt_len_chosen_dist.get(), calc_belt_len_entry_dia_1.get(), calc_belt_len_chosen_dia_1.get(), calc_belt_len_entry_dia_2.get(), calc_belt_len_chosen_dia_2.get()))
calc_belt_len_entry_dia_2.bind('<Return>', lambda event: belt_length_calc('dia_2', calc_belt_len_entry_len.get(), calc_belt_len_chosen_len.get(), calc_belt_len_entry_dist.get(), calc_belt_len_chosen_dist.get(), calc_belt_len_entry_dia_1.get(), calc_belt_len_chosen_dia_1.get(), calc_belt_len_entry_dia_2.get(), calc_belt_len_chosen_dia_2.get()))

# OptionMenus
calc_belt_len_chosen_len, calc_belt_len_chosen_dist, calc_belt_len_chosen_dia_1, calc_belt_len_chosen_dia_2 = StringVar(), StringVar(), StringVar(), StringVar()  # StringVars for all the lists

calc_belt_len_options_len = OptionMenu(frame_belt_len, calc_belt_len_chosen_len, units_dict['dist'][0], *units_dict['dist'])  # OptionMenus for all the units
calc_belt_len_options_dist = OptionMenu(frame_belt_len, calc_belt_len_chosen_dist, units_dict['dist'][0], *units_dict['dist'])
calc_belt_len_options_dia_1 = OptionMenu(frame_belt_len, calc_belt_len_chosen_dia_1, units_dict['dist'][0], *units_dict['dist'])
calc_belt_len_options_dia_2 = OptionMenu(frame_belt_len, calc_belt_len_chosen_dia_2, units_dict['dist'][0], *units_dict['dist'])

calc_belt_len_options_len.config(width=optionmenu_unit_width)  # Setting the optionmenu widths
calc_belt_len_options_dist.config(width=optionmenu_unit_width)
calc_belt_len_options_dia_1.config(width=optionmenu_unit_width)
calc_belt_len_options_dia_2.config(width=optionmenu_unit_width)

calc_belt_len_options_len.grid(row=1, column=1, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)  # Positioning of all the OptionMenus
calc_belt_len_options_dist.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)
calc_belt_len_options_dia_1.grid(row=1, column=5, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)
calc_belt_len_options_dia_2.grid(row=1, column=7, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)

# PCD, pitch, teeth calculations
# Labels
calc_pcd_pitch_teeth_label_pcd = Label(master=frame_pcd_pitch_teeth, width=entry_width, text='PCD')  # Creates all the entry labels
calc_pcd_pitch_teeth_label_pitch = Label(master=frame_pcd_pitch_teeth, width=entry_width, text='Pitch ')
calc_pcd_pitch_teeth_label_teeth = Label(master=frame_pcd_pitch_teeth, width=entry_width, text='Teeth')

calc_pcd_pitch_teeth_label_pcd.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)  # Positioning all the labels
calc_pcd_pitch_teeth_label_pitch.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
calc_pcd_pitch_teeth_label_teeth.grid(row=0, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)

# Entries
calc_pcd_pitch_teeth_entry_pcd = Entry(master=frame_pcd_pitch_teeth, width=entry_width)  # Create all the entry fields
calc_pcd_pitch_teeth_entry_pitch = Entry(master=frame_pcd_pitch_teeth, width=entry_width)
calc_pcd_pitch_teeth_entry_teeth = Entry(master=frame_pcd_pitch_teeth, width=entry_width)

frame_pcd_pitch_teeth.grid_columnconfigure([0, 2, 4], weight=1)  # Column configurations to allow for expansion

calc_pcd_pitch_teeth_entry_pcd.grid(row=1, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)  # Positioning of all the entries
calc_pcd_pitch_teeth_entry_pitch.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
calc_pcd_pitch_teeth_entry_teeth.grid(row=1, column=4, ipadx=padding_int, ipady=padding_int, padx=25, pady=calcs_entry_padding_ext_y,  sticky=W+E)

calc_pcd_pitch_teeth_entry_pcd.bind('<Return>', lambda event: pcd_pitch_teeth_calc('PCD', calc_pcd_pitch_teeth_entry_pcd.get(), calc_pcd_pitch_teeth_chosen_pcd.get(), calc_pcd_pitch_teeth_entry_pitch.get(), calc_pcd_pitch_teeth_chosen_pitch.get(), calc_pcd_pitch_teeth_entry_teeth.get()))  # Function bindings for all the entry fields
calc_pcd_pitch_teeth_entry_pitch.bind('<Return>', lambda event: pcd_pitch_teeth_calc('pitch', calc_pcd_pitch_teeth_entry_pcd.get(), calc_pcd_pitch_teeth_chosen_pcd.get(), calc_pcd_pitch_teeth_entry_pitch.get(), calc_pcd_pitch_teeth_chosen_pitch.get(), calc_pcd_pitch_teeth_entry_teeth.get()))
calc_pcd_pitch_teeth_entry_teeth.bind('<Return>', lambda event: pcd_pitch_teeth_calc('teeth', calc_pcd_pitch_teeth_entry_pcd.get(), calc_pcd_pitch_teeth_chosen_pcd.get(), calc_pcd_pitch_teeth_entry_pitch.get(), calc_pcd_pitch_teeth_chosen_pitch.get(), calc_pcd_pitch_teeth_entry_teeth.get()))

# OptionMenus
calc_pcd_pitch_teeth_chosen_pcd, calc_pcd_pitch_teeth_chosen_pitch = StringVar(), StringVar()  # StringVars for all the lists

calc_pcd_pitch_teeth_options_pcd = OptionMenu(frame_pcd_pitch_teeth, calc_pcd_pitch_teeth_chosen_pcd, units_dict['dist'][0], *units_dict['dist'])  # OptionMenus for all the units
calc_pcd_pitch_teeth_options_pitch = OptionMenu(frame_pcd_pitch_teeth, calc_pcd_pitch_teeth_chosen_pitch, units_dict['dist'][0], *units_dict['dist'])

calc_pcd_pitch_teeth_options_pcd.config(width=optionmenu_unit_width)  # Setting the optionmenu widths
calc_pcd_pitch_teeth_options_pitch.config(width=optionmenu_unit_width)

calc_pcd_pitch_teeth_options_pcd.grid(row=1, column=1, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)  # Positioning of all the OptionMenus
calc_pcd_pitch_teeth_options_pitch.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)

# Gearbox Output Calculations
# Labels
calc_gbox_output_label_tor = Label(master=frame_gbox_output, width=entry_width, text='Torque')  # Creates all the entry labels
calc_gbox_output_label_pow = Label(master=frame_gbox_output, width=entry_width, text='Power ')
calc_gbox_output_label_rotspd = Label(master=frame_gbox_output, width=entry_width, text='Rotational Speed')
calc_gbox_output_label_ratio = Label(master=frame_gbox_output, width=entry_width, text='Ratio')
calc_gbox_output_label_eff = Label(master=frame_gbox_output, width=entry_width, text='Efficiency')

calc_gbox_output_label_tor.grid(row=0, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)  # Positioning all the labels
calc_gbox_output_label_pow.grid(row=0, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
calc_gbox_output_label_rotspd.grid(row=0, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
calc_gbox_output_label_ratio.grid(row=0, column=6, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)
calc_gbox_output_label_eff.grid(row=0, column=8, ipadx=padding_int, ipady=padding_int, padx=calcs_label_padding_ext_x, pady=calcs_label_padding_ext_y)

# Entries
calc_gbox_output_entry_tor = Entry(master=frame_gbox_output, width=entry_width)  # Create all the entry fields
calc_gbox_output_entry_pow = Entry(master=frame_gbox_output, width=entry_width)
calc_gbox_output_entry_rotspd = Entry(master=frame_gbox_output, width=entry_width)
calc_gbox_output_entry_ratio = Entry(master=frame_gbox_output, width=entry_width)
calc_gbox_output_entry_eff = Entry(master=frame_gbox_output, width=entry_width)

frame_gbox_output.grid_columnconfigure([0, 2, 4, 6, 8], weight=1)  # Column configurations to allow for expansion

calc_gbox_output_entry_tor.grid(row=1, column=0, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)  # Positioning of all the entries
calc_gbox_output_entry_pow.grid(row=1, column=2, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
calc_gbox_output_entry_rotspd.grid(row=1, column=4, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
calc_gbox_output_entry_ratio.grid(row=1, column=6, ipadx=padding_int, ipady=padding_int, padx=calcs_entry_padding_ext_x, pady=calcs_entry_padding_ext_y,  sticky=W+E)
calc_gbox_output_entry_eff.grid(row=1, column=8, ipadx=padding_int, ipady=padding_int, padx=25, pady=calcs_entry_padding_ext_y,  sticky=W+E)

calc_gbox_output_entry_tor.bind('<Return>', lambda event: gearbox_output_calc('torque', calc_gbox_output_entry_tor.get(), calc_gbox_output_chosen_tor.get(), calc_gbox_output_entry_pow.get(), calc_gbox_output_chosen_pow.get(), calc_gbox_output_entry_rotspd.get(), calc_gbox_output_chosen_rotspd.get(), calc_gbox_output_entry_ratio.get(), calc_gbox_output_entry_eff.get()))  # Function bindings for all the entry fields
calc_gbox_output_entry_pow.bind('<Return>', lambda event: gearbox_output_calc('power', calc_gbox_output_entry_tor.get(), calc_gbox_output_chosen_tor.get(), calc_gbox_output_entry_pow.get(), calc_gbox_output_chosen_pow.get(), calc_gbox_output_entry_rotspd.get(), calc_gbox_output_chosen_rotspd.get(), calc_gbox_output_entry_ratio.get(), calc_gbox_output_entry_eff.get()))
calc_gbox_output_entry_rotspd.bind('<Return>', lambda event: gearbox_output_calc('rotspd', calc_gbox_output_entry_tor.get(), calc_gbox_output_chosen_tor.get(), calc_gbox_output_entry_pow.get(), calc_gbox_output_chosen_pow.get(), calc_gbox_output_entry_rotspd.get(), calc_gbox_output_chosen_rotspd.get(), calc_gbox_output_entry_ratio.get(), calc_gbox_output_entry_eff.get()))
calc_gbox_output_entry_ratio.bind('<Return>', lambda event: gearbox_output_calc('ratio', calc_gbox_output_entry_tor.get(), calc_gbox_output_chosen_tor.get(), calc_gbox_output_entry_pow.get(), calc_gbox_output_chosen_pow.get(), calc_gbox_output_entry_rotspd.get(), calc_gbox_output_chosen_rotspd.get(), calc_gbox_output_entry_ratio.get(), calc_gbox_output_entry_eff.get()))
calc_gbox_output_entry_eff.bind('<Return>', lambda event: gearbox_output_calc('eff', calc_gbox_output_entry_tor.get(), calc_gbox_output_chosen_tor.get(), calc_gbox_output_entry_pow.get(), calc_gbox_output_chosen_pow.get(), calc_gbox_output_entry_rotspd.get(), calc_gbox_output_chosen_rotspd.get(), calc_gbox_output_entry_ratio.get(), calc_gbox_output_entry_eff.get()))

# OptionMenus
calc_gbox_output_chosen_tor, calc_gbox_output_chosen_pow, calc_gbox_output_chosen_rotspd = StringVar(), StringVar(), StringVar()  # StringVars for all the lists

calc_gbox_output_options_tor = OptionMenu(frame_gbox_output, calc_gbox_output_chosen_tor, units_dict['torque'][0], *units_dict['torque'])  # OptionMenus for all the units
calc_gbox_output_options_pow = OptionMenu(frame_gbox_output, calc_gbox_output_chosen_pow, units_dict['power'][0], *units_dict['power'])
calc_gbox_output_options_rotspd = OptionMenu(frame_gbox_output, calc_gbox_output_chosen_rotspd, units_dict['rot_spd'][0], *units_dict['rot_spd'])

calc_gbox_output_options_tor.config(width=optionmenu_unit_width)  # Setting the optionmenu widths
calc_gbox_output_options_pow.config(width=optionmenu_unit_width)
calc_gbox_output_options_rotspd.config(width=optionmenu_unit_width)

calc_gbox_output_options_tor.grid(row=1, column=1, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)  # Positioning of all the OptionMenus
calc_gbox_output_options_pow.grid(row=1, column=3, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)
calc_gbox_output_options_rotspd.grid(row=1, column=5, ipadx=padding_int, ipady=padding_int, padx=calcs_optionmenu_padding_ext_x, pady=calcs_optionmenu_padding_ext_y)


window.mainloop()

# End this here for now.
# End - 04/03/2021

# FUTURE WORK OR FURTHER ITERATIONS
# Make the calculations sections frames scrollable
# Need to add an imperial foot unit to convert to and from, don't know why I forgot that one the first time...
# Can you find a way to loop the creation of all the tkinter widgets, would be nice to not have so many lines
# I've seen people mention online using classes for tkinter widgets, would this make it more readable and less code lines
