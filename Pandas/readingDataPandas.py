import numpy as np
import pandas as pd
import sqlite3
from numpy.random import randn

# -------------------- CSV --------------------
print("\n📄 CSV Section:")
df_csv = pd.read_csv('data.csv')  # Make sure this file exists
print(df_csv)

# -------------------- Excel --------------------
print("\n📊 Excel Section:")
excel_data = {
    'Name': ['Safwan', 'Hamza', 'Ayan'],
    'Age': [21, 22, 23],
    'Grade': ['A', 'B', 'B+']
}
df_excel = pd.DataFrame(excel_data)
df_excel.to_excel('output.xlsx', index=False)
print(df_excel)

# -------------------- HTML --------------------
print("\n🌐 HTML Table from FDIC:")
html_data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
df_html = html_data[0]
print(df_html.head())  # Print first few rows for brevity

# -------------------- SQL --------------------
print("\n🗃 SQL Database:")
conn = sqlite3.connect('mydata.db')

sql_data = {
    'Name': ['Safwan', 'Hamza', 'Zoha'],
    'Age': [21, 21, 20],
    'Field': ['Data Science', 'Blockchain', 'Machine Learning']
}
df_sql = pd.DataFrame(sql_data)

df_sql.to_sql('students', conn, if_exists='replace', index=False)

query_df = pd.read_sql('SELECT * FROM students', conn)
print(query_df)

# Always close the connection when done
conn.close()
