from oauth2client.service_account import ServiceAccountCredentials
import gspread
from api import google_key
import api_connect as ac

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

# 로그인 인증키 저장
creds = ServiceAccountCredentials.from_json_keyfile_name(google_key, scope)

sheet_name = "api_test"  # 파일명 변수 저장
client = gspread.authorize(creds)  # 연동 및 로그인 인증
sps = client.open(sheet_name)  # 파일 연동 후 저장

tab1_sheet = sps.worksheet("tab1")  # 파일내 워크시트 선택 후 저장
tab2_sheet = sps.worksheet("tab2")
tab3_sheet = sps.worksheet("tab3")

### 업데이트 영역 ###

# DataFrame create
poi = '천지연폭포'
poi_code = ac.contents_connet(poi)

age_df = ac.visitor_age(poi_code)
cnt_df = ac.visitor_cnt(poi_code)
gender_df = ac.visitor_gender(poi_code)

# 셀 업데이트
# tab1_sheet.update_acell("A2", "AAA")

def sheet_update(sheet_obj, df):
    sheet_obj.update([df.columns.values.tolist()] + df.values.tolist())


sheet_update(tab1_sheet, age_df)
sheet_update(tab2_sheet, cnt_df)
sheet_update(tab3_sheet, gender_df)