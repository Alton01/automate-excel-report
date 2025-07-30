import pandas as pd

df = pd.read_excel('supermarket_sales.xlsx')

df = df[['Gender', 'Product line', 'Total']]

# plotting to see the total which each gender spends in each product line

pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)

# export pivot table in excel format
pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)
