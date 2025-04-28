# ----------------------------------------------------------------
#!/usr/bin/python3
# Author(s)   : Mahbub Alam
# File        : data_cleaning_auto.py
# Created     : 2025-03-23 (Mar, Sun) 19:37:59 CET
# Description : X
# ----------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('auto_raw.csv')

# # =============[[ underscore type columns name ]]=============={{{

# # df.rename({col: col.replace('-', '_') for col in df.columns}, axis=1, inplace=True)
# print(df.columns) # output: ["symboling", "normalized_losses", "make", "fuel_type", "aspiration", "num_of_doors", "body_style", "drive_wheels", "engine_location", "wheel_base", "length", "width", "height", "curb_weight", "engine_type", "num_of_cylinders", "engine_size", "fuel_system", "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm", "city_mpg", "highway_mpg", "price"]
# # df.to_csv('auto_raw.csv', index=False)

# # }}}

# print(df.dtypes)

# ===============[[ dealing with missing data ]]==============={{{

df.replace('?', np.nan, inplace=True)

missing_data = df.isnull()
# print(missing_data.sum().info())
missing_data_dict = missing_data.sum()[lambda x: x > 0].to_dict()
# print(missing_data_dict) # Output: {'normalized_losses': 41, 'num_of_doors': 2, 'bore': 4, 'stroke': 4, 'horsepower': 2, 'peak_rpm': 2, 'price': 4}
cols_with_nan = df.columns[missing_data.any()].to_list()
# print(cols_with_nan) # output: ['normalized_losses', 'num_of_doors', 'bore', 'stroke', 'horsepower', 'peak_rpm', 'price']
print(f"")

# ====================[[ replace by mean ]]===================={{{

avg_norm_losses = df['normalized_losses'].astype('float').mean()
df['normalized_losses'].replace(np.nan, avg_norm_losses, inplace=True)

avg_bore = df['bore'].astype("float").mean()
df['bore'].replace(np.nan, avg_bore, inplace=True)

avg_stroke = df['stroke'].astype("float").mean()
df['stroke'].replace(np.nan, avg_stroke, inplace=True)

avg_horsepower = df['horsepower'].astype("float").mean()
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

avg_peak_rpm = df['peak_rpm'].astype("float").mean()
df.replace({'peak_rpm': np.nan}, avg_peak_rpm, inplace=True)

# }}}

# ============[[ replace by most frequent value ]]============={{{

# print(df['num_of_doors'].value_counts())
max_num_of_doors = df['num_of_doors'].value_counts().idxmax()
df.replace({'num_of_doors': np.nan}, max_num_of_doors, inplace=True)

# }}}

# =====================[[ drop columns ]]======================{{{

df.dropna(subset=['price'], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

# }}}

# }}}

# ====================[[ changing dtypes ]]===================={{{

df[["wheel_base", "length", "width", "height", "curb_weight", "engine_size", "bore", "stroke", "compression_ratio", "peak_rpm", "city_mpg", "highway_mpg", "price"]] = df[["wheel_base", "length", "width", "height", "curb_weight", "engine_size", "bore", "stroke", "compression_ratio", "peak_rpm", "city_mpg", "highway_mpg", "price"]].astype('float')
df[["normalized_losses", "horsepower"]] = df[["normalized_losses", "horsepower"]].astype("int")

# print(df['normalized_losses'])

# }}}

# =================[[ data standardization ]]=================={{{

df['city-L/100km'] = 235/df['city_mpg']
df['highway-L/100km'] = 235/df['highway_mpg']

# }}}

# ==================[[ data normalization ]]==================={{{

df['length_scaled'] = df['length']/df['length'].max()
df['width_scaled'] = df['width']/df['width'].max()
df['height_scaled'] = df['height']/df['height'].max()

# }}}

# ========================[[ binning ]]========================{{{

# =======================[[ histogram ]]======================={{{

file_name='horsepower_hist'
plt.figure(file_name)
df['horsepower'].hist(edgecolor='black')

# x/y labels
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower histogram")

plt.savefig(f'{file_name}.jpg')

plt.show()

# }}}

# ===================[[ binning normally ]]===================={{{

bins = np.linspace(df['horsepower'].min(), df['horsepower'].max(), 4)
group_names = ['Low', 'Medium', 'High']
df['horsepower_binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)

file_name='horsepower_bins'
plt.figure(file_name)
horsepower_binned = df['horsepower_binned'].value_counts().reindex(group_names)
plt.bar(group_names, horsepower_binned)

plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

plt.savefig(f'{file_name}.jpg')

# plt.show()

# }}}

# ===================[[ binning with hist ]]==================={{{

file_name='horsepower_bins_from_hist'
plt.figure(file_name)
df['horsepower'].hist(bins=3)

plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins from histogram")

plt.savefig(f'{file_name}.jpg')

# plt.show()

# }}}

# }}}

# ==================[[ indicator variables ]]=================={{{

dummy_var_1 = pd.get_dummies(df['fuel_type'], dtype=int)
dummy_var_1.rename({'gas': 'fuel_type_gas', 'diesel': 'fuel_type_diesel'}, axis=1, inplace=True)
# print(dummy_var_1.head())

dummy_var_2 = pd.get_dummies(df['aspiration'], dtype=int)
dummy_var_2.rename(lambda x : 'aspiration_' + x, axis=1, inplace=True)
# print(dummy_var_2.head())

# ======================[[ concatinate ]]======================{{{

df = pd.concat([df, dummy_var_1], axis=1)
df = pd.concat([df, dummy_var_2], axis=1)

# }}}

# # =================[[ drop original column ]]=================={{{

# df.drop('fuel_type', axis=1, inplace=True)
# df.drop('aspiration', axis=1, inplace=True)

# # }}}

# }}}

print(df[['fuel_type', 'aspiration']].head())

df.to_csv('clean_auto.csv', index=False)
