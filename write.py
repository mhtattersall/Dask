import dask
import os
import datetime

# Create a 'data' directory if it doesn't exist
if not os.path.exists('data'):
    os.mkdir('data')

# Function to generate file names based on date
def name(i):
    return str(datetime.date(2000, 1,1) + i * datetime.timedelta(days=1))

# Create a Dask dataframe with synthetic timeseries data
df = dask.datasets.timeseries()

# Save the dataframe to CSV files in the 'data' directory
df.to_csv('data/*.csv', name_function=name)

