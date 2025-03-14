import streamlit as st

tabSettings, tabBasic, tabUpdate, tabLoops, tabJoins, tabGroupBy, tabCrossTab, tabPivotTable, tabCharts, tabDataSci = st.tabs(['Settings', 'Basic', 'Update', 'Loops', 'Joins', 'GroupBy', 'CrossTab', 'PivotTable', 'Charts', 'DataSci'])

def print_code(code, option=True):
    if option: st.code('import pandas as pd', language='python')    
    st.code(code, language='python')
    


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


with tabBasic:
    code = '''
    # read a csv file
    file_path = 'https://raw.githubusercontent.com/mgarlabx/solverpills/refs/heads/main/files/sales.csv'
    df = pd.read_csv(file_path)
    '''
    print_code(code)
    
    code = '''
    # show the first 5 rows
    x = df.head()
    print(x)
    '''
    print_code(code, False)

    code = '''
    # show only selected columns
    columns = ['Date', 'Payment', 'Total']
    x = df[columns]
    print(x)
    '''
    print_code(code, False)

    code = '''
    # show only selected rows
    condition = (df['Payment'] == 'Cash')
    x = df[condition]
    print(x)
    '''
    print_code(code, False)

    code = '''
    # show only selected columns and rows
    x = df[columns][condition]
    print(x)
    '''
    print_code(code, False)


with tabUpdate:
    code = '''
    # Drop columns
    df = df.drop(columns=['Payment']) # drop column 'Payment'
    df = df.drop(columns=[df.columns[0]]) # drop first column
    '''   
    print_code(code)
    
    code = '''
    # Rename columns
    df = df.rename(columns={'Payment': 'Method'}) # rename column 'Payment' to 'Method'
    df = df.rename(columns={df.columns[0]: 'Date'}) # rename first column to 'Date'
    '''   
    print_code(code, False)
    
    code = '''
    # Sort values
    df = df.sort_values(by='Date', ascending=False) # sort by 'Date' in descending order
    df = df.sort_values(by=['Date', 'Total'], ascending=False) # sort by 'Date' and 'Total' in descending order
    df = df.sort_values(by=['Date', 'Total'], ascending=[False, True) # sort by 'Date' in descending order and 'Total' in ascending order
    '''   
    print_code(code, False)

    code = '''
    # Update values
    df.loc[df['Payment'] == 'Cash', 'Payment'] = 'Cash Payment' # update 'Payment' column
    df.loc[df['Payment'] == 'Cash', ['Payment', 'Total']] = ['Cash Payment', 0] # update 'Payment' and 'Total' columns
    '''   
    print_code(code, False)

    code = '''
    # Replace values
    df = df.replace({'Payment': 'Cash'}, 'Cash Payment') # replace 'Payment' column
    df = df.replace({'Payment': {'Cash': 'Cash Payment', 'Card': 'Card Payment'}}) # replace 'Payment' column

    '''   
    print_code(code, False)

    
with tabLoops:
    code = '''
    # Loop through rows
    for index, row in df.iterrows():
        print(row['Date'], row['Payment'], row['Total'])
    '''   
    print_code(code)
    
    code = '''
    # Apply function
    def increase_total(x):
        return x * 1.1
        
    df['Total'] = df['Total'].apply(increase_total) # increase 'Total' by 10%
    '''   
    print_code(code, False)
    
    code = '''
    # Apply lambda
    df['Total'] = df['Total'].apply(lambda x: x * 1.1) # increase 'Total' by 10%
    '''   
    print_code(code, False)

    
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


with tabGroupBy:
    st.write('groupby = ONE COLUMN')
    
    code = '''
    # read a csv file
    file_path = 'https://raw.githubusercontent.com/mgarlabx/solverpills/refs/heads/main/files/sales.csv'
    df = pd.read_csv(file_path)
    '''   
    print_code(code)
    
    code = '''
    # Simple count by column
    x = df['Payment'].value_counts()
    print(x)
    '''   
    print_code(code, False)
    
    code = '''
    # Count, sum, mean
    x = df.groupby('Payment')['Total'].count()
    print(x)
    
    x = df.groupby('Payment')['Total'].sum()
    print(x)
    
    x = df.groupby('Payment')['Total'].mean()
    print(x)
    
    x = df.groupby('Payment')['Total'].agg(['count', 'sum', 'mean'])
    print(x)
    '''   
    print_code(code, False)

    code = '''
    # Advanced groupby
    x = df.groupby('Payment').agg(
        count = ('Total', 'count'),
        sum = ('Total', 'sum'),
        mean = ('Total', 'mean'),
        unique = ('Total', 'nunique'),
        above100 = ('Total', lambda x: x[x>100].count())
    )
    print(x)
    '''   
    print_code(code, False)

    
with tabCrossTab:
    st.write('crosstab = TWO COLUMNS')

    code = '''
    # read a csv file
    file_path = 'https://raw.githubusercontent.com/mgarlabx/solverpills/refs/heads/main/files/sales.csv'
    df = pd.read_csv(file_path)
    '''   
    print_code(code)
        
    code = '''
    # aggfunc options: sum, mean, max, min, median, var, std, first, last, count, nunique
    x = pd.crosstab(df['City'], df['Payment'], values=df['Total'], aggfunc='sum') 
    print(x)
    '''   
    print_code(code, False)

    code = '''
    # totals
    x = pd.crosstab(df['City'], df['Payment'], values=df['Total'], aggfunc='sum', margins=True, margins_name='Total')
    print(x)
    '''   
    print_code(code, False)
    
    code = '''
    # percentage
    x = pd.crosstab(df['City'], df['Payment'], values=df['Total'], aggfunc='sum', normalize='all') # all, index (horiz), columns (vert)
    print(x)
    '''   
    print_code(code, False)

    
with tabPivotTable:
    st.write('pivot_table = MULTIPLE COLUMNS')
        
    code = '''
    # read a csv file
    file_path = 'https://raw.githubusercontent.com/mgarlabx/solverpills/refs/heads/main/files/sales.csv'
    df = pd.read_csv(file_path)
    '''   
    print_code(code)

    code = '''
    # 1 x 1 columns
    x = pd.pivot_table(df, values='Total', index=['Payment'], columns=['City'], aggfunc='sum')
    print(x)
    '''   
    print_code(code, False)
    
    code = '''
    # 2 x 1 columns
    x = pd.pivot_table(df, values='Total', index=['Payment', 'Product line'], columns=['City'], aggfunc='sum')
    print(x)
    '''   
    print_code(code, False)

    code = '''
    # 2 x 2 columns
    x = pd.pivot_table(df, values='Total', index=['Payment', 'Product line'], columns=['Gender', 'City'], aggfunc='sum')
    print(x)
    '''   
    print_code(code, False)


with tabCharts:
    code = '''
    # read a csv file
    file_path = 'https://raw.githubusercontent.com/mgarlabx/solverpills/refs/heads/main/files/sales.csv'
    df = pd.read_csv(file_path)
    '''   
    print_code(code)
        
    code = '''
    # Histogram basic
    x = df['Total'].hist()
    print(x)
    '''   
    print_code(code, False)
    
    code = '''
    # Histogram advanced
    x = df['Total'].hist(bins=30, grid=False, color='blue', zorder=2, rwidth=0.9)
    print(x)
    '''   
    print_code(code, False)
    
    code = '''
    # Line chart
    x = df.groupby('Payment')['Total'].sum().plot(kind='line', title='Total Sales by Payment Method')
    print(x)
    '''   
    print_code(code, False)
    
    code = '''
    # Bar chart
    x = pd.crosstab(df['City'], df['Payment'], values=df['Total'], aggfunc='sum').plot(kind='bar')
    print(x)
    '''   
    print_code(code, False)

    code = '''
    # Stacked bar chart
    x = pd.crosstab(df['City'], df['Payment'], values=df['Total'], aggfunc='sum').plot(kind='bar', stacked=True)
    print(x)
    '''   
    print_code(code, False)

with tabDataSci:
    code = '''
    # read a csv file
    file_path = 'https://raw.githubusercontent.com/mgarlabx/solverpills/refs/heads/main/files/sales.csv'
    df = pd.read_csv(file_path)
    '''   
    print_code(code)
        
    code = '''
    # correlation
    df[['Total', 'Tax 5%', 'Unit price']].corr()
    '''   
    print_code(code, False)

    code = '''
    # deleting outliers out of 2 standard deviations
    upper_limit = df['Total'].mean() + 2 * df['Total'].std()
    lower_limit = df['Total'].mean() - 2 * df['Total'].std()
    dff = df[(df['Total'] > upper_limit) | (df['Total'] < lower_limit)]
    x = df.shape[0], dff.shape[0]
    print(x)
    '''   
    print_code(code, False)

    code = '''
    # deleting outliers out of 5% quantile
    upper_limit = df['Total'].quantile(0.95)
    lower_limit = df['Total'].quantile(0.05)
    dff = df[(df['Total'] > upper_limit) | (df['Total'] < lower_limit)]
    x = df.shape[0], dff.shape[0]
    print(x)
    '''   
    print_code(code, False)

    code = '''
    # replacing outliers with cap values
    upper_limit = df['Total'].quantile(0.95)
    lower_limit = df['Total'].quantile(0.05)
    dff = df.copy()
    dff.loc[(dff['Total'] > upper_limit), 'Total'] = upper_limit
    dff.loc[(dff['Total'] < lower_limit), 'Total'] = lower_limit
    x = df['Total'].max(), dff['Total'].max()
    print(x)
    '''   
    print_code(code, False)

    code = '''
    # Normalization
    dff = df.copy()
    dff['Total'] = (dff['Total'] - dff['Total'].min()) / (dff['Total'].max() - dff['Total'].min())
    x = df['Total'].max(), dff['Total'].max()
    print(x)
    '''   
    print_code(code, False)

    code = '''
    # Standardization
    dff = df.copy()
    dff['Total'] = (dff['Total'] - dff['Total'].mean()) / dff['Total'].std()
    x = df['Total'].mean(), dff['Total'].mean()
    print(x)
    '''   
    print_code(code, False)

    code = '''
    # Binning (bucketing)

    # fixed-width binning
    bins = 3 
    labels = ['low', 'medium', 'high']
    df['Total_bin_fixed'] = pd.cut(df['Total'], bins=bins, labels=labels)

    # binning based on custom ranges
    bins = [0, 100, 500, 1000, 5000, 10000]
    labels = ['very low', 'low', 'medium', 'high', 'very high']
    df['Total_bin_custom'] = pd.cut(df['Total'], bins=bins, labels=labels)

    # quantile-based binning
    bins = 3
    labels = ['low', 'medium', 'high']
    df['Total_bin_quantile'] = pd.qcut(df['Total'], q=bins, labels=labels)
    '''   
    print_code(code, False)

    code = '''
    # One-hot encoding
    encoded_columns = pd.get_dummies(df['City'])
    dff = df.join(encoded_columns)
    x = df.shape[1], dff.shape[1]
    print(x)
    '''   
    print_code(code, False)

