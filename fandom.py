import pandas as pd
import numpy as np

df17 = pd.read_json('data\cf17_catalog.json')
df18 = pd.read_json('data\cf18_catalog_raw_20240502.json')

df = pd.concat([df17,df18])

fandom = df[["fandom", "other_fandom"]]
other_list = fandom["other_fandom"].tolist()
fandom2 = fandom["fandom"].str.upper()

other_list_2 = []

for ip1 in other_list:
    lists = ip1.replace("🌻", ",").replace(";", ",").replace("\u2060", "").split(",")
    for ip2 in lists:
        other_list_2.append(ip2.strip().upper())

ol2 = np.array(other_list_2)

complete = np.sort(np.unique(np.append(fandom2, ol2)))

#ol3 = set(other_list_2)
#print(len(other_list_2))
#print(len(ol3))

#unique_fandom = fandom2.unique()

#print(len(unique_fandom))
#print(type(unique_fandom))
#print(len(unique_fandom) + len(ol3))
print(len(complete))
print(complete[:10])
print(complete[-10:])

cdf = pd.DataFrame(complete)
cdf.to_csv("data/fandoms.csv")