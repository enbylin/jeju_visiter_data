import pandas as pd

def ranking_score(df):
    
    if df['ranking'] == 1:
        df['rank_score'] = 10
    elif df['ranking'] == 2:
        df['rank_score'] = 9
    elif df['ranking'] == 3:
        df['rank_score'] = 8
    elif df['ranking'] == 4:
        df['rank_score'] = 7
    elif df['ranking'] == 5:
        df['rank_score'] = 6
    elif df['ranking'] == 6:
        df['rank_score'] = 5
    elif df['ranking'] == 7:
        df['rank_score'] = 4
    elif df['ranking'] == 8:
        df['rank_score'] = 3
    elif df['ranking'] == 9:
        df['rank_score'] = 2
    elif df['ranking'] == 10:
        df['rank_score'] = 1
    
    return df