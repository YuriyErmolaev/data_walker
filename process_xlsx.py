import pandas as pd

df = pd.read_excel("data/large_file.xlsx", nrows=1000)
df.to_excel("output/first_1000.xlsx", index=False)
