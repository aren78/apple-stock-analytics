import pandas as pd

df = pd.read_csv("/Users/kumbhanarendrakumar/Desktop/Apple_Stock_Analytics/etl/Data/apple.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df.to_csv(
    "/Users/kumbhanarendrakumar/Desktop/Apple_Stock_Analytics/etl/Data/apple_clean.csv",
    index=False
)

print("Cleaning Complete")