---
title: home_credit_default_risk
---

# Kaggle API 설치
- Google Colab에서 Kaggle API를 불러오려면 다음 소스코드를 실행한다.


```python
!pip install kaggle
```

    Requirement already satisfied: kaggle in /usr/local/lib/python3.6/dist-packages (1.5.9)
    Requirement already satisfied: requests in /usr/local/lib/python3.6/dist-packages (from kaggle) (2.23.0)
    Requirement already satisfied: slugify in /usr/local/lib/python3.6/dist-packages (from kaggle) (0.0.1)
    Requirement already satisfied: urllib3 in /usr/local/lib/python3.6/dist-packages (from kaggle) (1.24.3)
    Requirement already satisfied: tqdm in /usr/local/lib/python3.6/dist-packages (from kaggle) (4.41.1)
    Requirement already satisfied: python-slugify in /usr/local/lib/python3.6/dist-packages (from kaggle) (4.0.1)
    Requirement already satisfied: six>=1.10 in /usr/local/lib/python3.6/dist-packages (from kaggle) (1.15.0)
    Requirement already satisfied: certifi in /usr/local/lib/python3.6/dist-packages (from kaggle) (2020.6.20)
    Requirement already satisfied: python-dateutil in /usr/local/lib/python3.6/dist-packages (from kaggle) (2.8.1)
    Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.6/dist-packages (from requests->kaggle) (2.10)
    Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.6/dist-packages (from requests->kaggle) (3.0.4)
    Requirement already satisfied: text-unidecode>=1.3 in /usr/local/lib/python3.6/dist-packages (from python-slugify->kaggle) (1.3)
    

## 1. Kaggle Token 다운로드
- Kaggle에서 `API Token`을 다운로드 받는다. 
- [Kaggle]-[My Account]-[API]-[Create New API Token]을 누르면 kaggle.json 파일이 다운로드 된다. 
- 이 파일을 바탕화면에 옮긴 뒤, 아래 코드(토큰을 실행시키는 코드)를 실행 시킨다.





```python
from google.colab import files
uploaded = files.upload()
for fn in uploaded.keys():
  print('uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  
# kaggle.json을 아래 폴더로 옮긴 뒤, file을 사용할 수 있도록 권한을 부여한다. 
!mkdir -p ~/.kaggle/ && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json
```



<input type="file" id="files-6d88dc91-54e2-468b-be7e-dc5aa0fecab8" name="files[]" multiple disabled
   style="border:none" />
<output id="result-6d88dc91-54e2-468b-be7e-dc5aa0fecab8">
 Upload widget is only available when the cell has been executed in the
 current browser session. Please rerun this cell to enable.
 </output>
 <script src="/nbextensions/google.colab/files.js"></script> 


    Saving kaggle.json to kaggle.json
    uploaded file "kaggle.json" with length 66 bytes
    

- 아래 코드는 실행됬는지 확인하는 코드


```python
ls -1ha ~/.kaggle/kaggle.json
```

    /root/.kaggle/kaggle.json
    

## 2. Kaggle 데이터 불러오기
- 먼저 kaggle competition list를 불러온다.


```python
!kaggle competitions list
```

    Warning: Looks like you're using an outdated API Version, please consider updating (server 1.5.9 / client 1.5.4)
    ref                                            deadline             category            reward  teamCount  userHasEntered  
    ---------------------------------------------  -------------------  ---------------  ---------  ---------  --------------  
    contradictory-my-dear-watson                   2030-07-01 23:59:00  Getting Started     Prizes        134           False  
    gan-getting-started                            2030-07-01 23:59:00  Getting Started     Prizes        161           False  
    tpu-getting-started                            2030-06-03 23:59:00  Getting Started  Knowledge        292           False  
    digit-recognizer                               2030-01-01 00:00:00  Getting Started  Knowledge       2248           False  
    titanic                                        2030-01-01 00:00:00  Getting Started  Knowledge      17260            True  
    house-prices-advanced-regression-techniques    2030-01-01 00:00:00  Getting Started  Knowledge       4325            True  
    connectx                                       2030-01-01 00:00:00  Getting Started  Knowledge        366           False  
    nlp-getting-started                            2030-01-01 00:00:00  Getting Started  Knowledge       1130           False  
    rock-paper-scissors                            2021-02-01 23:59:00  Playground          Prizes        226           False  
    riiid-test-answer-prediction                   2021-01-07 23:59:00  Featured          $100,000       1491           False  
    nfl-big-data-bowl-2021                         2021-01-05 23:59:00  Analytics         $100,000          0           False  
    competitive-data-science-predict-future-sales  2020-12-31 23:59:00  Playground           Kudos       9392           False  
    halite-iv-playground-edition                   2020-12-31 23:59:00  Playground       Knowledge         44           False  
    predict-volcanic-eruptions-ingv-oe             2020-12-28 23:59:00  Playground            Swag        198           False  
    hashcode-drone-delivery                        2020-12-14 23:59:00  Playground       Knowledge         80           False  
    cdp-unlocking-climate-solutions                2020-12-02 23:59:00  Analytics          $91,000          0           False  
    lish-moa                                       2020-11-30 23:59:00  Research           $30,000       3454           False  
    google-football                                2020-11-30 23:59:00  Featured            $6,000        925           False  
    conways-reverse-game-of-life-2020              2020-11-30 23:59:00  Playground            Swag        132           False  
    lyft-motion-prediction-autonomous-vehicles     2020-11-25 23:59:00  Featured           $30,000        788           False  
    


```python
!kaggle competitions download -c home-credit-default-risk
```

    Warning: Looks like you're using an outdated API Version, please consider updating (server 1.5.9 / client 1.5.4)
    installments_payments.csv.zip: Skipping, found more recently modified local copy (use --force to force download)
    previous_application.csv.zip: Skipping, found more recently modified local copy (use --force to force download)
    application_test.csv.zip: Skipping, found more recently modified local copy (use --force to force download)
    bureau.csv.zip: Skipping, found more recently modified local copy (use --force to force download)
    sample_submission.csv: Skipping, found more recently modified local copy (use --force to force download)
    POS_CASH_balance.csv.zip: Skipping, found more recently modified local copy (use --force to force download)
    credit_card_balance.csv.zip: Skipping, found more recently modified local copy (use --force to force download)
    HomeCredit_columns_description.csv: Skipping, found more recently modified local copy (use --force to force download)
    application_train.csv.zip: Skipping, found more recently modified local copy (use --force to force download)
    bureau_balance.csv.zip: Skipping, found more recently modified local copy (use --force to force download)
    

- ls는 디렉터리(파일,경로) 내의 데이터 파일을 보여주는 명령어


```python
!ls
```

    application_test.csv.zip	    installments_payments.csv.zip
    application_train.csv.zip	    POS_CASH_balance.csv.zip
    bureau_balance.csv.zip		    previous_application.csv.zip
    bureau.csv.zip			    sample_data
    credit_card_balance.csv.zip	    sample_submission.csv
    gender_submission.csv		    test.csv
    HomeCredit_columns_description.csv  train.csv
    


```python
! unzip application_test.csv.zip	  
! unzipinstallments_payments.csv.zip
! unzip application_train.csv.zip	    
! unzip POS_CASH_balance.csv.zip
! unzip bureau_balance.csv.zip		    
! unzip previous_application.csv.zip
! unzip bureau.csv.zip			    
! unzip credit_card_balance.csv.zip
```

    Archive:  application_test.csv.zip
      inflating: application_test.csv    
    /bin/bash: unzipinstallments_payments.csv.zip: command not found
    Archive:  application_train.csv.zip
    replace application_train.csv? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
      inflating: application_train.csv   
    Archive:  POS_CASH_balance.csv.zip
    replace POS_CASH_balance.csv? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
      inflating: POS_CASH_balance.csv    
    Archive:  bureau_balance.csv.zip
    replace bureau_balance.csv? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
      inflating: bureau_balance.csv      
    Archive:  previous_application.csv.zip
    replace previous_application.csv? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
      inflating: previous_application.csv  
    Archive:  bureau.csv.zip
    replace bureau.csv? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
      inflating: bureau.csv              
    Archive:  credit_card_balance.csv.zip
    replace credit_card_balance.csv? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
      inflating: credit_card_balance.csv  
    

- 현재 총 14개의 데이터를 다운로드 받았다. 
 + application_test.csv.zip	  
 + installments_payments.csv.zip
 + application_train.csv.zip	    
 + POS_CASH_balance.csv.zip
 + bureau_balance.csv.zip		    
 + previous_application.csv.zip
 + bureau.csv.zip			    
 + sample_data
 + credit_card_balance.csv.zip	     
 + sample_submission.csv
 + gender_submission.csv		    
 + test.csv
 + HomeCredit_columns_description.csv  
 + train.csv

## 3. 캐글 데이터 수집 및 EDA 
- 우선 데이터를 수집하기에 앞서서 `EDA`에 관한 필수 패키지를 설치하자. 


```python
# 데이터 조작을 위한 numpy와 팬더
import numpy as np
import pandas as pd  
# 범주형 변수를 처리하기 위한 사전 처리 학습
from sklearn.preprocessing import LabelEncoder
# 파일 시스템 매니지먼트
import os
# 경고 억제
import warnings
warnings.filterwarnings('ignore')
# 플롯을 위한 matplotlib 및 seaorn
import matplotlib.pyplot as plt
import seaborn as sns
```

## 분류
- 감독됨: 라벨은 교육 데이터에 포함되며, 목적은 형상으로부터 라벨을 예측하는 방법을 학습하는 모델을 훈련시키는 것이다.
- 분류: 라벨은 0(대출금을 제때 상환할 수 있음), 1(대출금 상환에 어려움이 있음)의 이진 변수다.
- 데이터 : 은행을 이용하지 않은 사람들에게 신용대출(대출)을 제공하는 서비스인 홈 크레딧에 의해 제공된다


```python
# 사용 가능한 파일 나열
print(os.listdir())
```

    ['.config', 'previous_application.csv', 'application_train.csv', 'bureau_balance.csv', 'application_test.csv.zip', 'bureau.csv', 'POS_CASH_balance.csv', 'previous_application.csv.zip', 'bureau_balance.csv.zip', 'POS_CASH_balance.csv.zip', 'HomeCredit_columns_description.csv', 'bureau.csv.zip', 'installments_payments.csv.zip', 'test.csv', 'sample_submission.csv', 'application_train.csv.zip', 'gender_submission.csv', 'credit_card_balance.csv', 'credit_card_balance.csv.zip', 'train.csv', 'sample_data']
    


```python
# 교육자료
app_train = pd.read_csv('application_train.csv')
print('Training data shape: ', app_train.shape)
app_train.head()
```

    Training data shape:  (307511, 122)
    




<div style = overflow:scroll;>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SK_ID_CURR</th>
      <th>TARGET</th>
      <th>NAME_CONTRACT_TYPE</th>
      <th>CODE_GENDER</th>
      <th>FLAG_OWN_CAR</th>
      <th>FLAG_OWN_REALTY</th>
      <th>CNT_CHILDREN</th>
      <th>AMT_INCOME_TOTAL</th>
      <th>AMT_CREDIT</th>
      <th>AMT_ANNUITY</th>
      <th>AMT_GOODS_PRICE</th>
      <th>NAME_TYPE_SUITE</th>
      <th>NAME_INCOME_TYPE</th>
      <th>NAME_EDUCATION_TYPE</th>
      <th>NAME_FAMILY_STATUS</th>
      <th>NAME_HOUSING_TYPE</th>
      <th>REGION_POPULATION_RELATIVE</th>
      <th>DAYS_BIRTH</th>
      <th>DAYS_EMPLOYED</th>
      <th>DAYS_REGISTRATION</th>
      <th>DAYS_ID_PUBLISH</th>
      <th>OWN_CAR_AGE</th>
      <th>FLAG_MOBIL</th>
      <th>FLAG_EMP_PHONE</th>
      <th>FLAG_WORK_PHONE</th>
      <th>FLAG_CONT_MOBILE</th>
      <th>FLAG_PHONE</th>
      <th>FLAG_EMAIL</th>
      <th>OCCUPATION_TYPE</th>
      <th>CNT_FAM_MEMBERS</th>
      <th>REGION_RATING_CLIENT</th>
      <th>REGION_RATING_CLIENT_W_CITY</th>
      <th>WEEKDAY_APPR_PROCESS_START</th>
      <th>HOUR_APPR_PROCESS_START</th>
      <th>REG_REGION_NOT_LIVE_REGION</th>
      <th>REG_REGION_NOT_WORK_REGION</th>
      <th>LIVE_REGION_NOT_WORK_REGION</th>
      <th>REG_CITY_NOT_LIVE_CITY</th>
      <th>REG_CITY_NOT_WORK_CITY</th>
      <th>LIVE_CITY_NOT_WORK_CITY</th>
      <th>...</th>
      <th>LIVINGAPARTMENTS_MEDI</th>
      <th>LIVINGAREA_MEDI</th>
      <th>NONLIVINGAPARTMENTS_MEDI</th>
      <th>NONLIVINGAREA_MEDI</th>
      <th>FONDKAPREMONT_MODE</th>
      <th>HOUSETYPE_MODE</th>
      <th>TOTALAREA_MODE</th>
      <th>WALLSMATERIAL_MODE</th>
      <th>EMERGENCYSTATE_MODE</th>
      <th>OBS_30_CNT_SOCIAL_CIRCLE</th>
      <th>DEF_30_CNT_SOCIAL_CIRCLE</th>
      <th>OBS_60_CNT_SOCIAL_CIRCLE</th>
      <th>DEF_60_CNT_SOCIAL_CIRCLE</th>
      <th>DAYS_LAST_PHONE_CHANGE</th>
      <th>FLAG_DOCUMENT_2</th>
      <th>FLAG_DOCUMENT_3</th>
      <th>FLAG_DOCUMENT_4</th>
      <th>FLAG_DOCUMENT_5</th>
      <th>FLAG_DOCUMENT_6</th>
      <th>FLAG_DOCUMENT_7</th>
      <th>FLAG_DOCUMENT_8</th>
      <th>FLAG_DOCUMENT_9</th>
      <th>FLAG_DOCUMENT_10</th>
      <th>FLAG_DOCUMENT_11</th>
      <th>FLAG_DOCUMENT_12</th>
      <th>FLAG_DOCUMENT_13</th>
      <th>FLAG_DOCUMENT_14</th>
      <th>FLAG_DOCUMENT_15</th>
      <th>FLAG_DOCUMENT_16</th>
      <th>FLAG_DOCUMENT_17</th>
      <th>FLAG_DOCUMENT_18</th>
      <th>FLAG_DOCUMENT_19</th>
      <th>FLAG_DOCUMENT_20</th>
      <th>FLAG_DOCUMENT_21</th>
      <th>AMT_REQ_CREDIT_BUREAU_HOUR</th>
      <th>AMT_REQ_CREDIT_BUREAU_DAY</th>
      <th>AMT_REQ_CREDIT_BUREAU_WEEK</th>
      <th>AMT_REQ_CREDIT_BUREAU_MON</th>
      <th>AMT_REQ_CREDIT_BUREAU_QRT</th>
      <th>AMT_REQ_CREDIT_BUREAU_YEAR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100002</td>
      <td>1</td>
      <td>Cash loans</td>
      <td>M</td>
      <td>N</td>
      <td>Y</td>
      <td>0</td>
      <td>202500.0</td>
      <td>406597.5</td>
      <td>24700.5</td>
      <td>351000.0</td>
      <td>Unaccompanied</td>
      <td>Working</td>
      <td>Secondary / secondary special</td>
      <td>Single / not married</td>
      <td>House / apartment</td>
      <td>0.018801</td>
      <td>-9461</td>
      <td>-637</td>
      <td>-3648.0</td>
      <td>-2120</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>Laborers</td>
      <td>1.0</td>
      <td>2</td>
      <td>2</td>
      <td>WEDNESDAY</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0205</td>
      <td>0.0193</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>reg oper account</td>
      <td>block of flats</td>
      <td>0.0149</td>
      <td>Stone, brick</td>
      <td>No</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>-1134.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100003</td>
      <td>0</td>
      <td>Cash loans</td>
      <td>F</td>
      <td>N</td>
      <td>N</td>
      <td>0</td>
      <td>270000.0</td>
      <td>1293502.5</td>
      <td>35698.5</td>
      <td>1129500.0</td>
      <td>Family</td>
      <td>State servant</td>
      <td>Higher education</td>
      <td>Married</td>
      <td>House / apartment</td>
      <td>0.003541</td>
      <td>-16765</td>
      <td>-1188</td>
      <td>-1186.0</td>
      <td>-291</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>Core staff</td>
      <td>2.0</td>
      <td>1</td>
      <td>1</td>
      <td>MONDAY</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0787</td>
      <td>0.0558</td>
      <td>0.0039</td>
      <td>0.01</td>
      <td>reg oper account</td>
      <td>block of flats</td>
      <td>0.0714</td>
      <td>Block</td>
      <td>No</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>-828.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100004</td>
      <td>0</td>
      <td>Revolving loans</td>
      <td>M</td>
      <td>Y</td>
      <td>Y</td>
      <td>0</td>
      <td>67500.0</td>
      <td>135000.0</td>
      <td>6750.0</td>
      <td>135000.0</td>
      <td>Unaccompanied</td>
      <td>Working</td>
      <td>Secondary / secondary special</td>
      <td>Single / not married</td>
      <td>House / apartment</td>
      <td>0.010032</td>
      <td>-19046</td>
      <td>-225</td>
      <td>-4260.0</td>
      <td>-2531</td>
      <td>26.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>Laborers</td>
      <td>1.0</td>
      <td>2</td>
      <td>2</td>
      <td>MONDAY</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-815.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100006</td>
      <td>0</td>
      <td>Cash loans</td>
      <td>F</td>
      <td>N</td>
      <td>Y</td>
      <td>0</td>
      <td>135000.0</td>
      <td>312682.5</td>
      <td>29686.5</td>
      <td>297000.0</td>
      <td>Unaccompanied</td>
      <td>Working</td>
      <td>Secondary / secondary special</td>
      <td>Civil marriage</td>
      <td>House / apartment</td>
      <td>0.008019</td>
      <td>-19005</td>
      <td>-3039</td>
      <td>-9833.0</td>
      <td>-2437</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>Laborers</td>
      <td>2.0</td>
      <td>2</td>
      <td>2</td>
      <td>WEDNESDAY</td>
      <td>17</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>-617.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>100007</td>
      <td>0</td>
      <td>Cash loans</td>
      <td>M</td>
      <td>N</td>
      <td>Y</td>
      <td>0</td>
      <td>121500.0</td>
      <td>513000.0</td>
      <td>21865.5</td>
      <td>513000.0</td>
      <td>Unaccompanied</td>
      <td>Working</td>
      <td>Secondary / secondary special</td>
      <td>Single / not married</td>
      <td>House / apartment</td>
      <td>0.028663</td>
      <td>-19932</td>
      <td>-3038</td>
      <td>-4311.0</td>
      <td>-3458</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>Core staff</td>
      <td>1.0</td>
      <td>2</td>
      <td>2</td>
      <td>THURSDAY</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-1106.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 122 columns</p>
</div>



교육 데이터에는 307511개의 관측치(각각 별도 대출)와 대상(우리가 예측하고자 하는 라벨)을 포함한 122개의 특징(변수)이 있다.


```python
# 데이터 기능 테스트
app_test = pd.read_csv('application_test.csv')
print('Testing data shape: ', app_test.shape)
app_test.head()
```

    Testing data shape:  (48744, 121)
    




<div style = overflow:scroll;>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SK_ID_CURR</th>
      <th>NAME_CONTRACT_TYPE</th>
      <th>CODE_GENDER</th>
      <th>FLAG_OWN_CAR</th>
      <th>FLAG_OWN_REALTY</th>
      <th>CNT_CHILDREN</th>
      <th>AMT_INCOME_TOTAL</th>
      <th>AMT_CREDIT</th>
      <th>AMT_ANNUITY</th>
      <th>AMT_GOODS_PRICE</th>
      <th>NAME_TYPE_SUITE</th>
      <th>NAME_INCOME_TYPE</th>
      <th>NAME_EDUCATION_TYPE</th>
      <th>NAME_FAMILY_STATUS</th>
      <th>NAME_HOUSING_TYPE</th>
      <th>REGION_POPULATION_RELATIVE</th>
      <th>DAYS_BIRTH</th>
      <th>DAYS_EMPLOYED</th>
      <th>DAYS_REGISTRATION</th>
      <th>DAYS_ID_PUBLISH</th>
      <th>OWN_CAR_AGE</th>
      <th>FLAG_MOBIL</th>
      <th>FLAG_EMP_PHONE</th>
      <th>FLAG_WORK_PHONE</th>
      <th>FLAG_CONT_MOBILE</th>
      <th>FLAG_PHONE</th>
      <th>FLAG_EMAIL</th>
      <th>OCCUPATION_TYPE</th>
      <th>CNT_FAM_MEMBERS</th>
      <th>REGION_RATING_CLIENT</th>
      <th>REGION_RATING_CLIENT_W_CITY</th>
      <th>WEEKDAY_APPR_PROCESS_START</th>
      <th>HOUR_APPR_PROCESS_START</th>
      <th>REG_REGION_NOT_LIVE_REGION</th>
      <th>REG_REGION_NOT_WORK_REGION</th>
      <th>LIVE_REGION_NOT_WORK_REGION</th>
      <th>REG_CITY_NOT_LIVE_CITY</th>
      <th>REG_CITY_NOT_WORK_CITY</th>
      <th>LIVE_CITY_NOT_WORK_CITY</th>
      <th>ORGANIZATION_TYPE</th>
      <th>...</th>
      <th>LIVINGAPARTMENTS_MEDI</th>
      <th>LIVINGAREA_MEDI</th>
      <th>NONLIVINGAPARTMENTS_MEDI</th>
      <th>NONLIVINGAREA_MEDI</th>
      <th>FONDKAPREMONT_MODE</th>
      <th>HOUSETYPE_MODE</th>
      <th>TOTALAREA_MODE</th>
      <th>WALLSMATERIAL_MODE</th>
      <th>EMERGENCYSTATE_MODE</th>
      <th>OBS_30_CNT_SOCIAL_CIRCLE</th>
      <th>DEF_30_CNT_SOCIAL_CIRCLE</th>
      <th>OBS_60_CNT_SOCIAL_CIRCLE</th>
      <th>DEF_60_CNT_SOCIAL_CIRCLE</th>
      <th>DAYS_LAST_PHONE_CHANGE</th>
      <th>FLAG_DOCUMENT_2</th>
      <th>FLAG_DOCUMENT_3</th>
      <th>FLAG_DOCUMENT_4</th>
      <th>FLAG_DOCUMENT_5</th>
      <th>FLAG_DOCUMENT_6</th>
      <th>FLAG_DOCUMENT_7</th>
      <th>FLAG_DOCUMENT_8</th>
      <th>FLAG_DOCUMENT_9</th>
      <th>FLAG_DOCUMENT_10</th>
      <th>FLAG_DOCUMENT_11</th>
      <th>FLAG_DOCUMENT_12</th>
      <th>FLAG_DOCUMENT_13</th>
      <th>FLAG_DOCUMENT_14</th>
      <th>FLAG_DOCUMENT_15</th>
      <th>FLAG_DOCUMENT_16</th>
      <th>FLAG_DOCUMENT_17</th>
      <th>FLAG_DOCUMENT_18</th>
      <th>FLAG_DOCUMENT_19</th>
      <th>FLAG_DOCUMENT_20</th>
      <th>FLAG_DOCUMENT_21</th>
      <th>AMT_REQ_CREDIT_BUREAU_HOUR</th>
      <th>AMT_REQ_CREDIT_BUREAU_DAY</th>
      <th>AMT_REQ_CREDIT_BUREAU_WEEK</th>
      <th>AMT_REQ_CREDIT_BUREAU_MON</th>
      <th>AMT_REQ_CREDIT_BUREAU_QRT</th>
      <th>AMT_REQ_CREDIT_BUREAU_YEAR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100001</td>
      <td>Cash loans</td>
      <td>F</td>
      <td>N</td>
      <td>Y</td>
      <td>0</td>
      <td>135000.0</td>
      <td>568800.0</td>
      <td>20560.5</td>
      <td>450000.0</td>
      <td>Unaccompanied</td>
      <td>Working</td>
      <td>Higher education</td>
      <td>Married</td>
      <td>House / apartment</td>
      <td>0.018850</td>
      <td>-19241</td>
      <td>-2329</td>
      <td>-5170.0</td>
      <td>-812</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>2</td>
      <td>2</td>
      <td>TUESDAY</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>Kindergarten</td>
      <td>...</td>
      <td>NaN</td>
      <td>0.0514</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>block of flats</td>
      <td>0.0392</td>
      <td>Stone, brick</td>
      <td>No</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-1740.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100005</td>
      <td>Cash loans</td>
      <td>M</td>
      <td>N</td>
      <td>Y</td>
      <td>0</td>
      <td>99000.0</td>
      <td>222768.0</td>
      <td>17370.0</td>
      <td>180000.0</td>
      <td>Unaccompanied</td>
      <td>Working</td>
      <td>Secondary / secondary special</td>
      <td>Married</td>
      <td>House / apartment</td>
      <td>0.035792</td>
      <td>-18064</td>
      <td>-4469</td>
      <td>-9118.0</td>
      <td>-1623</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>Low-skill Laborers</td>
      <td>2.0</td>
      <td>2</td>
      <td>2</td>
      <td>FRIDAY</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>Self-employed</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100013</td>
      <td>Cash loans</td>
      <td>M</td>
      <td>Y</td>
      <td>Y</td>
      <td>0</td>
      <td>202500.0</td>
      <td>663264.0</td>
      <td>69777.0</td>
      <td>630000.0</td>
      <td>NaN</td>
      <td>Working</td>
      <td>Higher education</td>
      <td>Married</td>
      <td>House / apartment</td>
      <td>0.019101</td>
      <td>-20038</td>
      <td>-4458</td>
      <td>-2175.0</td>
      <td>-3503</td>
      <td>5.0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>Drivers</td>
      <td>2.0</td>
      <td>2</td>
      <td>2</td>
      <td>MONDAY</td>
      <td>14</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>Transport: type 3</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-856.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100028</td>
      <td>Cash loans</td>
      <td>F</td>
      <td>N</td>
      <td>Y</td>
      <td>2</td>
      <td>315000.0</td>
      <td>1575000.0</td>
      <td>49018.5</td>
      <td>1575000.0</td>
      <td>Unaccompanied</td>
      <td>Working</td>
      <td>Secondary / secondary special</td>
      <td>Married</td>
      <td>House / apartment</td>
      <td>0.026392</td>
      <td>-13976</td>
      <td>-1866</td>
      <td>-2000.0</td>
      <td>-4208</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>Sales staff</td>
      <td>4.0</td>
      <td>2</td>
      <td>2</td>
      <td>WEDNESDAY</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>Business Entity Type 3</td>
      <td>...</td>
      <td>0.2446</td>
      <td>0.3739</td>
      <td>0.0388</td>
      <td>0.0817</td>
      <td>reg oper account</td>
      <td>block of flats</td>
      <td>0.3700</td>
      <td>Panel</td>
      <td>No</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-1805.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>100038</td>
      <td>Cash loans</td>
      <td>M</td>
      <td>Y</td>
      <td>N</td>
      <td>1</td>
      <td>180000.0</td>
      <td>625500.0</td>
      <td>32067.0</td>
      <td>625500.0</td>
      <td>Unaccompanied</td>
      <td>Working</td>
      <td>Secondary / secondary special</td>
      <td>Married</td>
      <td>House / apartment</td>
      <td>0.010032</td>
      <td>-13040</td>
      <td>-2191</td>
      <td>-4000.0</td>
      <td>-4262</td>
      <td>16.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>2</td>
      <td>2</td>
      <td>FRIDAY</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>Business Entity Type 3</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-821.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 121 columns</p>
</div>



테스트 세트가 상당히 작고 대상 컬럼이 부족하다.

## 탐색적 데이터 분석.
탐색적 데이터 분석(EDA)은 우리가 통계를 계산하고 수치를 만들어 데이터 내의 경향, 이상 징후, 패턴 또는 관계를 찾아내는 개방형 프로세스다. EDA의 목표는 우리의 데이터가 우리에게 말해줄 수 있는 것을 배우는 것이다. 일반적으로 높은 수준의 개요에서 시작되며, 데이터에서 흥미로운 영역을 발견하면 특정 영역으로 좁혀진다. 그 결과들은 그 자체로 흥미로울 수도 있고, 어떤 기능을 사용할지 결정하는 것을 도와줌으로써 우리의 모델 선택을 알리는 데 사용될 수도 있다.

### 대상 열의 분포 조사
대상은 대출금 0을 제때 상환했거나 고객이 상환에 어려움을 겪었음을 나타내는 1을 예측하라는 것이다. 우리는 우선 각 범주에 속하는 대출의 수를 조사할 수 있다.


```python
app_train['TARGET'].value_counts()
```




    0    282686
    1     24825
    Name: TARGET, dtype: int64




```python
app_train['TARGET'].astype(int).plot.hist();
```


![png](/images/home_credit_default_risk/output_24_0.png)


이 정보로부터, 우리는 이것이 불균형한 계급 문제임을 알 수 있다. 제때 갚지 못한 대출보다 제때 갚은 대출이 훨씬 많다. 일단 우리가 좀 더 정교한 기계 학습 모델에 들어가면, 우리는 이러한 불균형을 반영하기 위해 데이터에서의 그들의 표현에 따라 수업에 무게를 둘 수 있다.

### 결측값 검사
다음으로 각 열에 있는 결측값의 수와 백분율을 살펴보기로 한다.


```python
# 결측값을 열로 계산하는 함수 #Funct 
def missing_values_table(df):
        # 결측값 합계
        mis_val = df.isnull().sum()
        
        # 결측값 백분율
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        # 결과로 테이블 만들기
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        # 열 이름 바꾸기
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # 누락된 내림차순 백분율을 기준으로 테이블 정렬
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
        # 일부 요약 정보 인쇄
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
        
        # 누락된 정보가 있는 데이터 프레임 반환
        return mis_val_table_ren_columns
```


```python
# 결측값 통계량
missing_values = missing_values_table(app_train)
missing_values.head(20)
```

    Your selected dataframe has 122 columns.
    There are 67 columns that have missing values.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Missing Values</th>
      <th>% of Total Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>COMMONAREA_MEDI</th>
      <td>214865</td>
      <td>69.9</td>
    </tr>
    <tr>
      <th>COMMONAREA_AVG</th>
      <td>214865</td>
      <td>69.9</td>
    </tr>
    <tr>
      <th>COMMONAREA_MODE</th>
      <td>214865</td>
      <td>69.9</td>
    </tr>
    <tr>
      <th>NONLIVINGAPARTMENTS_MEDI</th>
      <td>213514</td>
      <td>69.4</td>
    </tr>
    <tr>
      <th>NONLIVINGAPARTMENTS_MODE</th>
      <td>213514</td>
      <td>69.4</td>
    </tr>
    <tr>
      <th>NONLIVINGAPARTMENTS_AVG</th>
      <td>213514</td>
      <td>69.4</td>
    </tr>
    <tr>
      <th>FONDKAPREMONT_MODE</th>
      <td>210295</td>
      <td>68.4</td>
    </tr>
    <tr>
      <th>LIVINGAPARTMENTS_MODE</th>
      <td>210199</td>
      <td>68.4</td>
    </tr>
    <tr>
      <th>LIVINGAPARTMENTS_MEDI</th>
      <td>210199</td>
      <td>68.4</td>
    </tr>
    <tr>
      <th>LIVINGAPARTMENTS_AVG</th>
      <td>210199</td>
      <td>68.4</td>
    </tr>
    <tr>
      <th>FLOORSMIN_MODE</th>
      <td>208642</td>
      <td>67.8</td>
    </tr>
    <tr>
      <th>FLOORSMIN_MEDI</th>
      <td>208642</td>
      <td>67.8</td>
    </tr>
    <tr>
      <th>FLOORSMIN_AVG</th>
      <td>208642</td>
      <td>67.8</td>
    </tr>
    <tr>
      <th>YEARS_BUILD_MODE</th>
      <td>204488</td>
      <td>66.5</td>
    </tr>
    <tr>
      <th>YEARS_BUILD_MEDI</th>
      <td>204488</td>
      <td>66.5</td>
    </tr>
    <tr>
      <th>YEARS_BUILD_AVG</th>
      <td>204488</td>
      <td>66.5</td>
    </tr>
    <tr>
      <th>OWN_CAR_AGE</th>
      <td>202929</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>LANDAREA_AVG</th>
      <td>182590</td>
      <td>59.4</td>
    </tr>
    <tr>
      <th>LANDAREA_MEDI</th>
      <td>182590</td>
      <td>59.4</td>
    </tr>
    <tr>
      <th>LANDAREA_MODE</th>
      <td>182590</td>
      <td>59.4</td>
    </tr>
  </tbody>
</table>
</div>



### 열 유형
각 데이터 유형의 열 수를 살펴보자. int64와 float64는 숫자 변수(이산형 또는 연속형일 수 있음)이다. 객체 열은 문자열을 포함하며 범주형 형상이다.


```python
# 각 열 유형별 수
app_train.dtypes.value_counts()
```




    float64    65
    int64      41
    object     16
    dtype: int64



이제 각 개체(범주형) 열에 있는 고유한 항목 수를 살펴봅시다.


```python
# 각 객체 열의 고유 클래스 수
app_train.select_dtypes('object').apply(pd.Series.nunique, axis = 0)
```




    NAME_CONTRACT_TYPE             2
    CODE_GENDER                    3
    FLAG_OWN_CAR                   2
    FLAG_OWN_REALTY                2
    NAME_TYPE_SUITE                7
    NAME_INCOME_TYPE               8
    NAME_EDUCATION_TYPE            5
    NAME_FAMILY_STATUS             6
    NAME_HOUSING_TYPE              6
    OCCUPATION_TYPE               18
    WEEKDAY_APPR_PROCESS_START     7
    ORGANIZATION_TYPE             58
    FONDKAPREMONT_MODE             4
    HOUSETYPE_MODE                 3
    WALLSMATERIAL_MODE             7
    EMERGENCYSTATE_MODE            2
    dtype: int64



대부분의 범주형 변수의 고유 항목 수는 상대적으로 적다. 우리는 이러한 범주형 변수에 대처할 방법을 찾아야 할 것이다!

범주형 변수를 인코딩하는 중:
더 나아가기 전에 성가신 범주형 변수를 다뤄야 한다. 기계 학습 모델은 유감스럽게도 범주형 변수를 다룰 수 없다(LightGBM과 같은 일부 모델은 제외). 따라서 이 변수들을 모델로 넘기기 전에 숫자로 인코딩(표현)하는 방법을 찾아야 한다. 이 과정을 수행하는 방법에는 크게 두 가지가 있다.
- 라벨 인코딩: 정수를 사용하여 범주형 변수의 각 고유 범주를 할당하십시오. 새 열이 생성되지 않음 예는 아래와 같다.

- 단일 핫 인코딩: 범주형 변수의 각 고유 범주에 대해 새 열을 생성하십시오. 각 관측치는 해당 범주에 대해 열에 1을, 다른 모든 새 열에 0을 받는다.

라벨 인코딩의 문제는 카테고리에 임의의 순서를 부여한다는 것이다. 각 범주에 할당된 값은 랜덤이며 범주의 고유한 측면을 반영하지 않는다. 위의 예에서 프로그래머는 4를, 데이터 과학자는 1을 받지만, 만약 우리가 같은 과정을 다시 한다면, 라벨이 거꾸로 되거나 완전히 달라질 수 있다. 정수의 실제 할당은 임의적이다. 따라서 우리가 라벨 인코딩을 수행할 때 모델은 형상의 상대적 값(예: 프로그래머 = 4 및 데이터 과학자 = 1)을 사용하여 우리가 원하는 가중치를 할당할 수 있다. 범주형 변수(예: 남성/여성)에 대해 고유한 값이 두 개뿐이면 레이블 인코딩은 괜찮지만 두 개 이상의 고유한 범주에 대해서는 하나의 핫 인코딩이 안전한 옵션이다.

이러한 접근방식의 상대적 장점에 대해 일부 논쟁이 있으며, 일부 모델은 라벨로 인코딩된 범주형 변수를 문제 없이 다룰 수 있다. 여기 좋은 스택 오버플로 토론이 있다. 클래스가 많은 범주형 변수에 대해서는 (그리고 이것은 개인적인 의견일 뿐이다) 하나의 핫 인코딩이 범주에 임의의 값을 부과하지 않기 때문에 가장 안전한 접근법이라고 생각한다. 단일 핫 인코딩의 유일한 단점은 피쳐 수(데이터의 치수)가 범주가 많은 범주형 변수로 폭발할 수 있다는 점이다. 이를 처리하기 위해 PCA나 기타 차원성 감소 방법에 따라 1회 핫 인코딩을 수행하여 치수 수를 줄일 수 있다(여전히 정보 보존을 위해 노력).

이 노트북에서는 범주 2개만 있는 범주형 변수에 레이블 인코딩을 사용하고 범주 2개 이상의 범주형 변수에 대해 One-Hot 인코딩을 사용할 것이다. 이 과정은 프로젝트에 더 깊이 들어가면서 변화가 필요할 수 있지만, 현재로서는 이것이 우리에게 어떤 영향을 미치는지 알 수 있을 것이다. (우리는 또한 이 노트북에서 어떠한 차원성 감소도 사용하지 않고 향후 반복해서 검토할 것이다.)

### 레이블 인코딩 및 단일 핫 인코딩
위에서 설명한 정책을 실행하자: 2개의 고유한 범주를 가진 범주형 변수(dtype == 객체)에 대해서는 레이블 인코딩을 사용하고, 2개 이상의 고유한 범주를 가진 범주형 변수에 대해서는 1-hot 인코딩을 사용한다.

라벨 인코딩의 경우 Scikit-Learn LabelEncoder를 사용하고, 핫 인코딩의 경우 팬더 get_dummies(df) 기능을 사용한다.


```python
# 레이블 인코더 객체 생성
le = LabelEncoder()
le_count = 0

# 열을 반복하십시오
for col in app_train:
    if app_train[col].dtype == 'object':
        # 고유 범주가 2개 이하인 경우
        if len(list(app_train[col].unique())) <= 2:
            # 교육 데이터 교육
            le.fit(app_train[col])
            # 교육 및 테스트 데이터 모두 혁신
            app_train[col] = le.transform(app_train[col])
            app_test[col] = le.transform(app_test[col])
            
            # 레이블이 인코딩된 열 수를 추적
            le_count += 1
            
print('%d columns were label encoded.' % le_count)
```

    0 columns were label encoded.
    


```python
# 범주형 변수의 단일 핫 인코딩
app_train = pd.get_dummies(app_train)
app_test = pd.get_dummies(app_test)

print('Training Features shape: ', app_train.shape)
print('Testing Features shape: ', app_test.shape)
```

    Training Features shape:  (307511, 243)
    Testing Features shape:  (48744, 239)
    

### 교육 및 테스트 데이터 정렬
훈련 데이터와 시험 데이터 모두에서 동일한 특징(색상)이 있어야 한다. 원핫 인코딩은 시험 데이터에 나타나지 않는 범주를 포함하는 일부 범주형 변수가 있었기 때문에 훈련 데이터에 더 많은 열을 생성했다. 테스트 데이터에 없는 교육 데이터 열을 제거하려면 데이터 프레임을 정렬해야 한다. 먼저 교육 데이터에서 대상 열을 추출한다(시험 데이터에는 없지만 이 정보를 보관해야 하기 때문이다). 정렬을 수행할 때 행이 아닌 열에 따라 데이터 프레임을 정렬하도록 축 = 1을 설정해야 함! 


```python
train_labels = app_train['TARGET']

# 교육 및 테스트 데이터 정렬, 두 데이터 프레임에 열만 유지
app_train, app_test = app_train.align(app_test, join = 'inner', axis = 1)

# 목표값 다시 추가
app_train['TARGET'] = train_labels

print('Training Features shape: ', app_train.shape)
print('Testing Features shape: ', app_test.shape)
```

    Training Features shape:  (307511, 240)
    Testing Features shape:  (48744, 239)
    

교육 및 테스트 데이터셋은 이제 머신러닝에 필요한 기능과 동일한 기능을 가지고 있다. 원핫 인코딩으로 피쳐 수가 크게 늘었다. 데이터셋 크기를 줄이기 위해 언젠가는 차원성 축소(관련되지 않은 기능 제거)를 시도해보려고 할 것이다.

### 탐색 데이터 분석으로 돌아가기
이상 징후  
우리가 EDA를 할 때 항상 경계하고 싶은 한 가지 문제는 데이터 내의 이상 현상이다. 이는 잘못된 형식의 숫자, 측정 장비의 오류 또는 유효하지만 극단적인 측정 때문일 수 있다. 이상 징후를 정량적으로 지원하는 한 가지 방법은 설명 방법을 사용하여 열의 통계를 보는 것이다. DAYS_BOYDE 칼럼의 숫자는 현재 대출 신청과 관련하여 기록되기 때문에 음수가 된다. 이러한 통계치를 년 단위로 보려면 -1로 나누어 1년 내 일수로 나누면 된다.


```python
(app_train['DAYS_BIRTH'] / -365).describe()
```




    count    307511.000000
    mean         43.936973
    std          11.956133
    min          20.517808
    25%          34.008219
    50%          43.150685
    75%          53.923288
    max          69.120548
    Name: DAYS_BIRTH, dtype: float64



그 나이들은 합리적으로 보인다. 높은 쪽이든 낮은 쪽이든 나이에 대한 특이치는 없다.


```python
app_train['DAYS_EMPLOYED'].describe()
```




    count    307511.000000
    mean      63815.045904
    std      141275.766519
    min      -17912.000000
    25%       -2760.000000
    50%       -1213.000000
    75%        -289.000000
    max      365243.000000
    Name: DAYS_EMPLOYED, dtype: float64



그건 옳지 않아! 최대값(긍정적인 것 외에)은 약 1000년


```python
app_train['DAYS_EMPLOYED'].plot.hist(title = 'Days Employment Histogram');
plt.xlabel('Days Employment');
```


![png](/images/home_credit_default_risk/output_46_0.png)


그냥 궁금해서 변칙적인 고객들을 부분집합해서 나머지 고객들보다 채무불이행 비율이 더 높은지 낮은지 살펴보자.


```python
anom = app_train[app_train['DAYS_EMPLOYED'] == 365243]
non_anom = app_train[app_train['DAYS_EMPLOYED'] != 365243]
print('The non-anomalies default on %0.2f%% of loans' % (100 * non_anom['TARGET'].mean()))
print('The anomalies default on %0.2f%% of loans' % (100 * anom['TARGET'].mean()))
print('There are %d anomalous days of employment' % len(anom))
```

    The non-anomalies default on 8.66% of loans
    The anomalies default on 5.40% of loans
    There are 55374 anomalous days of employment
    

이상 징후는 채무불이행 비율이 낮은 것으로 나타났다.

이상 징후를 다루는 것은 정해진 규칙 없이 정확한 상황에 따라 달라진다. 가장 안전한 방법 중 하나는 기계의 학습 전에 이상 징후를 결측값으로 설정한 다음 (귀책 사용) 입력하는 것이다. 이 경우 모든 이상 징후가 정확히 동일한 가치를 가지기 때문에 이러한 모든 대출이 공통적으로 공유될 경우에 대비하여 동일한 가치로 기입하고자 한다. 변칙적인 값들은 어느 정도 중요한 것 같아, 만약 우리가 실제로 이 값을 채웠다면 우리는 기계 학습 모델을 말해주고 싶다. 해결책으로 숫자(np.nan)가 아닌 변칙값으로 채운 다음 변칙값의 변칙 여부를 나타내는 부울란을 새로 만들겠다.


```python
# 변칙적인 플래그 열 생성
app_train['DAYS_EMPLOYED_ANOM'] = app_train["DAYS_EMPLOYED"] == 365243

# 변칙적인 값은 nan으로 대체
app_train['DAYS_EMPLOYED'].replace({365243: np.nan}, inplace = True)

app_train['DAYS_EMPLOYED'].plot.hist(title = 'Days Employment Histogram');
plt.xlabel('Days Employment');
```


![png](/images/home_credit_default_risk/output_50_0.png)


분포는 우리가 예상할 수 있는 것과 훨씬 일치하는 것으로 보이며, 우리는 또한 모형에 이 값들이 원래 변칙적이라는 것을 알리기 위해 새로운 열을 만들었다. (왜냐하면 우리는 일부 값, 아마도 열의 중간값으로 난을 채워야 할 것이기 때문이다.) 데이터 프레임에 Days가 있는 다른 열은 명백한 특이치가 없는 것으로 우리가 기대하는 것에 대한 것으로 보인다.

매우 중요한 사항으로서, 교육 데이터에 대해 수행하는 모든 작업은 테스트 데이터에도 적용되어야 한다. 반드시 새 열을 만들고 기존 열을 테스트 데이터에 np.nan으로 채우자.          


```python
app_test['DAYS_EMPLOYED_ANOM'] = app_test["DAYS_EMPLOYED"] == 365243
app_test["DAYS_EMPLOYED"].replace({365243: np.nan}, inplace = True)

print('There are %d anomalies in the test data out of %d entries' % (app_test["DAYS_EMPLOYED_ANOM"].sum(), len(app_test)))
```

    There are 9274 anomalies in the test data out of 48744 entries
    

상관 관계
이제 범주형 변수와 특이치를 다루었으므로 EDA를 계속 진행합시다. 데이터를 이해하고 이해하는 한 가지 방법은 피쳐와 대상 간의 상관 관계를 찾는 것이다. 우리는 .corr 데이터프레임 방법을 사용하여 모든 변수와 목표값 사이의 Pearson 상관 계수를 계산할 수 있다.

상관 계수는 형상의 "관련성"을 나타내는 가장 큰 방법은 아니지만, 데이터 내에서 가능한 관계에 대한 아이디어를 제공한다. 상관관계의 절대값에 대한 일반적인 해석은 다음과 같다.

- .00-19 "매우 약함"
- .20-.39 "weak"
- .40-.59 "moderate"
- .60-.79 "강력"
- .80-1.0 "매우 강함"


```python
# 대상과의 상관관계를 찾아 정렬
correlations = app_train.corr()['TARGET'].sort_values()

# 상관관계 표시
print('Most Positive Correlations:\n', correlations.tail(15))
print('\nMost Negative Correlations:\n', correlations.head(15))
```

    Most Positive Correlations:
     OCCUPATION_TYPE_Laborers                             0.043019
    FLAG_DOCUMENT_3                                      0.044346
    REG_CITY_NOT_LIVE_CITY                               0.044395
    FLAG_EMP_PHONE                                       0.045982
    NAME_EDUCATION_TYPE_Secondary / secondary special    0.049824
    REG_CITY_NOT_WORK_CITY                               0.050994
    DAYS_ID_PUBLISH                                      0.051457
    CODE_GENDER_M                                        0.054713
    DAYS_LAST_PHONE_CHANGE                               0.055218
    NAME_INCOME_TYPE_Working                             0.057481
    REGION_RATING_CLIENT                                 0.058899
    REGION_RATING_CLIENT_W_CITY                          0.060893
    DAYS_EMPLOYED                                        0.074958
    DAYS_BIRTH                                           0.078239
    TARGET                                               1.000000
    Name: TARGET, dtype: float64
    
    Most Negative Correlations:
     EXT_SOURCE_3                           -0.178919
    EXT_SOURCE_2                           -0.160472
    EXT_SOURCE_1                           -0.155317
    NAME_EDUCATION_TYPE_Higher education   -0.056593
    CODE_GENDER_F                          -0.054704
    NAME_INCOME_TYPE_Pensioner             -0.046209
    DAYS_EMPLOYED_ANOM                     -0.045987
    ORGANIZATION_TYPE_XNA                  -0.045987
    FLOORSMAX_AVG                          -0.044003
    FLOORSMAX_MEDI                         -0.043768
    FLOORSMAX_MODE                         -0.043226
    EMERGENCYSTATE_MODE_No                 -0.042201
    HOUSETYPE_MODE_block of flats          -0.040594
    AMT_GOODS_PRICE                        -0.039645
    REGION_POPULATION_RELATIVE             -0.037227
    Name: TARGET, dtype: float64
    

더 중요한 상관관계 몇 가지를 살펴봅시다: DAYS_BOYT는 가장 긍정적인 상관관계 입니다. (변수와 그 자체와의 상관관계가 항상 1이기 때문에 TARGET은 제외) 문서를 보면 Days_BOYT는 마이너스일(어떠한 이유로든!) 대출 당시 고객의 일(일) 연령이다. 상관관계는 양수지만, 이 특성의 값은 실제로 음수인데, 이는 클라이언트가 나이가 들수록 대출금 채무불이행(대상 == 0) 가능성이 적다는 것을 의미한다. 그건 좀 헷갈리니까 형상의 절대값을 취해서 그 다음에 상관관계는 음수가 될 겁니다.

### 상환연령이 상환에 미치는 영향



```python
# 출생 후 양일간과 대상의 상관관계 찾기
app_train['DAYS_BIRTH'] = abs(app_train['DAYS_BIRTH'])
app_train['DAYS_BIRTH'].corr(app_train['TARGET'])
```




    -0.07823930830982694



고객이 나이가 들수록 고객이 나이가 들수록 대출금을 제때 상환하는 경향이 있다는 목표와 부정적인 선형 관계가 형성된다.

이 변수부터 살펴보자. 첫째, 우리는 시대의 히스토그램을 만들 수 있다. 우리는 그 줄거리를 좀 더 이해할 수 있도록 몇 년 안에 x축을 넣을 것이다.


```python
# 플롯 스타일 설정
plt.style.use('fivethirtyeight')

# 연령별 연령 분포 그림 그리기
plt.hist(app_train['DAYS_BIRTH'] / 365, edgecolor = 'k', bins = 25)
plt.title('Age of Client'); plt.xlabel('Age (years)'); plt.ylabel('Count');
```


![png](/images/home_credit_default_risk/output_59_0.png)


그 자체로 연령의 분포는 모든 연령대가 합리적이기 때문에 특이치가 없다는 것 이외에는 우리에게 별로 알려주지 않는다. 연령대가 대상에 미치는 영향을 시각화하기 위해 다음으로 대상의 값으로 색칠한 KDE(커널 밀도 추정도)를 만들겠다. 커널 밀도 추정 그림은 단일 변수의 분포를 보여주며 평활 히스토그램으로 생각할 수 있다(대개 가우스인 커널을 각 데이터 지점에서 계산한 다음 모든 개별 커널을 평균하여 단일 평활 곡선을 개발함으로써 생성된다). 우리는 이 그래프에 해저 Kdeplot을 사용할 것이다.


```python
plt.figure(figsize = (10, 8))

# 제때 상환된 대출의 KDE 플롯
sns.kdeplot(app_train.loc[app_train['TARGET'] == 0, 'DAYS_BIRTH'] / 365, label = 'target == 0')

# 제때 상환되지 않은 대출의 KDE 플롯
sns.kdeplot(app_train.loc[app_train['TARGET'] == 1, 'DAYS_BIRTH'] / 365, label = 'target == 1')

# 플롯의 라벨링
plt.xlabel('Age (years)'); plt.ylabel('Density'); plt.title('Distribution of Ages');
```


![png](/images/home_credit_default_risk/output_61_0.png)


목표 == 1 커브가 범위의 젊은 쪽 끝을 향해 기울어진다. 이는 유의미한 상관 계수(-0.07 상관 계수)는 아니지만, 이 변수는 대상에 영향을 미치기 때문에 머신러닝 모델에서 유용할 것으로 보인다. 이 관계를 다른 방식으로 보자: 평균적으로 연령대별 대출금 상환 실패.

이 그래프를 만들기 위해 먼저 나이 범주를 각각 5년씩의 빈으로 자른다. 그런 다음 각 빈에 대해 대상의 평균가치를 산출하는데, 이는 각 연령 범주별로 상환되지 않은 대출의 비율을 알려준다.
