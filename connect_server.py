import streamlit as st
from the_model import generate_prp  # The Python script to interact with FCEA2.exe

# Streamlit Web App
st.title("Fuel Property Input for .prp File Generation")

# Collect user inputs
fuel_type = st.text_input("Enter fuel type")
density = st.number_input("Enter density (kg/m³)")
specific_heat = st.number_input("Enter specific heat (J/kg.K)")

# Button to trigger PRP generation
if st.button("Generate .prp file"):
    prp_file = generate_prp(fuel_type, density, specific_heat)
    if prp_file:
        with open(prp_file, "rb") as file:
            st.download_button(label="Download .prp file", data=file, file_name=prp_file)
    else:
        st.error("Failed to generate .prp file")
