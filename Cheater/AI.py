import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

data_path = "./Cheater/Data2.csv"
df = pd.read_csv(data_path)

X = df.drop('Cheat', axis=1)
# X = df[['karma', 'networkExp', 'bedwars_bedwars_killer', 'bedwars_loot_box','BEDWARS__offensive', 'Bedwars_openedChests', 'coins','final_deaths_bedwars', 'losses_bedwars', 'wins_bedwars']]
# X = df[['networkExp', 'bedwars_beds', 'bedwars_level', 'bedwars_wins', 'beds_broken_bedwars', 'beds_lost_bedwars', 'deaths_bedwars', 'diamond_resources_collected_bedwars', 'emerald_resources_collected_bedwars', 'fall_deaths_bedwars', 'final_deaths_bedwars', 'final_kills_bedwars', 'games_played_bedwars', 'games_played_bedwars_1', 'kills_bedwars', 'losses_bedwars', 'void_deaths_bedwars', 'void_final_deaths_bedwars', 'wins_bedwars']]

y = df['Cheat']

# 訓練データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# model = MLPClassifier(hidden_layer_sizes=(500,50), max_iter=200)
model = RandomForestClassifier(random_state=0)
model.fit(X_train_scaled, y_train)

# 訓練データの正解率
train_accuracy = model.score(X_train_scaled, y_train)
print(f'Training Accuracy: {train_accuracy}')

# テストデータの正解率
test_accuracy = model.score(X_test_scaled, y_test)
print(f'Testing Accuracy: {test_accuracy}')

data = [[381135, 6514661.0, 810, 30, 2331, 4604, 172, 168, 194, 1263, 0, 0, 90, 62, 504, 836792, 47915, 810, 1423, 750865, 9234, 2445, 1429, 458, 63, 87, 331, 1375, 1993, 2542, 2989, 5443, 1279, 4311, 411, 666, 2257, 1263, 1, 1.4494545454545456, 0.9874902267396404, 0.5692199578355587, 11.587209302325581, 31.6453488372093, 4.709302325581396]]

# print(X.columns.tolist())
new_data = []
for item in data:
    data_list = item[:38]+item[39:]
    new_data.append(data_list)

columns_ = ['karma', 'networkExp', 'bedwars_beds', 'bedwars_bedwars_challenger', 'bedwars_bedwars_killer', 'bedwars_collectors_edition', 'bedwars_level', 'bedwars_loot_box', 'bedwars_slumber_ticket_master', 'bedwars_wins', 'challenges', 'all_timeBEDWARS__defensive', 'BEDWARS__offensive', 'BEDWARS__support', 'Bedwars_openedChests', 'Experience', '_items_purchased_bedwars', 'beds_broken_bedwars', 'beds_lost_bedwars', 'coins', 'deaths_bedwars', 'diamond_resources_collected_bedwars', 'emerald_resources_collected_bedwars', 'fall_deaths_bedwars', 'fall_final_deaths_bedwars', 'fall_final_kills_bedwars', 'fall_kills_bedwars', 'final_deaths_bedwars', 'final_kills_bedwars', 'games_played_bedwars', 'games_played_bedwars_1', 'kills_bedwars', 'losses_bedwars', 'void_deaths_bedwars', 'void_final_deaths_bedwars', 'void_final_kills_bedwars', 'void_kills_bedwars', 'wins_bedwars','fkdr','wlr','bblr','fk_lev','bb_lev','kill_lev']
select_bool = []
for i, column in enumerate(columns_):
    if column in X.columns.tolist():
        select_bool.append(True)
    else:
        select_bool.append(False)

new_datas = []
for i, item in enumerate(new_data):
    new_data = []
    for j in range(len(item)):
        if select_bool[j]:
            new_data.append(item[j])
    new_datas.append(new_data)


X_test_scaled = pd.DataFrame(new_datas, columns=X.columns.tolist())
scaler = StandardScaler()
X_test_scaled2 = scaler.fit_transform(X_test_scaled)

y_pred = model.predict(X_test_scaled2)

print(y_pred)