import streamlit as st

tabFStrings, tabDates, tabPrint = st.tabs(["f-strings", "Dates", "print"])

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

with tabPrint:
        st.code('''
            dre = [
                ['gross revenues', 0, 875000, 2950000, 9270000, 25515000, 46462560],
                ['bad debt prov', 0, -43750.0, -147500.0, -463500.0, -1275750.0, -2323128.0],
                ['net revenues', 0, 831250.0, 2802500.0, 8806500.0, 24239250.0, 44139432.0],
                ['headcount', -2205600.0, -2920800.0, -5469600.0, -6004800.0, -8078400.0, -9052800.0],
                ['marketing', -500000.04, -437500.0, -737500.0, -927000.0, -1786050.0, -2323128.0],
                ['facilities', -600000, -600000, -600000, -984000, -984000, -984000],
                ['other', -330560.004, -395830.0, -680710.0, -791580.0, -1084845.0, -1235992.8],
                ['total expenses', -3636160.044, -4354130.0, -7487810.0, -8707380.0, -11933295.0, -13595920.8],
                ['ebitda', -3636160.044, -3522880.0, -4685310.0, 99120.0, 12305955.0, 30543511.2],
                ['capex', -300000.0, -200000.0, -100000.0, -100000.0, -200000.0, -400000.0],
                ['taxes', 0.0, 0.0, 0.0, -177534.0, -1845893.25, -4581526.68],
                ['cash flow', -3936160.044, -3722880.0, -4785310.0, -178414.0, 10260061.75, 25561984.52]
            ]
            ''')
        
        st.code('''
                print('DRE'.center(116, ' '))
                print('-' * 116)
                print(' ')
                r = 0
                for i in dre:
                    print(i[0].ljust(18, ' '), end='\t')
                    for j in range(1, 7):
                        print(f'{i[j]:,.0f}'.rjust(12, ' '), end='\t')
                    print()
                    if r == 2 or r == 7 or r == 8 or r == 10:
                        print(' ')
                    r += 1
            ''')






