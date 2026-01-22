import pandas as pd
import glob

# Load all CSV files from the data folder
files = glob.glob("data/*.csv")
df_list = []

for file in files:
    df = pd.read_csv(file)

    # Keep only rows with 'pink morsel'
    df = df[df["product"].str.lower() == "pink morsel"]

    # Create 'Sales' column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep only required columns and rename them
    df = df[["Sales", "date", "region"]]
    df = df.rename(columns={"date": "Date", "region": "Region"})

    df_list.append(df)

# Combine all cleaned data
final_df = pd.concat(df_list, ignore_index=True)

# Save to output file
final_df.to_csv("cleaned_data.csv", index=False)
print("✅ cleaned_data.csv created successfully!")
