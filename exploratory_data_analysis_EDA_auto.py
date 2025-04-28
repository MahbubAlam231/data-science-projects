# ----------------------------------------------------------------
#!/usr/bin/python3
# Author(s)   : Mahbub Alam
# File        : exploratory_data_analysis_EDA_auto.py
# Created     : 2025-03-21 (Mar, Fri) 16:49:07 CET
# Description : X
# ----------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('clean_auto.csv')

# print(df.columns)
# df.rename({col: col.replace('-', '_') for col in df.columns}, axis=1, inplace=True)

# df[["normalized_losses", "wheel_base", "length", "width", "height", "curb_weight", "engine_size", "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm", "city_mpg", "highway_mpg", "price"]].astype('float')
# df.to_csv('auto.csv', index=False)

# print(df.head())
# print(df.dtypes)


# ===========[[ descriptive stats: value_counts() ]]==========={{{

# # drive_wheels_count = df[['drive_wheels']].value_counts().reset_index()
# # drive_wheels_count = df[['drive_wheels']].value_counts() # gives MultiIndex Series
# drive_wheels_count = df['drive_wheels'].value_counts() # gives Series
# drive_wheels_count.name='value_counts' # naming a pd.Series
# # drive_wheels_count.columns = ['drive_wheels', 'value_counts']
# # drive_wheels_count.index.name='x' # naming indices of a Series or dataframe
# # print(drive_wheels_count.to_string(index=False))
# # print(drive_wheels_count.describe())
# # print(drive_wheels_count.info())
# print(drive_wheels_count.head())

drive_wheels_count = df['drive_wheels'].value_counts().to_frame(name='value_counts')
drive_wheels_count.index.name = 'drive_wheels'
# print(drive_wheels_count.info())
print(f"")
print(drive_wheels_count.head())

# }}}

# =======================[[ Box plots ]]======================={{{

file_name = 'drive_wheels_box_plot'
plt.figure(file_name)
sns.boxplot(x='drive_wheels', y='price', data=df)

# x/y coordinate labels
plt.xlabel("Drive wheels")
plt.ylabel("Price")
plt.title("Drive wheels box plot")

plt.savefig(f'{file_name}.jpg')

plt.close()

# }}}

# ========[[ scatter plot for price and engine size ]]========={{{

file_name='price_vs_engine_size_scatter_plot'
plt.figure(file_name)
y=df['price']
x=df['engine_size']
plt.scatter(x, y)

# x/y coordinate labels
plt.xlabel("Engine size")
plt.ylabel("Price")
plt.title("Scatter plot of Price and Engine size")
# plt.legend()
plt.grid(True)

plt.savefig(f'{file_name}.jpg')

plt.close()

# }}}

# ===================[[ groupby and pivot ]]==================={{{

df_test = df[['drive_wheels', 'body_style', 'price']]
df_grp = df_test.groupby(['drive_wheels', 'body_style'], as_index=False).mean()
print(f"")
# print(df_grp)

df_pivot = df_grp.pivot(index='drive_wheels', columns='body_style')
print(df_pivot)

# df_pivot.to_excel('auto_drive_wheels_body_style_pivot_table.xlsx')

# }}}

# ==============[[ regression and correlation ]]==============={{{

file_name='price_and_engine_size_regression'
plt.figure(file_name)
sns.regplot(x='engine_size', y='price', data=df[['price', 'engine_size']])
# x/y coordinate labels
plt.xlabel("Engine size")
plt.ylabel("Price")
plt.title("Scatter plot of Price and Engine size")
# plt.legend()
plt.grid(True)

plt.savefig(f'{file_name}.jpg')
# plt.ylim(0,)
plt.close()

file_name='price_and_highway_mpg_correlation'
plt.figure(file_name)
sns.regplot(x='highway_mpg', y='price', data=df)
# x/y coordinate labels
plt.xlabel("highway_mpg")
plt.ylabel("price")
plt.title("correlation between highway_mpg and price")
plt.savefig(f'{file_name}.jpg')
if 0:
    plt.show()
else:
    plt.close()

file_name='price_and_peak_rpm_correlation'
plt.figure(file_name)
sns.regplot(x='peak_rpm', y='price', data=df)
# x/y coordinate labels
plt.xlabel("peak_rpm")
plt.ylabel("price")
plt.title("Correlation between peak_rpm and price")
plt.savefig(f'{file_name}.jpg')
if 0:
    plt.show()
else:
    plt.close()#

file_name='correlation_horsepower_and_price'
plt.figure(file_name)
sns.regplot(df, x='horsepower', y='price')
# x/y coordinate labels
plt.xlabel("horsepower")
plt.ylabel("price")
plt.title("correlation between horsepower and price")
plt.savefig(f'{file_name}.jpg')
if 1:
    plt.show()
else:
    plt.close()

# ==================[[ correlation coeffs ]]==================={{{

pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])

print(pearson_coef, p_value)

# plt.legend(f"Pearson coefficient: {pearson_coef}\nP_value: {p_value}")

# }}}

# }}}
