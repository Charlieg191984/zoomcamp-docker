import sys
import pandas as pd
print("arguements", sys.argv)
month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2, 3], "num_passengers": [4, 5, 6]})
df['month'] = month
print("Month:", month)
print("hello pipeline")
print(df.head())

df.to_parquet(f"output_{month}.parquet")