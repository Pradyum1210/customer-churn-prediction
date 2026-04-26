import pandas as pd

def preprocess_data(path):
  data = pd.read_csv(path)

  print(f"\nColumns: {data.shape[1]} and Rows: {data.shape[0]}\n")

  # Null check
  if data.isnull().sum().sum() == 0:
    print("\nNo null value\n")
  else:
    print("Some null values")

  # Remove duplicates
  data = data.drop_duplicates()

  # Handle empty space
  for col in data.columns:
    data[col] = data[col].replace(" ", None)

  # Handle TotalCharges
  data = data.dropna()
  data["TotalCharges"] = pd.to_numeric(data["TotalCharges"])
  

  data["charges_group"] = pd.cut(
    data["MonthlyCharges"],
    bins=[0, 35, 70, 120],
    labels=["Low", "Medium", "High"]
  )

  return data