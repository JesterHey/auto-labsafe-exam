import pandas as pd

data = pd.read_csv("quizbase.csv")
data = data.drop_duplicates()
data.to_csv("quizbase.csv", index=False)