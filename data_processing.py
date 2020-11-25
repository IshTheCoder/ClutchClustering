import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import plotly.graph_objects as go


df_shots = pd.read_csv('shots_fixed.csv')

# month_number = datetime.datetime.strptime(month_name, '%b').month

sched = pd.read_excel('2015-2016_NBA_Historical_Schedule.xlsx')


#df_shots['Margin']=df_shots.apply(lambda row: (sched['Home TEAM FINAL SCORE'] - sched['ROAD TEAM FINAL SCORE']) if row['Game_Id'] == sched['Game_Id'], axis=1)

Margins=[]

# (20151223 Los Angeles Lakers)


for index, row in df_shots.iterrows():
    print(index)
    Game_Id = row['GAME_ID']

    game = sched[sched['GAME ID'] == Game_Id]
    margin = game['HOME TEAM FINAL SCORE'] - game['ROAD TEAM FINAL SCORE']


    Margins.append(margin.values[0])


# print(Margins)
df_shots['Margin'] = Margins
df_shots.to_csv('shot_logs_margin.csv')
#     

# print(Margins)