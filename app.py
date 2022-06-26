from sqlite3 import OperationalError
from turtle import width
import streamlit as st
from streamlit import caching
import pandas as pd
from streamlit_option_menu import option_menu

st.markdown("<h1 style='text-align: center;'>Students Record </h1>",
            unsafe_allow_html=True)

df = pd.read_csv("student.csv")
df.index = df.index + 1

if"button_clicked" not in st.session_state:
    st.session_state.button_clicked = False


def callback():
    st.session_state.button_clicked = True

col1, col2, col3 = st.columns([2,3,4])
with col1:
    st.write("")
with col2:
    df = df.astype(str)
    st.table(df)
with col3:
    st.write("")


selected = option_menu(
    menu_title=None,
    options=["Add New", "Delete", "Update", "Refresh"],
    orientation="horizontal"
)


if selected == "Add New":
    options_form = st.form("Form")
    Student_Id = (options_form.text_input("Enter Student Id"))
    First_Name = options_form.text_input("First Name")
    Last_Name = options_form.text_input("Last Name")
    Address = options_form.text_input("Address")
    program = options_form.text_input("Program")
    Marital_Status = options_form.text_input("Marital Status")
    Country = options_form.text_input("Country")
    Add = options_form.form_submit_button("Add Student Record")
    if Add:
        df = df.append({'Student_Id': Student_Id, 'First_Name': First_Name, 'Last_Name': Last_Name, 'Program': program,
                       'Marital Status': Marital_Status, 'Country': Country, 'Address': Address}, ignore_index=True)
        df.to_csv("student.csv", index=False)


if selected == "Delete":
    options_form = st.form("Form")
    Id = options_form.text_input("Enter Student Id to delete record")
    Del = options_form.form_submit_button("Delete Student Record")
    if Del:
        df = df.drop(df[df.Student_Id == Id].index)
        df.to_csv("student.csv", index=False)

if selected == "Update":
    options_form = st.form("Form")
    Id = options_form.text_input("Enter Student Id to update record")
    First_Name = options_form.text_input("First Name")
    Last_Name = options_form.text_input("Last Name")
    address = options_form.text_input("Address")
    program = options_form.text_input("Program")
    Marital_Status = options_form.text_input("Marital Status")
    Country = options_form.text_input("Country")
    Update_data = options_form.form_submit_button("Update Student Record")
    if Update_data:
        df.loc[df['Student_Id'] == Id, 'First_Name'] = First_Name
        df.loc[df['Student_Id'] == Id, 'Last_Name'] = Last_Name
        df.loc[df['Student_Id'] == Id, 'Address'] = address
        df.loc[df['Student_Id'] == Id, 'Program'] = program
        df.loc[df['Student_Id'] == Id, 'Marital Status'] = Marital_Status
        df.loc[df['Student_Id'] == Id, 'Country'] = Country
        df.to_csv("student.csv", index=False)

if selected == "Refresh":
    st.balloons()
