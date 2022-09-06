from riotwatcher import LolWatcher, ApiError #https://riot-watcher.readthedocs.io/en/latest/riotwatcher/LeagueOfLegends/index.html
import pandas as pd
from operator import itemgetter
from sqlalchemy import create_engine
import pickle

#global variables
api_key=''
watcher = LolWatcher(api_key)
rank = ['Iron','Bronze','Silver','Gold','Platinum','Diamond','Master','Grandmaster','Challenger']
region = ['North America','Korea','Europe West','Europe Nordic & East','Oceania','Japan','Brazil','Latin America S','Latin America N','Russia','Turkiye']
match_regions = {'North America':'AMERICAS','Brazil':'AMERICAS','Latin America S':'AMERICAS','Latin America N':'AMERICAS',
                'Korea':'ASIA','Japan':'ASIA',
                'Europe West':'EUROPE','Europe Nordic & East':'EUROPE','Russia':'EUROPE','Turkiye':'EUROPE',
                'Oceania':'SEA'}
regional_server = {'north america':'NA1','korea':'KR','europe west':'EUW1','europe nordic & east':'EUN1','oceania':'OC1','japan':'JP1',
            'brazil':'BR1','latin america s':'LA2','latin america n':'LA1','russia':'RU','turkiye':'TR1'}
latest = watcher.data_dragon.versions_all()[0]
engine = create_engine('sqlite:///League of Legends.db')

#gets player info in rank
def league_crawl(region):
    '''
    obtains all players of 1 region (iron, bronze, silver, gold, platinum, diamond, master, grandmaster, challenger)
    '''
    regions = {'north america':'NA1','korea':'KR','europe west':'EUW1','europe nordic & east':'EUN1','oceania':'OC1','japan':'JP1',
            'brazil':'BR1','latin america s':'LA2','latin america n':'LA1','russia':'RU','turkiye':'TR1'}
    tiers=['IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND']
    divisions=['I','II','III','IV']

    data = []
    for tier in tiers:
        for division in divisions:
            page = 1
            division_response =[]
            while watcher.league.entries(regions.get(region.lower()),'RANKED_SOLO_5x5',tier,division,page)!=[]:
                response = watcher.league.entries(regions.get(region.lower()),'RANKED_SOLO_5x5',tier,division,page)
                page+=1
                division_response.extend(response)
            data.extend(division_response)
    masters=watcher.league.masters_by_queue(regions.get(region.lower()),'RANKED_SOLO_5x5')
    for x in masters['entries']:
        x['tier']=masters['tier']
        x['queueType']=masters['queue']
        x['leagueId']=masters['leagueId']
    data.extend(masters['entries'])
    
    grandmasters=watcher.league.grandmaster_by_queue(regions.get(region.lower()),'RANKED_SOLO_5x5')
    for x in grandmasters['entries']:
        x['tier']=grandmasters['tier']
        x['queueType']=grandmasters['queue']
        x['leagueId']=grandmasters['leagueId']
    data.extend(grandmasters['entries'])
    
    challengers=watcher.league.challenger_by_queue(regions.get(region.lower()),'RANKED_SOLO_5x5')
    for x in challengers['entries']:
        x['tier']=challengers['tier']
        x['queueType']=challengers['queue']
        x['leagueId']=challengers['leagueId']
    data.extend(challengers['entries'])

    return data

#player info dataframes
na_df = pd.DataFrame(league_crawl('north america'))
kr_df = pd.DataFrame(league_crawl('korea'))
euw_df = pd.DataFrame(league_crawl('europe west'))
eun_df = pd.DataFrame(league_crawl('europe nordic & eas'))
oc_df = pd.DataFrame(league_crawl('oceania'))
jp_df = pd.DataFrame(league_crawl('japan'))
br_df = pd.DataFrame(league_crawl('brazil'))
las_df = pd.DataFrame(league_crawl('latin america s'))
lan_df = pd.DataFrame(league_crawl('latin america n'))
ru_df = pd.DataFrame(league_crawl('russia'))
tr_df = pd.DataFrame(league_crawl('turkiye'))


na_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('na_players',engine,if_exists='replace',index=False)
kr_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('kr_players',engine,if_exists='replace',index=False)
euw_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('euw_players',engine,if_exists='replace',index=False)
eun_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('eun_players',engine,if_exists='replace',index=False)
oc_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('oc_players',engine,if_exists='replace',index=False)
jp_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('jp_players',engine,if_exists='replace',index=False)
br_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('br_players',engine,if_exists='replace',index=False)
las_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('las_players',engine,if_exists='replace',index=False)
lan_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('lan_players',engine,if_exists='replace',index=False)
ru_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('ru_players',engine,if_exists='replace',index=False)
tr_df[['leagueId','queueType','tier','rank','summonerId','summonerName','leaguePoints','wins','losses']].to_sql('tr_players',engine,if_exists='replace',index=False)

jp_df = pd.DataFrame(pd.read_sql_query('''SELECT * FROM jp_players''',engine))

#match information
def match_crawl(regions):
    df_to_use = {'Japan':jp_df,'North America':na_df,'Brazil':br_df,'Latin America S':las_df,'Latin America N':lan_df,
                'Korea':kr_df,'Europe West':euw_df,'Europe Nordic & East':eun_df,'Russia':ru_df,'Turkiye':tr_df,'Oceania':oc_df
                }
    data = []
    for index,row in df_to_use[regions].iterrows():
        puuid = (watcher.summoner.by_id(regional_server[regions.lower()],row['summonerId'])['puuid'])
        matches = watcher.match.matchlist_by_puuid(region=match_regions[regions],puuid=puuid,count=3,queue=420,type='ranked')
        for x in matches:
            try:
                indexing = watcher.match.by_id(match_regions[regions],x)['metadata']['participants'].index(puuid)
                champion = watcher.match.by_id(match_regions[regions],x)['info']["participants"][indexing]["championName"]
                champion = watcher.data_dragon.champions(version=latest)['data'][champion]['name']
                match_info=[x,puuid,row['tier'],champion]
                data.append(match_info)
            except:
                continue
    match_df = pd.DataFrame(data,columns=['matchId','puuid','tier','champion'])
    return match_df

#gathering data
jp_match_df = pd.DataFrame(match_crawl('Japan'))
jp_match_df.drop_duplicates(inplace=True)
jp_match_df.to_csv('Japanese Matches.csv', index=False)
pickle.dump(jp_match_df,open('match.pkl','wb'))
jp_match_df.to_sql('jp_matches',engine, if_exists='replace',index=False)