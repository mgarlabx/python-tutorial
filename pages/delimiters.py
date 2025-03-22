import pandas as pd
import streamlit as st

data = [
    ['[]','brackets','colchetes','corchetes'],
    ['()','parentheses','parênteses','paréntesis'],
    ['{}','braces','chaves','llaves'],
    [',','comma','vírgula','coma'],
    [';','semicolon','ponto e vírgula','punto y coma'],
    [':','colon','dois pontos','dos puntos'],
    ['.','dot','ponto','punto'],
    ['"','double quotes','aspas','comillas dobles'],
    ["'",'single quotes','aspas simples','comillas simples'],
    ['-','dash','traço','guión'],
    ['_','underscore','traço baixo','guión bajo'],
    ['/','slash','barra','barra'],
    ['\\','backslash','barra invertida','barra invertida'],
    ['\#','hash','cerquilha','almohadilla / numeral'],
    ['B','bold','negrito','negrita'],
    ['U','underlined','sublinhado','subrayado'],
    ['*I*','italic','itálico','itálica'],
    ['!','exclamation mark','ponto de exclamação','signo de exclamación'],
    ['?','question mark','ponto de interrogação','signo de interrogación'],
]

df = pd.DataFrame(data, columns=['Symbol','English','Portuguese','Spanish'])

st.table(df)