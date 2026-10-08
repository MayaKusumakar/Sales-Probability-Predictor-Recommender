import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-Sales-Win-Loss.csv")

print("Rows and columns:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nAny missing values?")
print(df.isnull().sum())

print("\nWin vs Loss breakdown:")
print(df["Opportunity Result"].value_counts())
