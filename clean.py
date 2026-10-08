import pandas as pd
 
df = pd.read_csv("WA_Fn-UseC_-Sales-Win-Loss.csv")
 
KEEP_COLUMNS = [
"Opportunity Number",
"Opportunity Result",
"Opportunity Amount USD",
"Elapsed Days In Sales Stage",
"Sales Stage Change Count",
"Client Size By Revenue",
"Route To Market",
"Supplies Subgroup",
"Competitor Type",
"Revenue From Client Past Two Years",
]
 
df = df[KEEP_COLUMNS].copy()
 
df["Competitor Type"] = df["Competitor Type"].fillna("No Competitor")
print("\nMissing values after cleaning:")
print(df.isnull().sum())
 
print("Shape after dropping columns:", df.shape)
print("\nColumns kept:")
print(df.columns.tolist())
 
print("\nCompetitor Type values now:")
print(df["Competitor Type"].value_counts())
 
# Turn the win/loss word column into 1/0 (1 = Won, 0 = Loss)
df["Opportunity Result"] = (df["Opportunity Result"] == "Won").astype(int)
 
categorical_cols = [
    "Route To Market",
    "Supplies Subgroup",
    "Competitor Type"
]
 
for col in categorical_cols:
    df[col] = df[col].astype("category")
 
print("\nShape after converting words to numbers:", df.shape)
print("\nAll column names now:")
print(df.columns.tolist())
 
print("\nFirst 3 rows:")
print(df.head(3))
 
from sklearn.model_selection import train_test_split
 
# Split into a learning pile (80%) and a hidden testing pile (20%).
# stratify=df["Opportunity Result"] makes sure both piles have the same
# won/loss mix as the full dataset (roughly 22.6% won, 77.4% loss in each).
train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["Opportunity Result"],
)
 
print("\nTraining pile size:", train_df.shape)
print("Testing pile size:", test_df.shape)
 
print("\nWin rate in training pile:", train_df["Opportunity Result"].mean())
print("Win rate in testing pile:", test_df["Opportunity Result"].mean())
 
train_df.to_csv("train_data.csv", index=False)
test_df.to_csv("test_data.csv", index=False)
print("\nSaved train_data.csv and test_data.csv")