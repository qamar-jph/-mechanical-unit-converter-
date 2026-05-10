import streamlit as st

st.title("Mechanical Unit Converter")

st.write("Full Name: Qamar Ali")
st.write("Roll Number: 22-ME-101")

option = st.selectbox(
    "Choose",
    ["Meter to CM", "Celsius to Fahrenheit"]
)

value = st.number_input("Enter Value")

if option == "Meter to CM":
    st.success(f"Result = {value * 100} cm")

elif option == "Celsius to Fahrenheit":
    st.success(f"Result = {(value * 9/5) + 32} °F")

st.header("Material Density Checker")

material = st.selectbox(
    "Select Material",
    ["Steel", "Aluminum"]
)

if material == "Steel":
    st.write("Density = 7850 kg/m³")

elif material == "Aluminum":
    st.write("Density = 2700 kg/m³")
