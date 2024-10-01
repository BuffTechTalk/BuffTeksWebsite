import pandas as pd
import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
import sqlite3
from datetime import datetime

from webpages import code_editor as ce


# def get_ip():
#     try:
#         response = requests.get('https://api.ipify.org')
#         return response.text
#     except:
#         return "Unable to get IP"

# def get_location(ip_address):
#     try:
#         response = requests.get(f'https://ipapi.co/{ip_address}/json/')
#         data = response.json()
#         return data['latitude'], data['longitude'], data['city'], data['country_name']
#     except:
#         return None, None, "Unknown", "Unknown"

# def save_visitor(conn, lat, lon, city, country):
#     timestamp = datetime.now()
#     c = conn.cursor()
#     c.execute("INSERT INTO visitors (latitude, longitude, city, country, timestamp) VALUES (?, ?, ?, ?, ?)",
#             (lat, lon, city, country, timestamp))
#     conn.commit()

# def get_all_visitors(conn):
#     df = pd.read_sql_query("SELECT * from visitors", conn)
#     return df



# def create_map(df):
#     m = folium.Map(location=[41.2706, -97.1749], zoom_start=4)
#     # Create a custom icon

#     for _, row in df.iterrows():
#         folium.Marker(
#             location = [row['latitude'], row['longitude']],
#             popup=f"{row['city']}",
#             tooltip=f"{row['city']}"
#         ).add_to(m)
#     return m
import psutil

def get_connected_ips():
    connections = psutil.net_connections()
    ips = []
    for conn in connections:
        if conn.status == psutil.CONN_ESTABLISHED:
            ips.append(conn.raddr.ip)
    return ips



def testing():
    st.title("Testing Page")
    st.write(get_connected_ips())


    # ce.code_editor()
    
    # # # [Work]code for instering youtube videos
    # # video = "https://youtu.be/HluANRwPyNo?feature=shared"
    # # st.video(video)


    # Initialize the database
    # conn = sqlite3.connect('./files/visitor_locations.db')
    # c = conn.cursor()
    # c.execute('''CREATE TABLE IF NOT EXISTS visitors
    #             (id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             latitude REAL,
    #             longitude REAL,
    #             city TEXT,
    #             country TEXT,
    #             timestamp DATETIME)''')
    # conn.commit()



    # st.title('Visitor Location Tracker')

    # # Get and save current visitor's location
    # ip = get_ip()
    # lat, lon, city, country = get_location(ip)
    # if lat and lon:
    #     save_visitor(conn, lat, lon, city, country)
    #     st.write(f"Your location: {city}, {country}")
    # else:
    #     st.write("Unable to determine your location")

    # # Display all visitors on a map
    # st.subheader('All Visitor Locations')
    # df = get_all_visitors(conn)
    # if not df.empty:
    #     m = create_map(df)
    #     folium_static(m)
    # else:
    #     st.write("No visitor data available yet.")

    # # Display visitor statistics
    # st.subheader('Visitor Statistics')
    # col_visitors, col_cities, col_countries = st.columns(3)
    # if not df.empty:
    #     with col_visitors:
    #         st.metric(label="Total visitors", value= df['id'].nunique())
    #     with col_cities:
    #         st.metric(label="Total cities", value= df['city'].nunique())
    #     with col_countries:
    #         st.metric(label="Total countries", value= df['country'].nunique())
    #     st.write("Top 5 cities:")
    #     st.write(df['city'].value_counts().head())
    # else:
    #     st.write("No visitor data available yet.")

    # # Close the database connection
    # conn.close()