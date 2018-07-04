import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator

df = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_180630.txt')

df.columns = df.columns.str.strip()

df['real_entries'] = df['ENTRIES'].diff()
df['real_exits'] = df['EXITS'].diff()

df.loc[df['real_entries'] < 0] = np.nan
df.loc[df['real_exits'] < 0] = np.nan
df.loc[df['real_entries'] > 100000] = np.nan
df.loc[df['real_exits'] > 100000] = np.nan

print(df.columns)

station_1_av = df[df['STATION'] == '1 AV']
print(df.sort_values(by='real_entries', ascending=False).head(100))

print(df.groupby(['STATION'])['real_entries', 'real_exits'].median())

new_df = df.groupby(['STATION'])['real_entries', 'real_exits'].median()

totals = {}
for index, row in new_df.iterrows():
    totals[index] = row['real_entries'] + row['real_exits']

sorted_totals = sorted(totals.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_totals)
