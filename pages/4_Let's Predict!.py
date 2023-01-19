import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import cleantext
import nltk
nltk.download('stopwords')
import pickle
import sklearn
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

st.set_page_config(
    page_title="Senzer🧐",
)
def show_model():
    yol = "HTML/container_background.html"
    f = open(yol, 'r')
    contents = f.read()
    f.close()
    contents = contents.replace('smth', 'Prediction Model')
    st.markdown(contents, unsafe_allow_html=True)
    st.write("""*Choose one of the product category before you enter your review!*""")

    st.subheader("1. Choose the product you want to comment.")
    product_data,product = choose_data()

    st.subheader("2. Enter your comment.")
    comment = str(get_clean_comment())
    tfidf = get_vectorizer(product)
    vec = tfidf.transform([comment])
    modelSVM = choose_model(product)

    st.subheader("Result")
    prediction(vec,modelSVM)

def prediction(vec, model):
    pred_svm = model.predict(vec)
    st.write(pos_neg(pred_svm))

def pos_neg(pred):
  if(pred == 0):
    sentiment = 'The customer feels :red[Negative]!＞﹏＜'
  else:
    sentiment = 'The customer feels :green[Positive](❁´◡`❁)!'
  return sentiment



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

    return dataset,product


def get_clean_comment():
    if "review" not in st.session_state:
       st.session_state["review"] = ""

    review = st.text_input("Input a text here")
    submit = st.button("Enter")
    if submit:
        review = cleantext.clean(review)
        extra_stopwords = ['air', 'fryer','chair','chairs','kettle','kettles','plate','plates','corelle','Corelle','light','lamp','lamps','purifier','purifiers','airpurifier']
        review = list(review.split(" "))
        filtered_word = [word for word in review if word not in extra_stopwords]
    return review

def choose_model(product):
    if (product == 'Air Fryer'):
        modelSVM = pickle.load(open('model/af_svm.sav','rb'))
    elif (product == 'Air Purifier'):
        modelSVM = pickle.load(open('model/ap_svm.sav', 'rb'))
    elif (product == 'Chair'):
        modelSVM = pickle.load(open('model/c_svm.sav', 'rb'))
    elif (product == 'Kettle'):
        modelSVM = pickle.load(open('model/k_svm.sav', 'rb'))
    elif (product == 'Lamp'):
        modelSVM = pickle.load(open('model/l_svm.sav', 'rb'))
    else:
        modelSVM = pickle.load(open('model/p_svm.sav','rb'))

    return modelSVM

def get_vectorizer(product):
    if (product == 'Air Fryer'):
        vectorizer = pickle.load(open("vectorizer/af_vectorizer.pickle", 'rb'))
    elif (product == 'Air Purifier'):
        vectorizer = pickle.load(open("vectorizer/ap_vectorizer.pickle", 'rb'))
    elif (product == 'Chair'):
        vectorizer = pickle.load(open("vectorizer/c_vectorizer.pickle", 'rb'))
    elif (product == 'Kettle'):
        vectorizer = pickle.load(open("vectorizer/k_vectorizer.pickle", 'rb'))
    elif (product == 'Lamp'):
        vectorizer = pickle.load(open("vectorizer/l_vectorizer.pickle", 'rb'))
    else:
        vectorizer = pickle.load(open("vectorizer/p_vectorizer.pickle", 'rb'))

    return vectorizer

show_model()
