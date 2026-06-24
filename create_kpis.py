import pandas as pd

df = pd.read_csv("/Users/kumbhanarendrakumar/Desktop/Apple_Stock_Analytics/etl/Data/apple_clean.csv")

print(df.columns.tolist())

df.columns = df.columns.str.strip()
# Clean price columns
price_cols = ["Open","High","Low","Close","Adj_Close"]

for col in price_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("$","",regex=False)
        .str.replace(",","",regex=False)
        .astype(float)
    )

# Clean volume
df["Volume"] = (
    df["Volume"]
    .astype(str)
    .str.replace(",","",regex=False)
    .astype(int)
)

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

df.to_csv("/Users/kumbhanarendrakumar/Desktop/Apple_Stock_Analytics/etl/Data/apple_kpi.csv", index=False)
print("Cleaning Complete")
print(df.head())




df["Daily_Return"] = (
    (df["Close"] - df["Open"])
    / df["Open"]
) * 100

df["MA30"] = df["Close"].rolling(30).mean()

df.to_csv("/Users/kumbhanarendrakumar/Desktop/Apple_Stock_Analytics/etl/Data/apple_kpi.csv", index=False)

print(df[["Date","Close","Daily_Return","MA30"]].head())