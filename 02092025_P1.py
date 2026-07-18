import pandas as pd
import sqlite3
from nselib.capital_market import price_volume_data

# Fetch the data
data_1 = price_volume_data(symbol='CIPLA', from_date='1-8-2025', to_date='1-6-2026')

# Create a new DataFrame with just 'Date' and 'ClosePrice'
df_to_export = data_1[['Date', 'ClosePrice']]

# Create a connection to a SQLite database file
conn = sqlite3.connect('nselife.db')

# Export the DataFrame to a SQL table named 'nselife_prices'
# If the table exists, it will be replaced.
df_to_export.to_sql(name='nselife_prices', con=conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

print("Data exported successfully to nselife.db in a table named 'nselife_prices'.")
