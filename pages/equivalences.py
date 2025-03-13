import streamlit as st
import pandas as pd

# df = pd.read_excel('https://github.com/mgarlabx/python-tutorial/blob/main/pages/equivalences.xlsx?raw=true')
df = pd.read_excel('pages/equivalences.xlsx', engine='openpyxl')

tabStrings, tabNumbers, tabDates, tabCode, tabArrays = st.tabs(['Strings', 'Numbers', 'Dates', 'Code', 'Arrays'])

def get_row(column, row):
    language = df.columns[column]
    if language == 'mysql': language = 'sql'
    elif language == 'excel': language = 'sql'
    c1, c2 = st.columns([1,4])
    c1.write(df.columns[column])
    c2.code(row[column], language=language)

def get_df(tab):
    dff = df[df['chapter'] == tab]
    for index, row in dff.iterrows():
        st.write(f'##### :blue[{row[1]}]')
        get_row(4, row)
        get_row(2, row)
        get_row(3, row)
        get_row(5, row)
        st.divider()

with tabStrings:
    get_df('Strings')
    
with tabNumbers:
    get_df('Numbers')
    
with tabDates:
    get_df('Dates')

with tabCode:
    get_df('Code')

with tabArrays:
    get_df('Arrays')