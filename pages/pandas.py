import streamlit as st

tabBasic, tabSettings, tabJoins, tabGroup, tabCharts, tabXXX = st.tabs(['Basic', 'Settings', 'Joins', 'Group', 'Charts', 'XXX'])

def print_code(code, option=True):
    if option: st.code('import pandas as pd', language='python')    
    st.code(code, language='python')
    

with tabBasic:
    code = '''
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
    print_code(code)
    

with tabSettings:
    code = '''
    # display all columns
    pd.set_option('display.max_columns', None) 

    # display 100 rows
    pd.set_option('display.max_rows', 100) 

    # pandas version
    x = pd.__version__  
    print(x)
    '''   
    print_code(code)
    
with tabJoins:
    st.write('More about joins [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)')
    code = '''
    # Creating dataframes for testing

    df1 = pd.DataFrame()
    df1['A'] = ['A0', 'A1', 'A2', 'A3']
    df1['B'] = ['B0', 'B1', 'B2', 'B3']
    df1['X'] = ['X0', 'X1', 'X2', 'X3']

    df2 = pd.DataFrame()
    df2['C'] = ['C0', 'C1', 'C2', 'C3']
    df2['D'] = ['D0', 'D1', 'D2', 'D3']
    df2['E'] = ['E0', 'E1', 'E2', 'E3']

    df3 = pd.DataFrame()
    df3['A'] = ['A0', 'A1', 'A5', 'A6']
    df3['C'] = ['C0', 'C1', 'C2', 'C3']
    df3['D'] = ['D0', 'D1', 'D2', 'D3']

    df4 = pd.DataFrame()
    df4['E'] = ['A0', 'A1', 'A5', 'A6']
    df4['C'] = ['C0', 'C1', 'C2', 'C3']
    df4['D'] = ['D0', 'D1', 'D2', 'D3']

    df5 = pd.DataFrame()
    df5['A'] = ['A0', 'A1', 'A5', 'A6']
    df5['B'] = ['B0', 'B1', 'B2', 'B3']
    df5['C'] = ['C0', 'C1', 'C2', 'C3']
    df5['D'] = ['D0', 'D1', 'D2', 'D3']
    '''   
    print_code(code)
    
    code = '''
    # JOIN
    # both dataframes must have the same number of rows
    # no key is needed, rows are joined at the right
    df = df1.join(df2)
    print(df)
    '''   
    print_code(code, False)
    
    code = '''
    # CONCAT HORIZONTAL
    # same as above, rows are joined at the right
    df = pd.concat([df1, df2], axis=1) # axis=1 is horizontal
    print(df)
    '''   
    print_code(code, False)

    code = '''
    # CONCAT VERTICAL
    # rows are joined at the bottom
    df = pd.concat([df1, df2], axis=0) # axis=0 is vertical (default, can be omitted)
    print(df)
    '''   
    print_code(code, False)

    code = '''
    # MERGE
    # Similar to SQL joins

    # inner join
    df = pd.merge(df1, df3, on='A', how='inner') 
    print(df)

    # left join
    df = pd.merge(df1, df3, on='A', how='left') 
    print(df)

    # right join
    df = pd.merge(df1, df3, on='A', how='right') 
    print(df)
    '''   
    print_code(code, False)

    code = '''
    # Merging on different columns
    df = pd.merge(df1, df4, left_on='A', right_on='E', how='inner') 
    print(df)
    '''   
    print_code(code, False)

    code = '''
    # Merging on multiple columns
    df = pd.merge(df1, df5, on=['A', 'B'], how='inner') 
    print(df)
    '''   
    print_code(code, False)

    code = '''
    # APPEND IS DEPRECATED
    # Use concat() instead
    '''   
    print_code(code, False)

with tabXXX:
    code = '''
    xxx
    '''   
    print_code(code)