import pandas as pd

data = pd.read_csv("quzibase.csv")
data = data.drop_duplicates()
data.to_csv("quzibase.csv", index=False)