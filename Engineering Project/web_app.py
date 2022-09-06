import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import pickle

#global variables
#engine = create_engine('sqlite:///League of Legends.db')
#data = pd.DataFrame(pd.read_sql_query('''SELECT * FROM jp_matches''',engine))
dbfile = open('match.pkl','rb')
data = pickle.load(dbfile)
tiers = {'Iron+':['IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','MASTER','GRANDMASTER','CHALLENGER'],
        'Bronze+':['BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','MASTER','GRANDMASTER','CHALLENGER'],
        'Silver+':['SILVER','GOLD','PLATINUM','DIAMOND','MASTER','GRANDMASTER','CHALLENGER'],
        'Gold+':['GOLD','PLATINUM','DIAMOND','MASTER','GRANDMASTER','CHALLENGER'],
        'Platinum+':['PLATINUM','DIAMOND','MASTER','GRANDMASTER','CHALLENGER'],
        'Diamond+':['DIAMOND','MASTER','GRANDMASTER','CHALLENGER'],
        'Master+':['MASTER','GRANDMASTER','CHALLENGER'],
        'Grandmaster+':['GRANDMASTER','CHALLENGER'],
        'Challenger':['CHALLENGER']}

st.markdown(
    '''
    <style>
    body {
        background-image: url("https://lolstatic-a.akamaihd.net/frontpage/apps/prod/rg-league-display-2017/en_US/cb24025fade09e3f965776440dffcc65024d3266/assets/img/content/splash/content-original-championillustrations-group-slashes.jpg");
        background-size: cover;
        opacity: 0.9;
    }
    </style>
    ''', 
    unsafe_allow_html=True
)

#playrate section
st.write(
    '''
    ## League of Legend Champion Playrate
    Champion playrates in ranked games on the Japanese server
    '''
)
champion_name = st.selectbox("What champion's playrate would you like to check?",options = data.champion.sort_values().unique())
start_tier = st.select_slider('Select ranks to filter by',
    options = ['Iron+','Bronze+','Silver+','Gold+','Platinum+','Diamond+','Master+','Grandmaster+','Challenger'])
mask = ((data['tier'].isin(tiers.get(start_tier))) & (data['champion']==champion_name))
number_of_games = len(data[data['tier'].isin(tiers.get(start_tier))])
playrate = round(len(data[mask])/number_of_games,3)
st.write(
    f'Playrate of {champion_name} at {start_tier} is {playrate}% of {number_of_games} games'
)