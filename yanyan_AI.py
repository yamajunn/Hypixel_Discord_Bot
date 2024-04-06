import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

from yanyan_GetCheater import get_cheater
def judgment_cheater(name):
    model = joblib.load('models/Cheater.pkl')
    X = ['networkExp', 'bedwars_level', 'Experience', 'beds_broken_bedwars', 'beds_lost_bedwars', 'coins', 'deaths_bedwars', 'diamond_resources_collected_bedwars', 'emerald_resources_collected_bedwars', 'final_deaths_bedwars', 'final_kills_bedwars', 'games_played_bedwars', 'games_played_bedwars_1', 'kills_bedwars', 'losses_bedwars', 'void_final_deaths_bedwars',  'wins_bedwars','fkdr','wlr','bblr','fk_lev','bb_lev','kill_lev']
    columns_ = ['karma', 'networkExp', 'bedwars_beds', 'bedwars_bedwars_challenger',
        'bedwars_bedwars_killer', 'bedwars_collectors_edition', 'bedwars_level',
        'bedwars_loot_box', 'bedwars_slumber_ticket_master', 'bedwars_wins',
        'challenges', 'all_timeBEDWARS__defensive', 'BEDWARS__offensive',
        'BEDWARS__support', 'Bedwars_openedChests', 'Experience',
        '_items_purchased_bedwars', 'beds_broken_bedwars', 'beds_lost_bedwars',
        'coins', 'deaths_bedwars', 'diamond_resources_collected_bedwars',
        'emerald_resources_collected_bedwars', 'fall_deaths_bedwars',
        'fall_final_deaths_bedwars', 'fall_final_kills_bedwars',
        'fall_kills_bedwars', 'final_deaths_bedwars', 'final_kills_bedwars',
        'games_played_bedwars', 'games_played_bedwars_1', 'kills_bedwars',
        'losses_bedwars', 'void_deaths_bedwars', 'void_final_deaths_bedwars',
        'void_final_kills_bedwars', 'void_kills_bedwars', 'wins_bedwars',
        'fkdr', 'wlr', 'bblr', 'fk_lev', 'bb_lev', 'kill_lev']
    # data = [[76995.0,987634.0,64.0,0.0,177.0,38.0,7.0,5.0,0.0,21.0,0.0,0.0,17.0,8.0,11.0,25853.0,2343.0,63.0,96.0,22412.0,400.0,295.0,219.0,5.0,2.0,2.0,4.0,106.0,91.0,153.0,154.0,246.0,125.0,195.0,14.0,31.0,102.0,21.0,0,0.8584905660377359,0.168,0.65625,13.0,35.142857142857146,9.0]]
    data = get_cheater(name)

    select_bool = []
    for i, column in enumerate(columns_):
        if column in X:
            select_bool.append(True)
        else:
            select_bool.append(False)
    
    data2 = []
    for i, item in enumerate(data[0]):
        if select_bool[i]:
            data2.append(item)

    scaler = joblib.load('models/scaler/scaler.joblib')

    X_test_scaled = pd.DataFrame([data2], columns=X)
    X_test_scaled2 = scaler.transform(X_test_scaled)

    y_pred = model.predict_proba(X_test_scaled2)

    return y_pred[0][0]

# print(judgment_cheater("Gokiton"))