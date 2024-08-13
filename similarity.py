import Levenshtein
import pandas as pd

df = pd.read_csv("data/fandoms.csv")
fandom_list = df["0"].tolist()

list_of_dict = []

fandom = "GENSHIN IMPACT"

for name in fandom_list:
    list_of_dict.append({"fandom":name, "ratio":Levenshtein.ratio(name, fandom)})
#print(Levenshtein.ratio("ACROSS THE SPIDER VERSE", "ACROSS THE SPIDER-VERSE"))

df2 = pd.DataFrame(list_of_dict).sort_values(by="ratio", ascending=False)

print(df2.head(20))