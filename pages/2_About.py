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

def show_about():
    yol = "HTML/container_background.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', 'For your information...')
    st.markdown(contents, unsafe_allow_html=True)

    font_color("E-Commerce is so hot today🔥")
    st.markdown("""
            * From 2019 to 2022, there was a **45% increase** of e-commerce sellers.
            * By 16 March 2021, **472,000** sellers had joined Amazon Marketplace.
            * The competition is getting greater. Therefore, to stand out among the competitors, sentiment analysis on the reviews is very important.
            """)
    st.write("""***""")
    col1, col2 = st.columns([3, 5])
    with col2:
        font_color("What is sentiment analysis?🤷‍")
        st.write("""##### The process of compiling and examining the opinions, ideas, and impressions of people. In short, to know your customers feel: """)
        st.markdown("""
                * Positive
                * Negative
                """)
        st.write("""##### to your product!""")

    with col1:
        sentiment_img = Image.open("image/sentiment analysis.jpg")
        st.image(sentiment_img, use_column_width=True)
    st.write("""***""")

    st.markdown("""
    <style>
    .big-font {
        font-size:70px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">About This Project</p>', unsafe_allow_html=True)
    st.write("##### This is the final product of my Data Science Project. It is mainly used to help e-Commerce sellers to understand the reviews collected by using visualisations and machine learning model predictions.")
    st.write("""***""")

    font_color("Problem Statement")
    st.write("When it comes to sentiment analysis, we are talking about customers’ emotions towards the product, for example, positive or negative. However, sellers do not know **which part of the product or service needs improvement**.")
    st.write("""***""")

    font_color("Objectives")
    st.markdown("""
                    * To identify the topics and keywords of the product reviews.
                    * To build a model to identify the topic of a review and predict its sentiment.
                    * To present a dashboard about the topics and keywords as well as the average ratings of each product.
                    """)
    st.write("""***""")

    font_color("Data Source")
    st.write("The dataset that will be used in this project is Product Reviews acquired from Amazon website. I will use the reviews from 6 different types of products, which are air purifier, lamp, kettle, air fryer, chair and plate. The URL links are here:")
    st.markdown("""
                * [Air fryer](https://www.amazon.com/COSORI-One-Touch-Reminder-Dishwasher-Safe-Detachable/product-reviews/B07GJBBGHG/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1)
                * [Air purifier](https://www.amazon.com/LEVOIT-Purifier-Home-Allergies-Pets/product-reviews/B07VVK39F7/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1)
                * [Chair](https://www.amazon.com/Walker-Edison-Douglas-Industrial-Leather/product-reviews/B07DPMRZNR/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1)
                * [Kettle](https://www.amazon.com/Mueller-Electric-SpeedBoil-Borosilicate-Protection/product-reviews/B07TZ5YHJN/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1)                
                * [Lamp](https://www.amazon.com/JOOFO-Torchiere-Temperatures-Lamps-Tall-Office%EF%BC%88Black%EF%BC%89/product-reviews/B07WFC14VR/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1)
                * [Plate](https://www.amazon.com/Corelle-Winter-Dinnerware-18-Piece-Service/product-reviews/B00R790CLY/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1)
                """)
    st.write("""***""")

show_about()
