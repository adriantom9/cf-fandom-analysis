import pandas as pd
import numpy as np

dfa = pd.read_csv('data\\anime.csv')
dfm = pd.read_csv('data\manga.csv')
fandoms = pd.read_csv('data\\fandom_index.csv')
fandom_list = fandoms['string'].tolist()
dfa['Title'] = dfa['Title'].str.upper()
dfa['Year'] = dfa['Premiered'].str.slice(start=-4)
dfm['Title'] = dfm['Title'].str.upper()
dfm['Year'] = dfm['Published'].str.slice(start=8, stop=13).str.strip()

big_result = pd.DataFrame()

print(dfa)
print(dfm)
print(dfa.columns)
print(dfm.columns)

listofdict = fandoms.to_dict(orient='records')
print(listofdict)

for dict in listofdict:
    substr = dict['string']
    print(substr)
    dfa2 = dfa[dfa['Title'].str.contains(str(substr).replace(")", "").replace("(", ""))][["Title", "Year"]]
    dfa2["substr"] = substr
    dfa2["fandom"] = dict['fandom']
    dfa2['Media'] = 'Anime'
    dfm2 = dfm[dfm['Title'].str.contains(str(substr).replace(")", "").replace("(", ""))][["Title", "Year"]]
    dfm2["substr"] = substr
    dfm2["fandom"] = dict['fandom']
    dfm2['Media'] = 'Manga'
    big_result = pd.concat([big_result, dfa2, dfm2])
    #print(dfa[dfa['Title'].str.contains(str(substr).replace(")", "").replace("(", ""))])

big_result_2 = big_result[["Title", "Year", "fandom", "Media"]].dropna().sort_values(by=['fandom','Year'], ascending=True).drop_duplicates(subset=['Title', 'fandom', 'Media'], keep='first')


print(big_result_2)

#maska = dfa['Title'].isin(fandom_list)
#maskm = dfm['Title'].isin(fandom_list)

#print(dfa[maska])
#print(dfm[maskm])


cdf = big_result_2
cdf.to_csv("data/fandoms_animanga.csv")

'''
cdf = pd.DataFrame(complete)
cdf.to_csv("data/fandoms_kpop.csv")'''