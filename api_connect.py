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
    name = df['poi'][0]
    code = df['confirmId'][0]
    return name, code

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
    return df_cnt


def visitor_gender(code):
    url = f'{VISITOR_URL}{api_key}?confirmId={code}'
    json_temp = json_read(url)
    df_gender = pd.DataFrame(data=json_temp['data'][0]['gender'])
    df_gender = df_gender[['labels', 'data']]
    df_gender = df_gender.rename(columns=({'labels':'성별', 'data':'인기도수치'})) 
    return df_gender


if __name__ == "__main__":    
    
    poi = '천지연폭포'
    poi_name, poi_code = contents_connet(poi)

    print(visitor_age(poi_code))
    print(visitor_cnt(poi_code))
    print(visitor_gender(poi_code))
