import pandas as pd

df = pd.read_csv("data/large_file.csv", nrows=1000)
df.to_csv("output/first_1000.csv", index=False)
