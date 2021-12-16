import time
import requests
import signaturehelper
import pandas as pd
import json

#네이버광고 키워드 분석 api 사용
#https://naver.github.io/searchad-apidoc/#/tags/RelKwdStat
BASE_URL = 'https://api.naver.com'
API_KEY = 'your apikey'
SECRET_KEY = 'your secretkey'
CUSTOMER_ID = 'your ID'

def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}

def get_df():
    # 키워드 검색
    relKeyword = '텐트' #hintKeywords
    includeHintKeywords = ''
    showDetail = 1

    uri = '/keywordstool'
    method = 'GET'
    r = requests.get(BASE_URL + uri, params={'hintKeywords': relKeyword, 'showDetail': showDetail}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))


    df=pd.DataFrame(r.json()['keywordList'])
    
    df[['monthlyMobileQcCnt', 'monthlyPcQcCnt']] = df[['monthlyMobileQcCnt', 'monthlyPcQcCnt']].apply(pd.to_numeric, errors='coerce')
    
    df['검색량'] = df['monthlyMobileQcCnt'] + df['monthlyPcQcCnt']
    
    df.rename({'compIdx':'경쟁정도',
            'monthlyAveMobileClkCnt':'월평균클릭수_모바일',
            'monthlyAveMobileCtr':'월평균클릭률_모바일',
            'monthlyAvePcClkCnt':'월평균클릭수_PC',
            'monthlyAvePcCtr':'월평균클릭률_PC', 
            'monthlyMobileQcCnt':'월간검색수_모바일',
            'monthlyPcQcCnt': '월간검색수_PC',
            'plAvgDepth':'월평균노출광고수', 
            'relKeyword':'연관키워드'},axis=1,inplace=True)
    
    return df


#if __name__ == "__main__":
    #get_df()