import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

data_path = "./Cheater/Data2.csv"
df = pd.read_csv(data_path)

X = df.drop('Cheat', axis=1)

# X = df[['karma', 'networkExp', 'bedwars_bedwars_killer', 'bedwars_loot_box','BEDWARS__offensive', 'Bedwars_openedChests', 'coins','final_deaths_bedwars', 'losses_bedwars', 'wins_bedwars','fkdr','wlr','bblr','fk_lev','bb_lev','kill_lev']]
# X = df[['networkExp', 'bedwars_beds', 'bedwars_level', 'bedwars_wins', 'beds_broken_bedwars', 'beds_lost_bedwars', 'deaths_bedwars', 'diamond_resources_collected_bedwars', 'emerald_resources_collected_bedwars', 'fall_deaths_bedwars', 'final_deaths_bedwars', 'final_kills_bedwars', 'games_played_bedwars', 'games_played_bedwars_1', 'kills_bedwars', 'losses_bedwars', 'void_deaths_bedwars', 'void_final_deaths_bedwars', 'wins_bedwars']]

y = df['Cheat']

# 訓練データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# X_train_scaled = X_train
# X_test_scaled = X_test

# model = MLPClassifier(hidden_layer_sizes=(500,50), max_iter=200)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 訓練データの正解率
train_accuracy = model.score(X_train_scaled, y_train)
print(f'Training Accuracy: {train_accuracy}')

# テストデータの正解率
test_accuracy = model.score(X_test_scaled, y_test)
print(f'Testing Accuracy: {test_accuracy}')

joblib.dump(scaler, 'models/scaler/scaler.joblib')
# モデルをファイルに保存
joblib.dump(model, 'models/Cheater.pkl')