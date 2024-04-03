import streamlit as st
import pickle
import requests
# def recommend(movie):
#     movie_index = movies_list[movies_list['title'] == movie].index[0]
#     distances = similarity[movie_index] # Assuming similarity is correctly defined elsewhere
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
#     recommended_movies = []
#     for i in movies_list:
#         recommended_movies.append(movies_list.iloc[i[0]].title)
#     return recommended_movies

# st.title('Movie Recommender System')

# movies_list = pickle.load(open('movies.pkl','rb' ))
# movies_list = movies_list['title'].values

# similarity = pickle.load(open('similarity.pkl','rb' ))

# selected_movie_name = st.selectbox(
#     'Hyeee ya please select the movie in the dropdown below',
#     movies_list)

# # st.write('You selected:', selected_movie_name)


# if st.button('Recommend'):
#     recommandation = recommend(selected_movie_name)
#     for i in recommandation:
#        st.write(i)

# def fetch_poster(movie_id):
#     requests.get()

def recommend(movie, movies_list):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index] # Assuming similarity is correctly defined elsewhere
    movies_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_sorted:
        recommended_movies.append(movies_list.iloc[i[0]]['title'])
        movie_id = i[0]
        # fetch poster from api
    return recommended_movies

st.title('Movie Recommender System')

movies_list = pickle.load(open('movies.pkl','rb'))
# Assuming 'movies.pkl' contains the DataFrame directly

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
    'Select a movie from the dropdown below',
    movies_list['title'].values)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name, movies_list)
    for movie in recommendation:
        st.write(movie)
