# import streamlit as st
# st.title("welcome to my application")
# st.write ("i am paragraph ")
# st.header("Heading")

# st.text_input("Enter your name")
# st.markdown("<h1 style = 'color:red'> welcome to my application</h1>",unsafe_allow_html=True) 
import streamlit as st
import pandas as pd


st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

   
else:
    st.write("Waiting on file upload...")