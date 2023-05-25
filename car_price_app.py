import streamlit as st
import pandas as pd
from sklearn import *
import pickle

# Load the saved model
model = pickle.load(open('rf_model.pkl', 'rb'))

# Load the dataframe
df = pd.read_excel("CAR DETAILS.xlsx")

def main():
    # Add a title to the app
    st.title("Car Price Prediction App")

    # Create input fields for user input
    Car_name = st.selectbox('Car Name', df['car_name'].unique())
    Year = st.selectbox('Year', df['year'].unique())
    Km_driven = st.text_input('Kilometers Driven')
    Fuel = st.selectbox('Fuel', df['fuel'].unique())
    Seller_type = st.selectbox('Seller Type', df['seller_type'].unique())
    Transmission = st.selectbox('Transmission', df['transmission'].unique())
    Owner = st.selectbox('Owner', df['owner'].unique())
    

    if st.button('Predict Car Price'):
        # Perform prediction using the loaded model
        pred = model.predict([[Car_name,Year, Km_driven, Fuel, Seller_type, Transmission, Owner]])
        output = round(pred[0], 2)
        if output < 0:  # Handling negative outputs
            st.error('The input values may be irrelevant. Please try again by providing relevant information.')
        else:
            write = str(output)
            st.success('You can sell your car for {}'.format(write))

if __name__ == '__main__':
    main()
