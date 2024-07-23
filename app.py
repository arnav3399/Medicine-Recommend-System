import streamlit as st
import pickle
import pandas as pd
import subprocess
                                        
with open('css/style.css') as f:
     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)




                                        

                    
medicines_dict = pickle.load(open('medicine_dict.pkl','rb'))
medicines = pd.DataFrame(medicines_dict)

                    
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(medicine):
     medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
     distances = similarity[medicine_index]
     medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_medicines = []
     for i in medicines_list:
         recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
     return recommended_medicines






                              
st.title('Medicine Recommender System')

                                      
selected_medicine_name = st.selectbox(
'Type your medicine name whose alternative is to be recommended',
     medicines['Drug_Name'].values)


                              
if st.button('Recommend Medicine'):
     recommendations = recommend(selected_medicine_name)
     j=1
     for i in recommendations:
          st.write(j,i)                     
          st.write("Click here -> "+" https://pharmeasy.in/search/all?name="+i) 
          j+=1



                                        
from PIL import Image
image = Image.open('images/photo.png')
st.image(image, caption='Recommended Medicines')



