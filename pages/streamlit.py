import streamlit as st
import numpy as np

tabIntro, tabBasic, tabSize, tabLinks, tabEquations, tabMetrics, tabIcons, tabCharts = st.tabs(["Intro", "Basic", "Size", "Links", "Equations", "Metrics", "Icons", "Charts"])

with tabIntro:
    st.image('https://streamlit.io/images/brand/streamlit-logo-primary-colormark-lighttext.png', width=300)
    st.write('This is a Streamlit cheat sheet')
    st.write('You can find the official cheat sheet [here](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)')
    st.write('You can find the API reference [here](https://docs.streamlit.io/library/api-reference)')
    
with tabBasic:
    def write(body):
        with st.container():
            st.code(f"st.write('{body}')")
            st.write(body)
            st.divider()

    write('Hello World!')
    write(':red[Hello World!]')
    write(':blue[Hello World!]')
    write('**Hello World!**')
    write('*Hello World!*')
    write(1234)
    write('1234')
    
with tabSize:
    st.code("st.title('This is a title')")
    st.title('This is a title')
    st.divider()
    st.code("st.title('This is a title with help', help='This is a help text')")
    st.title('This is a title with help', help='This is a help text')
    st.divider()
    st.code("st.header('This is a header')")
    st.header('This is a header')
    st.divider()
    st.code("st.header('This is a subheader')")
    st.subheader('This is a subheader')
    st.divider()
    st.code("st.caption('This is a caption')")
    st.caption('This is a caption')
    st.divider()
    write('# Hello World!')
    write('## Hello World!')
    write('### Hello World!')
    
with tabLinks:
    write('This is a link: [Google](https://www.google.com)')
    st.write(':gray[Use st.text() to avoid markdown rendering]')
    st.code("st.text('This is not a link: [Google](https://www.google.com)')")
    st.text('This is not a link: [Google](https://www.google.com)')
    st.divider()
    st.code("st.page_link('https://www.google.com', label='Google', icon='🌎')")
    st.page_link('https://www.google.com', label='Google', icon='🌎')
    st.divider()

with tabEquations:
    write('This is an equation: $x^2 + y^2 = z^2$')   
    body = 'Bhaskara formula: $x = \\\\frac{-b \\\\pm \\\\sqrt{b^2 - 4ac}}{2a}$'
    st.code(f"st.write('{body}')")
    st.write('Bhaskara formula: $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$')
    st.divider()
    st.code("st.latex('x = \\\\frac{-b \\\\pm \\\\sqrt{b^2 - 4ac}}{2a}')")
    st.latex('x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}')
    st.divider()
    
with tabMetrics:
    st.code("st.metric('This is a metric', 1234)")
    st.metric('This is a metric', 1234)
    st.divider()
    st.code("st.metric('This is a metric', 1234, border=True)")
    st.metric('This is a metric', 1234, border=True)
    st.divider()
    st.code("st.metric('This is a metric', 1234, delta=0.1, border=True)")
    st.metric('This is a metric', 1234, delta=0.1, border=True)
    
with tabIcons:
    st.write('Full icons list [here](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)')
    st.write(' ')
    write('This is an icon: :smiley:')
    write('This is an icon: :rocket:')
    write('This is an icon: :heart:')
    write('This is an icon: :star:')
    
with tabCharts:
    st.write('Charts API reference [here](https://docs.streamlit.io/develop/api-reference/charts)')
    st.write(' ')
    st.code("st.line_chart(np.random.randn(10, 2))")
    st.line_chart(np.random.randn(10, 2))
    st.divider()
    st.code("st.area_chart(np.random.randn(10, 2))")
    st.area_chart(np.random.randn(10, 2))
    st.divider()
    st.code("st.bar_chart(np.random.randn(10, 2))")
    st.bar_chart(np.random.randn(10, 2))
    st.divider()

