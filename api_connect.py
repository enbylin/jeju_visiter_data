from api import api_key
import pandas as pd
import json
import requests

def json_read(url):
    res = requests.get(url)
    json_temp = json.loads(res.text)
    return json_temp


def contents_connet(value):
    url = f'https://gw.jejudatahub.net/api/proxy/19a83f9fdb2c11e79252394919cf6a6f/{api_key}?poi={value}'
    json_temp = json_read(url)
    df = pd.DataFrame(data=json_temp['data'])
    code = df['confirmId'][0]
    return code

VISITOR_URL = 'https://gw.jejudatahub.net/api/proxy/f0663087dbb211e79252394919cf6a6f/'

def visitor_age(code):
    url = f'{VISITOR_URL}{api_key}?confirmId={code}'
    json_temp = json_read(url)
    df_age = pd.DataFrame(data=json_temp['data'][0]['age'])
    df_age = df_age[['labels', 'data']]
    df_age = df_age.rename(columns=({'labels':'연령대', 'data':'인기도수치'})) 
    return df_age


def visitor_cnt(code):
    url = f'{VISITOR_URL}{api_key}?confirmId={code}'
    json_temp = json_read(url)
    df_cnt = pd.DataFrame(data=json_temp['data'][0]['day'])
    df_cnt = df_cnt[['labels', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']]
    df_cnt = df_cnt.rename(columns=({'labels':'시간대'}))
    
    df_cnt_temp = df_cnt[['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']]
    
    df_cnt_temp_a = pd.DataFrame()
    df_cnt_temp_b = pd.DataFrame()
    
    for col in df_cnt_temp.columns:
        df_cnt_temp_a['인기도수치'] = df_cnt_temp[col]
        df_cnt_temp_a['요일'] = col
        df_cnt_temp_a['시간대'] = df_cnt['시간대']    

        if col == 'monday':           
            df_cnt_temp_b = pd.concat([df_cnt_temp_b, df_cnt_temp_a], axis=1)
        else:                   
            df_cnt_temp_b = pd.concat([df_cnt_temp_b, df_cnt_temp_a])
    
    df_cnt_temp_b = df_cnt_temp_b[['시간대', '요일', '인기도수치']]

    return df_cnt_temp_b


def visitor_gender(code):
    url = f'{VISITOR_URL}{api_key}?confirmId={code}'
    json_temp = json_read(url)
    df_gender = pd.DataFrame(data=json_temp['data'][0]['gender'])
    df_gender = df_gender[['labels', 'data']]
    df_gender = df_gender.rename(columns=({'labels':'성별', 'data':'인기도수치'})) 
    return df_gender


if __name__ == "__main__":    
    
    poi = '천지연폭포'
    poi_code = contents_connet(poi)
    
    print(visitor_cnt(poi_code))

  

    