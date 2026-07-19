import pandas as pd
import sqlite3
import sqlalchemy

# --- Step 1: Read the data from the SQLite database file ---
try:
    conn_sqlite = sqlite3.connect('nselife.db')
    df = pd.read_sql_query("SELECT * FROM nselife_prices", conn_sqlite)
    conn_sqlite.close()
    print("Data successfully read from the SQLite database.")

except Exception as e:
    print(f"Error reading from SQLite: {e}")
    exit()


# --- Step 2: Export the DataFrame to the PostgreSQL database ---
# These are your PostgreSQL credentials
db_user = 'postgres'  # Correctly changed to the default user
db_password = 'XXXXXXXXXXXXXXXXX' # check file in local computer disk
db_host = 'localhost'
db_port = '5432'
db_name = 'n1'

try:
    # Correctly formatted connection string
    connection_string = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    engine = sqlalchemy.create_engine(connection_string)

    df.to_sql(
        name='cipla_prices_from_sqlite',
        con=engine,
        if_exists='replace',
        index=False
    )

    print("Data successfully exported to PostgreSQL.")

except Exception as e:
    print(f"Error exporting to PostgreSQL: {e}")

finally:
    if 'engine' in locals():
        engine.dispose()

