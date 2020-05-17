import requests
import os
'''
Function to request jsons data from playtype.
User must specify what type of playtype, and which season year. Optional 
parameter to see stats by player or team is available.
:param: PlayType, str
Expected inputs to PlayType on the left hand side of the colon, 
with the corresponding playtype name on the right hand side 
    'iso':'Isolation', 
    'tr':'Transition', 
    'prb':'Pick & Roll Ball Handler', 
    'prr':'Pick & Roll Roll Man',
    'pu':'Post Up',
    'su': 'Spot uUp', 
    'ho':'Handoff',
    'cut':'Cut', 
    'os':'Off Screen', 
    'putback':'Putbacks', 
    'misc':'Misc'
:param: SeasonYear, str
Expected inputs to SeasonYear on the left hand side of the colon:
    '2019':'2019-20',
    '2018':'2018-19',
    '2017':'2017-18', 
    '2016':'2016-17',
    '2015':'2015-16'
:param: PlayerOrTeam, str
Expected inputs:
    'P': 'Player'
    'T': 'Team'
'''
playtype_shortcut = {'iso':'Isolation', 'tr':'Transition', 'prb':'PRBallHandler', 'prr':'PRRollMan','pu':'Postup','su': 'Spotup', 'ho':'Handoff','cut':'Cut', 'os':'Offscreen', 'putback':'OffRebound', 'misc':'Misc'}
seasonyear_shortcut = {'2019':'2019-20', '2018':'2018-19','2017':'2017-18', '2016':'2016-17','2015':'2015-16'}

def pull_nba(PlayType, SeasonYear,PlayerOrTeam='P',outdir="data/all_jsons1/"):
    '''
    function that extracts playtype data into json file.
    must specify playtype, season year. can specify data based by players or by team.
    '''
    
    pt = playtype_shortcut[PlayType]
    sy = seasonyear_shortcut[SeasonYear]

    stats_headers={ 'Host': 'stats.nba.com', 'User-Agent': 'Firefox/55.0', 'Accept': 'application/json text/plain, */*', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Referer': 'https://stats.nba.com/', 'x-nba-stats-origin': 'stats', 'x-nba-stats-token': 'true', 'DNT': '1', }
    request_str = 'https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=PerGame&PlayType=' + pt + '&PlayerOrTeam=' + PlayerOrTeam + '&SeasonType=Regular+Season&SeasonYear=' + sy + '&TypeGrouping=offensive'
    response = requests.get(request_str, headers= stats_headers)

    wb_filename = outdir+'leaguedash_' + PlayType + '_' + SeasonYear + '_' + PlayerOrTeam + '.json'
    with open(wb_filename, 'wb') as f:
        f.write(response.content)