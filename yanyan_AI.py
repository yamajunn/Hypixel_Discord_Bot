import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

from yanyan_GetCheater import get_cheater
def judgment_cheater(name):
    model = joblib.load('models/Cheater.pkl')
    X = ['karma', 'networkExp', 'bedwars_beds', 'bedwars_bedwars_challenger',
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
    data = get_cheater(name)[0]

    select_bool = []
    for i, column in enumerate(columns_):
        if column in X:
            select_bool.append(True)
        else:
            select_bool.append(False)
    
    select_data = []

    for i, item in enumerate(data):
        if select_bool[i]:
            select_data.append(item)
    # print(select_data)

    # scaler = joblib.load('models/scaler.joblib')

    X_test = pd.DataFrame([select_data], columns=X)
    # print(X_test)
    # X_test_scaled = scaler.transform(X_test)

    # Cheatカラムを削除して、各レコードの合計を計算する
    row_sums = X_test.sum(axis=1)

    # 10,000をその行の合計値で割った値を計算して保持する
    divisors = 1000 / row_sums

    # それぞれの行に対して計算した値を掛ける
    X_test_scaled = X_test.mul(divisors, axis=0)

    
    y_pred = model.predict_proba(X_test_scaled)

    return y_pred[0][0]

# print(judgment_cheater("resoligusokazioa"))