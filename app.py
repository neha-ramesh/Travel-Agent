from dotenv import load_dotenv
import streamlit as st
from datetime import date
from PIL import Image
import cohere
import os

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

st.set_page_config(page_title="Travel Agent App", layout="wide")

st.sidebar.title("Travel Agent Portal")
option = st.sidebar.radio(
    "Explore Options:",
    ["Home", "Plan Your Trip", "Accommodation", "Travel", "Food & Cuisine", "Attractions"]
)

if option == "Home":
    st.title("Welcome to the Travel Agent Portal!")
    st.image("download.jpg", caption="Discover Your Next Adventure!", use_column_width=True)
    st.write("""
        Explore amazing destinations, plan your itinerary, and make memories to last a lifetime. 
        Use the sidebar to navigate through our services.
    """)

elif option == "Plan Your Trip":
    st.title("Plan Your Dream Vacation")
    cities = ["Paris", "New York", "Tokyo", "London", "Dubai", "Sydney"]
    city = st.selectbox("Choose your destination city:", cities)
    st.write("Select your travel dates:")
    start_date = st.date_input("From", date.today())
    end_date = st.date_input("To", date.today())
    people = st.slider("Number of people:", 1, 10, 1)
    search = st.text_input("Search for activities or specific locations:")

    if st.button("Get Recommendations"):
        prompt = (
            f"Plan a trip to {city} from {start_date} to {end_date} for {people} people. "
            f"Highlight major attractions, accommodations, travel tips, and activities. "
            f"Search context: {search}"
        )
        response = co.generate(model="command-light", prompt=prompt, max_tokens=500)
        st.subheader("Trip Recommendations:")
        st.write(response.generations[0].text)

elif option == "Accommodation":
    st.title("Find the Perfect Stay")
    city = st.text_input("Enter the city:")
    check_in = st.date_input("Check-in Date", date.today())
    check_out = st.date_input("Check-out Date", date.today())

    if st.button("Search Accommodations"):
        prompt = (
            f"Find top accommodations in {city} from {check_in} to {check_out} with great reviews and budget options."
        )
        response = co.generate(model="command-light", prompt=prompt, max_tokens=300)
        st.subheader("Recommended Accommodations:")
        st.write(response.generations[0].text)

elif option == "Travel":
    st.title("Plan Your Travel")
    start_location = st.text_input("Starting Location:")
    destination = st.text_input("Destination:")
    travel_date = st.date_input("Travel Date", date.today())

    if st.button("Find Travel Options"):
        prompt = f"Suggest travel options from {start_location} to {destination} on {travel_date}."
        response = co.generate(model="command-light", prompt=prompt, max_tokens=300)
        st.subheader("Travel Options:")
        st.write(response.generations[0].text)

elif option == "Food & Cuisine":
    st.title("Explore Local Delicacies")
    city = st.text_input("Enter the city to explore:")

    if st.button("Find Food Options"):
        prompt = f"Recommend must-try food and cuisine in {city}, including popular restaurants."
        response = co.generate(model="command-light", prompt=prompt, max_tokens=300)
        st.subheader("Food Recommendations:")
        st.write(response.generations[0].text)

elif option == "Attractions":
    st.title("Top Attractions")
    city = st.text_input("Enter the city to explore:")

    if st.button("Discover Attractions"):
        prompt = f"List the top attractions in {city}, including historical, cultural, and modern sites."
        response = co.generate(model="command-light", prompt=prompt, max_tokens=300)
        st.subheader("Top Attractions:")
        st.write(response.generations[0].text)
