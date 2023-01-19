import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from nltk import FreqDist
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from wordcloud import WordCloud

st.set_page_config(
    page_title="Senzer🧐",
)
def show_dashboard():
    yol = "HTML/container_background.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', 'Dashboard📈')
    st.markdown(contents, unsafe_allow_html=True)
    font_color("Which product you would like to know more?")
    product, df = choose_data()

    col1, col2= st.columns(2)
    with col1:
        st.subheader("Number of Reviews:")
        st.write("The " + str(product) + " received ", len(df), "reviews from its buyers.")
    with col2:
        st.subheader("Average Star Rates:")
        average_rating = round(df["rating"].mean(), 1)
        star_rating = ":star:" * int(round(average_rating, 0))
        st.subheader(f"{average_rating} {star_rating}")

    st.write("""***""")

    st.subheader("How people feel with the product?")
    colA, colB = st.columns(2)
    with colA:
        img = Image.open("image/pos.jpg")
        st.image(img, use_column_width=True)
        a = str(len(df[df['sentiment'] == 1]))
        st.subheader(a)
    with colB:
        img = Image.open("image/neg.jpg")
        st.image(img, use_column_width=True)
        a = str(len(df[df['sentiment'] == 0]))
        st.subheader(a)

    st.write("""***""")
    # graph1
    st.subheader("The distribution of star rates is as below:")
    df_rating = df.groupby([df.rating]).size().reset_index().rename(columns = {0: 'counts'})
    chart_star_rate = px.bar(
        df_rating,
        x="rating",
        y="counts",
        orientation='v',
        template="plotly_white")
    st.plotly_chart(chart_star_rate)

    st.write("""***""")

    # graph2
    st.subheader("Top 20 words that appear in the reviews:")
    freq_words(df['Clean Review'])

    st.write("""***""")

    st.subheader('Topics of the Reviews')
    st.write("Generally, there are 2 topics each about the positive reviews & negative reviews.")

    dataframe = pd.DataFrame(df, columns=['rating', 'combinedReview', 'Clean Review', 'sentiment'])
    df_pos = dataframe[dataframe['sentiment'] == 1]
    df_neg = dataframe[dataframe['sentiment'] == 0]

    st.subheader(":green[POSITIVE] reviews")
    # Create & generate a word cloud image:
    wordcloud = WordCloud().generate(str(df_pos['Clean Review']))
    # Display the generated image:
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(fig)
    st.subheader("Topics & the keywords with weight:")

    pos1, pos2, pos_topic1, pos_topic2, neg_topic1, neg_topic2 = get_pos_keyword(product)
    st.write("Topic 1: "+ str(pos_topic1))
    word_weight = px.bar(
            pos1,
            x="word",
            y="weight",
            orientation='v',
            template="plotly_white")
    st.plotly_chart(word_weight)

    st.write("Topic 2: "+ str(pos_topic2))
    word_weight = px.bar(
            pos2,
            x="word",
            y="weight",
            orientation='v',
            template="plotly_white")
    st.plotly_chart(word_weight)

    st.subheader(":red[NEGATIVE] reviews")
    # Create & generate a word cloud image:
    wordcloud = WordCloud().generate(str(df_neg['Clean Review']))
    # Display the generated image:
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(fig)


    st.write("Topic 1: "+str(neg_topic1))
    neg1, neg2 = get_neg_keyword(product)
    word_weight = px.bar(
            neg1,
            x="word",
            y="weight",
            orientation='v',
            template="plotly_white")
    st.plotly_chart(word_weight)

    st.write("Topic 2: "+ str(neg_topic2))
    word_weight = px.bar(
            neg2,
            x="word",
            y="weight",
            orientation='v',
            template="plotly_white")
    st.plotly_chart(word_weight)



def choose_data():
    product = st.selectbox(
        'Choose one',
        ('Air Fryer', 'Air Purifier', 'Chair','Kettle','Lamp','Plate'))
    if (product == 'Air Fryer'):
        dataset = pd.read_excel('dataset/s_airfryer.xlsx')
    elif (product == 'Air Purifier'):
        dataset = pd.read_excel('dataset/s_airpurifier.xlsx')
    elif (product == 'Chair'):
        dataset = pd.read_excel('dataset/s_chair.xlsx')
    elif (product == 'Kettle'):
        dataset = pd.read_excel('dataset/s_kettle.xlsx')
    elif (product == 'Lamp'):
        dataset = pd.read_excel('dataset/s_lamp.xlsx')
    else:
        dataset = pd.read_excel('dataset/s_plate.xlsx')

    return product, dataset


def font_color(text):
    yol = "HTML/text_colour.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', text)
    st.markdown(contents, unsafe_allow_html=True)

def freq_words(x, terms=20):
    all_words = ' '.join([str(text) for text in x])
    all_words = all_words.split()

    fdist = FreqDist(all_words)
    words_df = pd.DataFrame({'word': list(fdist.keys()), 'count': list(fdist.values())})

    # selecting top 20 most frequent words
    d = words_df.nlargest(columns="count", n=terms)
    fig = plt.figure(figsize=(15, 8))
    sns.barplot(data=d, x="word", y="count")
    st.pyplot(fig)



def get_neg_keyword(product):
    if (product == 'Air Fryer'):
        dataset = pd.read_excel('word/af.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])

    elif (product == 'Air Purifier'):
        dataset = pd.read_excel('word/ap.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])

    elif (product == 'Chair'):
        dataset = pd.read_excel('word/c.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])

    elif (product == 'Kettle'):
        dataset = pd.read_excel('word/k.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])

    elif (product == 'Lamp'):
        dataset = pd.read_excel('word/l.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])

    else:
        dataset = pd.read_excel('word/p.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])
        # selecting rows based on condition
    neg1 = dataframe[(dataframe['topic'] == 1) & (dataframe['sentiment'] == 'negative')]
    neg2 = dataframe[(dataframe['topic'] == 2) & (dataframe['sentiment'] == 'negative')]

    return neg1, neg2

def get_pos_keyword(product):
    if (product == 'Air Fryer'):
        dataset = pd.read_excel('word/af.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])
        pos_num =0
        neg_num =1

    elif (product == 'Air Purifier'):
        dataset = pd.read_excel('word/ap.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])
        pos_num = 2
        neg_num = 3

    elif (product == 'Chair'):
        dataset = pd.read_excel('word/c.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])
        pos_num = 4
        neg_num = 5

    elif (product == 'Kettle'):
        dataset = pd.read_excel('word/k.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])
        pos_num = 6
        neg_num = 7
    elif (product == 'Lamp'):
        dataset = pd.read_excel('word/l.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])
        pos_num = 8
        neg_num = 9

    else:
        dataset = pd.read_excel('word/p.xlsx')
        dataframe = pd.DataFrame(dataset, columns=['word', 'weight', 'topic', 'sentiment'])
        pos_num = 10
        neg_num = 11

    # selecting rows based on condition
    pos1 = dataframe[(dataframe['topic'] == 1) & (dataframe['sentiment'] == 'positive')]
    pos2 = dataframe[(dataframe['topic'] == 2) & (dataframe['sentiment'] == 'positive')]

    dataset_topics = pd.read_excel('topic/topic.xlsx')
    df_topic = pd.DataFrame(dataset_topics, columns=['product', 'topic1', 'topic2', 'sentiment'])
    pos_topic1 = df_topic['topic1'][pos_num]
    pos_topic2 = df_topic['topic2'][pos_num]
    neg_topic1 = df_topic['topic1'][neg_num]
    neg_topic2 = df_topic['topic2'][neg_num]

    return pos1, pos2, pos_topic1, pos_topic2, neg_topic1, neg_topic2


show_dashboard()
