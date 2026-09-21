import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv


st.set_page_config(page_title="AI Travel Agent", page_icon=":airplane:", layout="wide")
st.title("AI Travel Agent itinerary Generator")

st.write("plan you day trip itinerary by entering your city and interests")

load_dotenv()

with st.form("travel_form"):
    city = st.text_input("Enter your city")
    interests = st.text_input("Enter your interests (comma-separated)")

    submitted = st.form_submit_button("Generate Itinerary")

    if submitted:
        planner = TravelPlanner()
        planner.set_city(city)
        planner.set_interests(interests)
        itinerary = planner.create_itinerary()

        st.subheader("Generated Itinerary")
        st.markdown(itinerary)
    else:
        st.write("Please enter your city and interests to generate an itinerary.")

