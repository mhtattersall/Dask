import dask.dataframe as ddf
from dask import delayed

# read all the csv files starting wtih 2000 in the data folder into a dask df
df = ddf.read_csv("data/2000*.csv")
print(df.head())
#df.compute()

# Compute the mean of the 'x' column
mean = df['x'].mean().compute()
print(f'mean: {mean}')

# Get the number of columns
cols = len(df.columns)
print(f'cols: {cols}')

# Get the number of rows
rows = len(df.index)
print(f'rows: {rows}')
