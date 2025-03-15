import streamlit as st

tabFStrings, tabDates = st.tabs(["f-strings", "Dates"])

with tabFStrings:
    st.code('''
            myValue = 1234.5678
            print(f"{myValue:.2f}") # 1234.57
            # same of
            print("{:.2f}".format(myValue)) # 1234.57
            ''')    
    st.code('''
            myValue = 9876543.21
            print(f"{myValue:,.0f}") # integer 9,876,543
            print(f"{myValue:,.2f}") # float 9,876,543.21
            print(f"US$ {myValue:,.2f}") # currency US$ 9,876,543.21
            ''')
    st.code('''
            myValue = 255
            print(f"{myValue:.2e}") # scientific 2.55e+02
            print(f"{myValue:b}") # binary 11111111
            print(f"{myValue:o}") # octal 377
            print(f"{myValue:x}") # hexa (lower) ff
            print(f"{myValue:X}") # hexa (upper) FF
            ''')
    st.code('''
            myValue = 1234
            print(f"{myValue:>10,.0f}") # padding left      1,234
            print(f"{myValue:<10,.0f}") # padding right 1,234  
            print(f"{myValue:010,.0f}") # fill zeros 00,001,234
            ''')
    st.code('''
            myValue = 0.1234
            print(f"{myValue:.2%}") # percentage 12.34%
            ''')

with tabDates:
    st.code('''
            from datetime import datetime
            ''')
    st.code('''
            myDate = datetime(2025, 3, 10, 14, 30, 15) 
            print(myDate.strftime("%d/%m/%Y")) # 10/03/2025 
            print(myDate.strftime("%Y-%m-%d")) # 2025-03-10
            print(myDate.strftime("%Y-%m"))  # 2025-03
            print(myDate.strftime("%d of %B of %Y")) # 10 de março de 2025
            print(myDate.strftime("%A, %d de %B de %Y")) # Segunda, 10 de março de 2025
            print(myDate.strftime("%Y-%m-%dT%H:%M:%S")) # 2025-03-10T14:30:15 --- ISO 8601
            print(myDate.strftime("%d/%m/%Y %H:%M:%S")) # 10/03/2025 14:30:15
            print(myDate.strftime("%I:%M %p")) # 02:30 PM
            ''')
    st.code('''
            myDate_str = "10/03/2025 14:30:15"
            myDate = datetime.strptime(myDate_str, "%d/%m/%Y %H:%M:%S")
            print(myDate) # 2025-03-10 14:30:15
            ''')
    st.code('''
            myDate = datetime.now()
            print(myDate.strftime("%d/%m/%Y %H:%M:%S")) # 10/03/2025 14:45:20
            ''')







