import streamlit as st
import requests
import pandas as pd

# Set page title and description using Markdown
st.title("People in Space and ISS Location")
st.markdown("This app displays the total number of people in space along with their names and the current location of the International Space Station (ISS).")

# Make a GET request to the API endpoint to get information about people in space
response_people = requests.get("http://api.open-notify.org/astros.json")

# Check if the request was successful
if response_people.status_code == 200:
    # Parse the JSON response into a Python dictionary
    data_people = response_people.json()
    
    # Extract the total number of people in space
    total_people = data_people["number"]
    
    # Extract the list of astronauts
    astronauts = data_people["people"]
    
    # Display the total number of people in space
    st.write(f"Total number of people in space: {total_people}")
    
    # Display the names of the astronauts
    st.write("Names of people in space:")
    for astronaut in astronauts:
        st.write("- " + astronaut["name"])
else:
    st.error("Error: Failed to fetch data about people in space.")

# Make a GET request to the API endpoint to get the current location of the ISS
response_iss = requests.get("http://api.open-notify.org/iss-now.json")

# Check if the request was successful
if response_iss.status_code == 200:
    # Parse the JSON response into a Python dictionary
    data_iss = response_iss.json()
    
    # Extract the current latitude and longitude of the ISS
    iss_location = {
        "LAT": [float(data_iss["iss_position"]["latitude"])],
        "LON": [float(data_iss["iss_position"]["longitude"])]
    }
    
    # Create a DataFrame with the ISS location data
    df_iss_location = pd.DataFrame(iss_location)
    
    # Display a short description for the map
    st.write("Current location of the International Space Station (ISS):")
    
    # Display the map with the current ISS location
    st.map(df_iss_location, zoom=3)
else:
    st.error("Error: Failed to fetch data about the ISS location.")
