import streamlit as st
import pandas as pd
import os
import pickle 
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler 

# Company image
st.image("https://upload.wikimedia.org/wikipedia/commons/0/0f/Corporaci%C3%B3n_Favorita_Logo.png?20161217003545")

st.write("""# Corporation Favorita Grocery """)

# Write a subheader
st.subheader("Enter your records")

# Load ml components from file
cwd = os.getcwd()
relative_path = "streamlit_project\\ml.pkl"

absolute_path = os.path.join(cwd, relative_path)
print(absolute_path)

# Reading Machine learning component file
with open(absolute_path, "rb") as f:
    ml_components = pickle.load(f)

pip = ml_components["pipline"]
scaler = pip["scaler"]
model = pip["regressor"]
      
# Preparing records to be choosen for family
family_choose = ["AUTOMOTIVE", "BABY CARE" , "BEAUTY" , "BEVERAGES" , "BOOKS" , "BREAD/BAKERY ", 
                 "CELEBRATION" , "CLEANING" , "DAIRY", "DELI" , "EGGS" , "FROZEN FOODS" , "GROCERY I" ,
                 "GROCERY II" , "HARDWARE"  , "HOME AND KITCHEN I" , "HOME AND KITCHEN II ",
                 "HOME APPLIANCES" , "HOME CARE" , "LADIESWEAR" , "LAWN AND GARDEN" , "LINGERIE" ,
                 "LIQUOR-WINE-BEER" , "MAGAZINES" ,"MEATS" , "PERSONAL CARE" , "PET SUPPLIES" ,
                 "PLAYERS AND ELECTRONICS" , "POULTRY" , "PREPARED FOODS ", "PRODUCE" ,
                 "SCHOOL AND OFFICE SUPPLIES ", "SEAFOOD" ]

# Accepting input
store_nbr = st.slider("Select an Store number", min_value=1, max_value=54, value=10, step=1)
family = st.selectbox("family", family_choose , key = "fam" )

onpromotion = st.number_input("onpromotion" , key = "pro" )
date = st.date_input("Select date", )


backgroundColor = "green"
with st.form(key = "my_form", clear_on_submit=True):
            
    # For presenting output
    submitted = st.form_submit_button("Predict")
    if submitted:
                
        try:
            
            inputs = [
                        ["store_nbr" , "family", "onpromotion", "date"], 
                    
                        [ store_nbr , family, onpromotion, date ], 
                        
                    ]
            
            df = pd.DataFrame(inputs[1:], columns=inputs[0])
            
            df = df.set_index("date") # make the date as index 
                   
            df = df[["store_nbr" , "onpromotion"]] # secting exogenous variables
            print(df)
            
            # Predicting values
            predicted = pip.predict(df)
            df["sales"] = predicted

            st.balloons()
            st.success('Successfully predicted!', icon="✅")
            print(df) 
            
            st.write(predicted)
            st.write(df)
            
        except:
            st.error('Something wrong happen....', icon="🚨")
        