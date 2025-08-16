import streamlit as st
import pickle
import numpy as np

import pandas as pd
pt = pd.read_pickle('Books.pkl')
similarity = pickle.load(open('similarity.pkl','rb'))
books_dict = pickle.load(open('books_dict.pkl','rb'))
books = pd.DataFrame(books_dict)


def recommend(book):
    book_index = np.where(pt.index==book)[0][0]
    distances = similarity[book_index]
    book_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_books=[]
    image_url=[]
    
    
    for i in book_list:
        
        recommended_books.append(pt.index[i[0]])
        temp = books[books['Book-Title']==pt.index[i[0]]].drop_duplicates('Book-Title')
        image_url.append(temp['Image-URL-M'].values[0])
        
     
    return recommended_books,image_url

st.title('Books Recommender System')

selected_book_name=st.selectbox('Select Your Book',pt.index.values)


if st.button('Recommend'):
    names,images=recommend(selected_book_name)
    
    
    
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(images[0])
    
    with col2:
        st.text(names[1])
        st.image(images[1])
        
    with col3:
        st.text(names[2])
        st.image(images[2])
        
    with col4:
        st.text(names[3])
        st.image(images[3])
    
    with col5:
        st.text(names[4])
        st.image(images[4])
        
   

    

