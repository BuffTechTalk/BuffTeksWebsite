import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import sqlite3
from datetime import datetime
from folium.features import CustomIcon


def testing():
    st.title("Testing Page")
    # Initialize the database
    conn = sqlite3.connect('student_locations.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                state TEXT,
                country TEXT,
                latitude REAL,
                longitude REAL,
                timestamp DATETIME)''')
    conn.commit()


    st.title('Where are Members From')

    # Input form for student location
    with st.form("student_form"):
        input_city = st.text_input("Enter your City, State (e.g.: Amarillo,TX), or City, Country (Toronto, Canada):")

        submitted = st.form_submit_button("Submit")
        
        if submitted:
            lat, lon, city, state, country = get_location(input_city)
            if lat and lon:
                save_student(conn, city, state, country, lat, lon)
                st.success(f"Location saved: {city}, {country}")
            else:
                st.error("Unable to find the location. Please try a different city name.")

        # Display all students on a map
        st.subheader('All Student Locations')
        df = get_all_students(conn)
        if not df.empty:
            m = create_map(df)
            folium_static(m)
        else:
            st.write("No student data available yet.")

        # Display student statistics
        st.subheader('Student Statistics')
        if not df.empty:
            st.write(f"Total students: {len(df)}")
            st.write(f"Total cities: {df['city'].nunique()}")
            st.write(f"Total countries: {df['country'].nunique()}")
            st.write("Top 5 cities:")
            st.write(df['city'].value_counts().head())
            st.write("Top 5 countries:")
            st.write(df['country'].value_counts().head())
        else:
            st.write("No student data available yet.")

        # Close the database connection
        conn.close()



def get_location(city):
    geolocator = Nominatim(user_agent="student_location_app")
    try:
        location = geolocator.geocode(city, language="en")
        st.write(location)
        if location:
            location_str = str(location).split(",")
            state, country = location_str[2], location_str[-1]
            return location.latitude, location.longitude, location.raw.get('name'), state, country
        else:
            return None, None, None, None, None
    except Exception as e:
        st.write(e)
        return None, None, None, None, None


def save_student(conn, city, state, country, lat, lon):
    c = conn.cursor()
    timestamp = datetime.now()
    c.execute("INSERT INTO students (city, state, country, latitude, longitude, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
              (city, state, country, lat, lon, timestamp))
    conn.commit()

def get_all_students(conn):
    df = pd.read_sql_query("SELECT * from students", conn)
    return df

def create_map(df):
    m = folium.Map(location=[41.2706, -97.1749], zoom_start=4)

    # Group by city and count occurrences
    city_counts = df.groupby(['city', 'state', 'latitude', 'longitude', 'country']).size().reset_index(name='count')
    
    # Normalize marker sizes
    max_count = city_counts['count'].max()
    min_size, max_size = 5, 20  # min and max marker sizes
    
    for _, row in city_counts.iterrows():
        # Create a custom icon
        icon = CustomIcon(
            icon_image='./images/BuffaloMarker.png',  # Replace with the path to your icon file
            icon_size=(30, 30),  # Adjust the size as needed
            icon_anchor=(15, 30),  # Adjust anchor point if needed
            popup_anchor=(0, -30)  # Adjust popup anchor if needed
        )
        
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"{row['city']} <br> {row['count']}",
            tooltip=f"{row['city']}, {row['country']}",
            icon=icon
        ).add_to(m)
    
    return m
