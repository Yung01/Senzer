import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Senzer🧐",
)

def font_color(text):
    yol = "HTML/text_colour.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', text)
    st.markdown(contents, unsafe_allow_html=True)

def show_home():
    st.title('Senzer: A Sentiment Analyzer')
    st.write("E-Commerce 🧐 Sentiment Analysis")
    home_img = Image.open("image/eCommerce.jpg")
    st.image(home_img, use_column_width=True)
    st.write("""##### Welcome to :green[SENZER]! Scroll down to have a look on the :green[User Manual]!""")
    st.write("""***""")

    font_color("User Manual📝")
    st.write("""##### There 4 pages in this application:""")
    st.markdown("""
                * **Home page** 
                User manual
                * **About**
                General knowledge about e-Commerce, sentiment analysis and information about my project
                * **Dashboard** 
                Visualizations about data of 6 different products on Amazon  
                * **Let's Predict!** 
                Enter the review and predict the sentiment of the review! 
                """)


show_home()


st.markdown("""
<style>
.big-font {
    font-size:150px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Let\'s Start!</p>', unsafe_allow_html=True)

