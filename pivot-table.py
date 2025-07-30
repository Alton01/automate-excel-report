import pandas as pd

df = pd.read_excel('supermarket_sales.xlsx')

df = df[['Gender', 'Product line', 'Total']]

print(df)

# plotting to see the total which each gender spends in each product line

df.pivot_table()
