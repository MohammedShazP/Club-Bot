import streamlit
import langchain_helper
streamlit.title("Clubs & Players Details")

# cuisine = streamlit.sidebar.selectbox("Pick a Cuisine",("Indian","American","Italian","Mexican","Chinese","Arabian"))
# clubs_names = streamlit.sidebar.selectbox("Pick a country",("India","Spain","England"))
clubs_names = streamlit.sidebar.text_input  ("Enter the country name")


if clubs_names :
    response = langchain_helper.generate_restaurant_name_and_items(clubs_names)
    streamlit.header(response["club_name"].strip())
    players_lists = response['players_name'].strip().split(",")
    streamlit.write("**Players Details**")

    for player in players_lists:
        streamlit.write("-",player)