import math
import pandas as pd

R = 0.00003728226
MILE_IN_KM = 1.60934

# two ways of doing it, pd data-series, or dictionary
# #ds_batt = pd.Series([3.7, 3.6, 3.2],['LIPO_VOLTS', 'LIIO_VOLTS', 'LIFE_VOLTS'])
ds_batt = {'LIPO_VOLTS': 3.7,
           'LIIO_VOLTS': 3.6,
           'LIFE_VOLTS': 3.2}

# two ways of doing it, pd data-series, or dictionary
ds_conf = {'cell_volts': ds_batt['LIIO_VOLTS'],
           'batt_cells': 10.0,
           'efficiency': .85,
           'motor_teeth': 15,
           'wheel_teeth': 50,
           'wheel_size': 95.0}

ds_conf['batt_volts'] = round(ds_conf['batt_cells'] * ds_conf['cell_volts'])
ds_conf['gear_ratio'] = round(ds_conf['motor_teeth'] / ds_conf['wheel_teeth'], 1)

# varying KV of the motor
columns = ['motor_rpm', 'erpm', 'speed_kph']
df = pd.DataFrame(data=10*[len(columns)*[1.0]], columns=columns, index=range(140, 240, 10), dtype=int)
df.index.name = 'KV'
for kv in df.index:
    df.motor_rpm[kv] = kv * ds_conf['batt_volts'] * ds_conf['efficiency']
    df.erpm[kv] = ds_conf['batt_volts'] * kv * 7
    df.speed_kph[kv] = df.motor_rpm[kv] * ds_conf['wheel_size'] * math.pi * R * ds_conf['gear_ratio'] * MILE_IN_KM

print("\n", ds_conf, "\n")
print(df.head(10))