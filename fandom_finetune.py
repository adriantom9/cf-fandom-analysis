import pandas as pd
import numpy as np



need_confirmation = ["2521",
"BIBI",
"BP",
"CARNIVAL",
"CECILIA",
"CHIARA",
"CHIZURU",
"CHLOE",
"DEMON HUNTER",
"DO OR DIE",
"DOODLE MONSTER",
"DVC",
"EVADE",
"FIGHT CLUB",
"GHOST",
"HM",
"HOSHI NO AI",
"INAH",
"INNOCENT",
"LEO",
"LOVEJOY",
"LOVESTRUCK\)",
"MANY YOU CAN SEE HERE",
"MARI",
"MARIN",
"MIKA",
"MILKMAN",
"MRS",
"NINO",
"OFF",
"OM!",
"PERFUME EDT",
"POTN",
"PRESSURE",
"PRIDE",
"RAVEANNE",
"RE",
"REYNARD",
"RIDDLE JOKER",
"RIMU",
"SENA",
"SENKA",
"STL",
"T1",
"THE BEAR",
"THE BOYZ",
"THE SANDMAN",
"TREASURE",
"VNC",
"YUTA",
"ZENO"]

#substr = "GENSHIN"
df17 = pd.read_json('data\cf17_catalog.json')
df17['event'] = "CF17"
df18 = pd.read_json('data\cf18_catalog_raw_20240502.json')
df18['event'] = "CF18"

df = pd.concat([df17,df18])
df["fandom"] = df["fandom"].str.upper()
df["other_fandom"] = df["other_fandom"].str.upper()

big_result = pd.DataFrame()

#print(df)

for substr in need_confirmation:
    fandom = df[["fandom", "other_fandom", "name", "circle_code", "event", "circle_facebook", "circle_instagram", "circle_twitter", "circle_other_socials", "sampleworks_images"]]
    result = pd.concat([fandom[fandom["fandom"].str.contains(substr)],fandom[fandom["other_fandom"].str.contains(substr)]])
    result["substring"] = substr
    big_result = pd.concat([big_result, result])
    #print(substr)
print(big_result)
big_result.to_csv("data/need_confirm.csv")
'''    print("string:", substr)
    print(result[["fandom", "other_fandom", "name", "circle_code", "event"]])
    print(result[["name", "circle_code", "event", "circle_facebook", "circle_instagram", "circle_twitter", "circle_other_socials"]])
    print(result[["name", "circle_code", "sampleworks_images"]])
    input("Press to continue...")'''
'''other_list = fandom["other_fandom"].tolist()
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
cdf.to_csv("data/fandoms.csv")'''