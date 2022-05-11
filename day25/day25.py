import pandas as pd

df=pd.read_csv("./day25/hacker_news.csv")

print(df.head())
print(df.tail())

s=pd.Series(df.columns)
print(s)

print("number of columns: ",len(df.columns))
print("number of rows: ",len(df))

print([i for i in df["title"] if "python" in i])
print([i for i in df["title"] if "JavaScript" in i])