import streamlit as st

tabBasic, tabGroup, tabCharts = st.tabs(['Basic', 'Group', 'Charts'])

with tabBasic:
    code = '''
import pandas as pd

# read a csv file
file_path = 'https://raw.githubusercontent.com/mgarlabx/solverpills/refs/heads/main/files/sales.csv'
df = pd.read_csv(file_path)

# show the first 5 rows
x = df.head()
print(x)

# show only selected columns
columns = ['Date', 'Payment', 'Total']
x = df[columns]
print(x)

# show only selected rows
condition = (df['Payment'] == 'Cash')
x = df[condition]
print(x)

# show only selected columns and rows
x = df[columns][condition]
print(x)
    '''
    st.code(code, language='python')