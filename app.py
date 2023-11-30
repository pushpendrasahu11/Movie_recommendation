import streamlit as st
import pickle 
movie_list=pickle.load(open('movies.pkl','rb'))
metrix=pickle.load(open('metrix.pkl','rb'))
hide_streamlit_style = """
<style>
#body {
    background-color:black;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

def recommend(movie):
    movie_index=movie_list[movie_list['title']==movie].index[0]
    distances=metrix[movie_index]
    new_movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in new_movie_list:
        recommended_movies.append(movie_list.iloc[i[0]].title)
    return recommended_movies
    


st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.image('https://cdn-icons-png.flaticon.com/512/3171/3171927.png',width=50,use_column_width=None)
st.title('Movie Recommendation')


selected_movie = st.selectbox(
    'How would you like to be contacted?',
    (movie_list['title']))
if st.button('Recommend'):
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)
   