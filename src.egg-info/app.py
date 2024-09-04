import pickle
import streamlit as st
import requests

def fetch_poster(id):
    url='https://api.themoviedb.org/3/movie/{}?api_key=831743db12db442d510800dfa5914809'.format(id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path=' https://image.tmdb.org/t/p/original'+poster_path

    return full_path


def recommend_movie(movie):
    index= movies[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similarity_vector[index])),reverse=True, key=lambda x: x[1])
    titles=[]
    ids=[]
    for i in distances[1:6]:
        titles.append(movies.iloc[i[0]].title)
        ids.append(fetch_poster(movies.iloc[i[0]].id))

    return titles,ids

st.header('Movie Recommendation Engine')
movies=pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity_vector=pickle.load(open('artifacts/similarity_scores.pkl','rb'))

movies_list=movies['title'].values

selected_movie= st.selectbox(
    'Type your movie for similar movies recommendation', movies_list
)



if st.button('Show Recommendations'):

    rec_titles, rec_img= recommend_movie(selected_movie)
    col1,col2,col3,col4,col5= st.columns(5)

    with col1:
        st.text(rec_titles[0])
        st.image(rec_img[0])

    with col2:
        st.text(rec_titles[1])
        st.image(rec_img[1])

    with col3:
        st.text(rec_titles[2])
        st.image(rec_img[2])

    with col4:
        st.text(rec_titles[3])
        st.image(rec_img[3])

    with col5:
        st.text(rec_titles[4])
        st.image(rec_img[4])



