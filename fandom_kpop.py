import pandas as pd
import numpy as np

df = pd.read_csv('data\kpopgroups.csv')
df['Name'] = df['Name'].str.upper()
fandoms = pd.read_csv('data\\fandoms.csv')
fandom_list = fandoms['0'].tolist()

mask = df['Name'].isin(fandom_list)

print(df)
print(df[mask])

cdf = df[mask]

'''
cdf = pd.DataFrame(complete)'''
cdf.to_csv("data/fandoms_kpop.csv")