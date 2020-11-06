---
title: titanic
---

# Kaggle API 설치
- Google Colab에서 Kaggle API를 불러오려면 다음 소스코드를 실행한다.


```python
!pip install kaggle
```

    Requirement already satisfied: kaggle in /usr/local/lib/python3.6/dist-packages (1.5.9)
    Requirement already satisfied: six>=1.10 in /usr/local/lib/python3.6/dist-packages (from kaggle) (1.15.0)
    Requirement already satisfied: urllib3 in /usr/local/lib/python3.6/dist-packages (from kaggle) (1.24.3)
    Requirement already satisfied: slugify in /usr/local/lib/python3.6/dist-packages (from kaggle) (0.0.1)
    Requirement already satisfied: python-dateutil in /usr/local/lib/python3.6/dist-packages (from kaggle) (2.8.1)
    Requirement already satisfied: tqdm in /usr/local/lib/python3.6/dist-packages (from kaggle) (4.41.1)
    Requirement already satisfied: python-slugify in /usr/local/lib/python3.6/dist-packages (from kaggle) (4.0.1)
    Requirement already satisfied: requests in /usr/local/lib/python3.6/dist-packages (from kaggle) (2.23.0)
    Requirement already satisfied: certifi in /usr/local/lib/python3.6/dist-packages (from kaggle) (2020.6.20)
    Requirement already satisfied: text-unidecode>=1.3 in /usr/local/lib/python3.6/dist-packages (from python-slugify->kaggle) (1.3)
    Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.6/dist-packages (from requests->kaggle) (3.0.4)
    Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.6/dist-packages (from requests->kaggle) (2.10)
    

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



<input type="file" id="files-efff3ea8-bcea-47b8-a2af-e515eebd283e" name="files[]" multiple disabled
   style="border:none" />
<output id="result-efff3ea8-bcea-47b8-a2af-e515eebd283e">
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
    


```python

```

## 2. Kaggle 데이터 불러오기
- 먼저 kaggle competition list를 불러온다.


```python
!kaggle competitions list
```

    Warning: Looks like you're using an outdated API Version, please consider updating (server 1.5.9 / client 1.5.4)
    ref                                            deadline             category            reward  teamCount  userHasEntered  
    ---------------------------------------------  -------------------  ---------------  ---------  ---------  --------------  
    contradictory-my-dear-watson                   2030-07-01 23:59:00  Getting Started     Prizes        134           False  
    gan-getting-started                            2030-07-01 23:59:00  Getting Started     Prizes        185           False  
    tpu-getting-started                            2030-06-03 23:59:00  Getting Started  Knowledge        315           False  
    digit-recognizer                               2030-01-01 00:00:00  Getting Started  Knowledge       2356           False  
    titanic                                        2030-01-01 00:00:00  Getting Started  Knowledge      18058            True  
    house-prices-advanced-regression-techniques    2030-01-01 00:00:00  Getting Started  Knowledge       4536            True  
    connectx                                       2030-01-01 00:00:00  Getting Started  Knowledge        390           False  
    nlp-getting-started                            2030-01-01 00:00:00  Getting Started  Knowledge       1184           False  
    rock-paper-scissors                            2021-02-01 23:59:00  Playground          Prizes        152           False  
    riiid-test-answer-prediction                   2021-01-07 23:59:00  Featured          $100,000       1466           False  
    nfl-big-data-bowl-2021                         2021-01-05 23:59:00  Analytics         $100,000          0           False  
    competitive-data-science-predict-future-sales  2020-12-31 23:59:00  Playground           Kudos       9343           False  
    halite-iv-playground-edition                   2020-12-31 23:59:00  Playground       Knowledge         43           False  
    predict-volcanic-eruptions-ingv-oe             2020-12-28 23:59:00  Playground            Swag        193           False  
    hashcode-drone-delivery                        2020-12-14 23:59:00  Playground       Knowledge         79           False  
    cdp-unlocking-climate-solutions                2020-12-02 23:59:00  Analytics          $91,000          0           False  
    lish-moa                                       2020-11-30 23:59:00  Research           $30,000       3395           False  
    google-football                                2020-11-30 23:59:00  Featured            $6,000        916           False  
    conways-reverse-game-of-life-2020              2020-11-30 23:59:00  Playground            Swag        131           False  
    lyft-motion-prediction-autonomous-vehicles     2020-11-25 23:59:00  Featured           $30,000        778           False  
    


```python
!kaggle competitions download -c titanic  
```

    Warning: Looks like you're using an outdated API Version, please consider updating (server 1.5.9 / client 1.5.4)
    Downloading gender_submission.csv to /content
      0% 0.00/3.18k [00:00<?, ?B/s]
    100% 3.18k/3.18k [00:00<00:00, 6.86MB/s]
    Downloading test.csv to /content
      0% 0.00/28.0k [00:00<?, ?B/s]
    100% 28.0k/28.0k [00:00<00:00, 23.4MB/s]
    Downloading train.csv to /content
      0% 0.00/59.8k [00:00<?, ?B/s]
    100% 59.8k/59.8k [00:00<00:00, 52.2MB/s]
    

- ls는 디렉터리(파일,경로) 내의 데이터 파일을 보여주는 명령어


```python
!ls
```

    gender_submission.csv  sample_data  test.csv  train.csv
    

- 현재 총 4개의 데이터를 다운로드 받았다. 
  + gender_submission.csv
  + sample_data
  + test.csv
  + train.csv

## 3. 캐글 데이터 수집 및 EDA 
- 우선 데이터를 수집하기에 앞서서 `EDA`에 관한 필수 패키지를 설치하자. 


```python
import pandas as pd # 데이터 가공 변환(deploy)
import pandas_profiling # 보고서 기능 
import numpy as np # 수치연산 & 배열 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
from IPython.core.display import display, HTML
```

### (1) 데이터 불러오기
- 지난 시간에 받은 데이터가 총 4개임을 확인했다.
  + gender_submission.csv
  + sample_data
  + test.csv
  + train.csv
- 여기에서는 우선 `test.csv` & `train.csv` 파일을 받도록 한다. 


```python
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print("data import is done")
```

    data import is done
    

### (2) 데이터 확인
- `Kaggle` 데이터를 불러오면 우선 확인해야 하는 것은 데이터셋의 크기다. 
  + 변수의 갯수
  + Numeric 변수 & Categorical 변수의 개수 등을 파악해야 한다.
- Point 1 - `train`데이터에서 굳이 훈련데이터와 테스트 데이터를 구분할 필요는 없다. 
  + 보통 `Kaggle`에서는 테스트 데이터를 주기적으로 업데이트 해준다.
- Point 2 - 보통 `test` 데이터의 변수의 개수가 하나 더 작다. 



```python
train.shape, test.shape
```




    ((891, 12), (418, 11))



- 그 후 `train`데이터의 `상위 5개`의 데이터만 확인한다. 


```python
display(train.head())
```



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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>


아래 코드는 train.csv을 data로 변환 한다.


```python
data=pd.read_csv('train.csv')
```


```python
data.head()
```




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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.isnull().sum()
```




    PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age            177
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    dtype: int64



The Age, Cabin and Embarked 에 대한 결측값을 구한다.

## 얼마나 살아남았나?


```python
f,ax=plt.subplots(1,2,figsize=(18,8))
data['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot('Survived',data=data,ax=ax[1])
ax[1].set_title('Survived')
plt.show()
```


![png](/images/titanic/output_27_0.png)


그 사고에서 살아남은 승객이 많지 않다는 것은 명백하다.

훈련장 891명 중 350명 정도만 살아남았다. 즉, 전체 훈련장 중 38.4%만이 추락사고에서 살아남았다. 우리는 데이터로부터 더 나은 통찰력을 얻고 어떤 범주의 승객들이 살아남았는지 그리고 누가 살아남지 않았는지 보기 위해 더 많은 정보를 캐내야 한다.

우리는 데이터 세트의 다른 특징들을 사용하여 생존율을 확인하도록 노력할 것이다. Sex, Port Of Embarcation, Age 등이 특징이다.

먼저 다양한 유형의 특징을 이해하십시오.

피쳐 유형
- 범주형 피쳐:
범주형 변수는 두 개 이상의 범주를 가진 변수 중 하나이며, 해당 형상의 각 값은 범주별로 분류할 수 있다.예를 들어, 성별은 두 개의 범주(남성과 여성)를 갖는 범주형 변수다. 이제 우리는 그러한 변수들에 대해 어떠한 순서도 정렬할 수 없다. 이 변수들은 공칭 변수라고도 한다.

 + 데이터 집합의 범주형 특징: 성별, 도착.

- 순서형 피쳐:
순서형 변수는 범주형 값과 비슷하지만, 그 값들 사이의 차이는 우리가 상대적인 순서나 값들 사이의 정렬을 가질 수 있다는 것이다. 예를 들어: 높이에 높은 값, 중간 값, 짧은 값과 같은 특징이 있다면 높이는 서수 변수다. 여기서 우리는 변수에서 상대적인 분류법을 가질 수 있다.

 + 데이터 집합의 순서형 기능: PClass

- 연속 기능:
형상은 형상 열의 두 점 또는 최소값 또는 최대값 사이에 값을 취할 수 있는 경우 지속된다고 한다.

 + 데이터 집합의 지속적인 기능: 나이


### 특성 분석  
성--> 범주형 특징


```python
data.groupby(['Sex','Survived'])['Survived'].count()
```




    Sex     Survived
    female  0            81
            1           233
    male    0           468
            1           109
    Name: Survived, dtype: int64




```python
f,ax=plt.subplots(1,2,figsize=(18,8))
data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar(ax=ax[0])
ax[0].set_title('Survived vs Sex')
sns.countplot('Sex',hue='Survived',data=data,ax=ax[1])
ax[1].set_title('Sex:Survived vs Dead')
plt.show()
```


![png](/images/titanic/output_32_0.png)


배에 타고 있는 남자들의 수가 여자들의 수보다 훨씬 많다. 그러나 여전히 구조된 여성의 수는 구조된 남성의 수보다 거의 두 배나 많다. 배에 타고 있는 여성의 생존율은 약 75%인 반면 남성은 약 18-19%이다.

이것은 모델링을 위해 매우 중요한 특징으로 보인다. 하지만 그게 최고일까? 다른 기능을 확인해 봅시다.

### Pclass --> 순서형 피쳐


```python
pd.crosstab(data.Pclass,data.Survived,margins=True).style.background_gradient(cmap='summer_r')
```



<div style = overflow:scroll;>
<style  type="text/css" >
#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row0_col0,#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row1_col1,#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row1_col2{
            background-color:  #ffff66;
            color:  #000000;
        }#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row0_col1{
            background-color:  #cee666;
            color:  #000000;
        }#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row0_col2{
            background-color:  #f4fa66;
            color:  #000000;
        }#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row1_col0{
            background-color:  #f6fa66;
            color:  #000000;
        }#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row2_col0{
            background-color:  #60b066;
            color:  #000000;
        }#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row2_col1{
            background-color:  #dfef66;
            color:  #000000;
        }#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row2_col2{
            background-color:  #90c866;
            color:  #000000;
        }#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row3_col0,#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row3_col1,#T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row3_col2{
            background-color:  #008066;
            color:  #f1f1f1;
        }</style><table id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002" ><thead>    <tr>        <th class="index_name level0" >Survived</th>        <th class="col_heading level0 col0" >0</th>        <th class="col_heading level0 col1" >1</th>        <th class="col_heading level0 col2" >All</th>    </tr>    <tr>        <th class="index_name level0" >Pclass</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002level0_row0" class="row_heading level0 row0" >1</th>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row0_col0" class="data row0 col0" >80</td>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row0_col1" class="data row0 col1" >136</td>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row0_col2" class="data row0 col2" >216</td>
            </tr>
            <tr>
                        <th id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002level0_row1" class="row_heading level0 row1" >2</th>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row1_col0" class="data row1 col0" >97</td>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row1_col1" class="data row1 col1" >87</td>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row1_col2" class="data row1 col2" >184</td>
            </tr>
            <tr>
                        <th id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002level0_row2" class="row_heading level0 row2" >3</th>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row2_col0" class="data row2 col0" >372</td>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row2_col1" class="data row2 col1" >119</td>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row2_col2" class="data row2 col2" >491</td>
            </tr>
            <tr>
                        <th id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002level0_row3" class="row_heading level0 row3" >All</th>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row3_col0" class="data row3 col0" >549</td>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row3_col1" class="data row3 col1" >342</td>
                        <td id="T_ceb04e82_1e4a_11eb_b25f_0242ac1c0002row3_col2" class="data row3 col2" >891</td>
            </tr>
    </tbody></table>




```python
f,ax=plt.subplots(1,2,figsize=(18,8))
data['Pclass'].value_counts().plot.bar(color=['#CD7F32','#FFDF00','#D3D3D3'],ax=ax[0])
ax[0].set_title('Number Of Passengers By Pclass')
ax[0].set_ylabel('Count')
sns.countplot('Pclass',hue='Survived',data=data,ax=ax[1])
ax[1].set_title('Pclass:Survived vs Dead')
plt.show()
```


![png](/images/titanic/output_36_0.png)


P클래스사람은 돈이 모든 것을 살 수 없다고 말한다. 그러나 우리는 구조하는 동안 P클래스 1의 승객이 매우 높은 우선순위를 부여받았다는 것을 분명히 알 수 있다. P클래스 3의 탑승객 수가 훨씬 더 많았지만, 여전히 탑승객들로부터 생존하는 사람들의 수는 약 25%로 매우 낮다.

P클래스의 경우 1% 생존율이 약 63%인 반면 P클래스2의 경우 약 48%이다. 그래서 돈과 지위가 중요하다. 그런 물질적인 세계.

좀 더 자세히 살펴보고 다른 흥미로운 관찰을 확인해 봅시다. 성과 P클래스 통해 생존율을 확인해보자.


```python
pd.crosstab([data.Sex,data.Survived],data.Pclass,margins=True).style.background_gradient(cmap='summer_r')
```



<div style = overflow:scroll;>
<style  type="text/css" >
#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row0_col0,#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row0_col1,#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row0_col3,#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row3_col2{
            background-color:  #ffff66;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row0_col2,#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row1_col2{
            background-color:  #f1f866;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row1_col0{
            background-color:  #96cb66;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row1_col1{
            background-color:  #a3d166;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row1_col3{
            background-color:  #cfe766;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row2_col0{
            background-color:  #a7d366;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row2_col1,#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row2_col3{
            background-color:  #85c266;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row2_col2{
            background-color:  #6eb666;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row3_col0{
            background-color:  #cde666;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row3_col1{
            background-color:  #f0f866;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row3_col3{
            background-color:  #f7fb66;
            color:  #000000;
        }#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row4_col0,#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row4_col1,#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row4_col2,#T_2327443c_1e4d_11eb_b25f_0242ac1c0002row4_col3{
            background-color:  #008066;
            color:  #f1f1f1;
        }</style><table id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002" ><thead>    <tr>        <th class="blank" ></th>        <th class="index_name level0" >Pclass</th>        <th class="col_heading level0 col0" >1</th>        <th class="col_heading level0 col1" >2</th>        <th class="col_heading level0 col2" >3</th>        <th class="col_heading level0 col3" >All</th>    </tr>    <tr>        <th class="index_name level0" >Sex</th>        <th class="index_name level1" >Survived</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002level0_row0" class="row_heading level0 row0" rowspan=2>female</th>
                        <th id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002level1_row0" class="row_heading level1 row0" >0</th>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row0_col0" class="data row0 col0" >3</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row0_col1" class="data row0 col1" >6</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row0_col2" class="data row0 col2" >72</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row0_col3" class="data row0 col3" >81</td>
            </tr>
            <tr>
                                <th id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002level1_row1" class="row_heading level1 row1" >1</th>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row1_col0" class="data row1 col0" >91</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row1_col1" class="data row1 col1" >70</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row1_col2" class="data row1 col2" >72</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row1_col3" class="data row1 col3" >233</td>
            </tr>
            <tr>
                        <th id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002level0_row2" class="row_heading level0 row2" rowspan=2>male</th>
                        <th id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002level1_row2" class="row_heading level1 row2" >0</th>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row2_col0" class="data row2 col0" >77</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row2_col1" class="data row2 col1" >91</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row2_col2" class="data row2 col2" >300</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row2_col3" class="data row2 col3" >468</td>
            </tr>
            <tr>
                                <th id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002level1_row3" class="row_heading level1 row3" >1</th>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row3_col0" class="data row3 col0" >45</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row3_col1" class="data row3 col1" >17</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row3_col2" class="data row3 col2" >47</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row3_col3" class="data row3 col3" >109</td>
            </tr>
            <tr>
                        <th id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002level0_row4" class="row_heading level0 row4" >All</th>
                        <th id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002level1_row4" class="row_heading level1 row4" ></th>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row4_col0" class="data row4 col0" >216</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row4_col1" class="data row4 col1" >184</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row4_col2" class="data row4 col2" >491</td>
                        <td id="T_2327443c_1e4d_11eb_b25f_0242ac1c0002row4_col3" class="data row4 col3" >891</td>
            </tr>
    </tbody></table>




```python
sns.factorplot('Pclass','Survived',hue='Sex',data=data) #성에 따른 Pclass 생존율
plt.show()
```


![png](/images/titanic/output_39_0.png)


이 경우 요인 그림은 범주형 값의 분리가 쉽기 때문에 요인 그림을 사용한다.

크로스탭과 인자 플롯을 보면 Pclass1 여성 94명 중 3명만이 사망했기 때문에 Pclass1 여성 생존율이 약 95~96%라고 쉽게 유추할 수 있다.

Pclass와 관계 없이 구조하는 동안 여성에게 우선권이 주어졌다는 것은 명백하다. 심지어 Pclass1 출신의 남성들도 생존율이 매우 낮다.

Pclass도 중요한 특징인 것 같다. 다른 특징을 분석해보자.

### 나이 --> 지속적 특징


```python
print('Oldest Passenger was of:',data['Age'].max(),'Years') #최대 나이 승객
print('Youngest Passenger was of:',data['Age'].min(),'Years') #최소 나이 승객 
print('Average Age on the ship:',data['Age'].mean(),'Years') #평균 나이 승객
```

    Oldest Passenger was of: 80.0 Years
    Youngest Passenger was of: 0.42 Years
    Average Age on the ship: 29.69911764705882 Years
    


```python
f,ax=plt.subplots(1,2,figsize=(18,8))
sns.violinplot("Pclass","Age", hue="Survived", data=data,split=True,ax=ax[0])
ax[0].set_title('Pclass and Age vs Survived') #제목
ax[0].set_yticks(range(0,110,10)) 
sns.violinplot("Sex","Age", hue="Survived", data=data,split=True,ax=ax[1])
ax[1].set_title('Sex and Age vs Survived') #제목
ax[1].set_yticks(range(0,110,10))
plt.show()
```


![png](/images/titanic/output_43_0.png)


관측치:
1)P클래스에 따라 자녀 수가 증가하고 10세 미만(즉, 자녀)의 패시네거 생존율은 P클래스에 관계없이 양호한 것으로 보인다.

2)Pclass1에서 20-50세의 승객의 생존 가능성은 높고 여성에게는 더욱 좋다.

3)남성의 경우 나이가 들수록 생존 가능성이 줄어든다.

앞에서 보았듯이 에이지 기능은 177개의 null 값을 가지고 있다. 이러한 NaN 값을 대체하기 위해 데이터 집합의 평균 연령을 할당할 수 있다.

그런데 문제는 나이 차이가 많은 사람들이 많았다는 겁니다. 우리는 단지 평균 나이 29세인 4살 아이를 배정할 수 없다. 승객이 어떤 연령대인지 알 수 있는 방법은 없을까?

이름 기능을 확인할 수 있어. 그 특징을 살펴보면, 우리는 그 이름들이 Mr. 또는 Mrs.와 같은 경례를 가지고 있다는 것을 알 수 있다. 따라서 우리는 Mr. Mrs와 Mrs의 평균값을 각 그룹에 할당할 수 있다.

### ''이름에 무엇이 있는가?"---> 특징 :p


```python
data['Initial']=0
for i in data:
    data['Initial']=data.Name.str.extract('([A-Za-z]+)\.') #인사말을 꺼내자.
```

자, 이제 Regex를 사용합시다. [A-Za-z]+).. 즉, A-Z 또는 a-z 사이에 있는 문자열을 찾고, 그 뒤에 .(점)이 있는 문자열을 찾는 겁니다. 그래서 우리는 이름에서 이니셜을 성공적으로 추출했다.


```python
pd.crosstab(data.Initial,data.Sex).T.style.background_gradient(cmap='summer_r') #성으로 이니셜 확인
```



<div style = overflow:scroll;>
<style  type="text/css" >
#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col0,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col1,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col3,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col4,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col5,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col7,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col8,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col12,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col15,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col16,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col2,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col6,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col9,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col10,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col11,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col13,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col14{
            background-color:  #ffff66;
            color:  #000000;
        }#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col2,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col6,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col9,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col10,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col11,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col13,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col14,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col0,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col1,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col3,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col4,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col5,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col7,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col8,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col12,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col15,#T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col16{
            background-color:  #008066;
            color:  #f1f1f1;
        }</style><table id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002" ><thead>    <tr>        <th class="index_name level0" >Initial</th>        <th class="col_heading level0 col0" >Capt</th>        <th class="col_heading level0 col1" >Col</th>        <th class="col_heading level0 col2" >Countess</th>        <th class="col_heading level0 col3" >Don</th>        <th class="col_heading level0 col4" >Dr</th>        <th class="col_heading level0 col5" >Jonkheer</th>        <th class="col_heading level0 col6" >Lady</th>        <th class="col_heading level0 col7" >Major</th>        <th class="col_heading level0 col8" >Master</th>        <th class="col_heading level0 col9" >Miss</th>        <th class="col_heading level0 col10" >Mlle</th>        <th class="col_heading level0 col11" >Mme</th>        <th class="col_heading level0 col12" >Mr</th>        <th class="col_heading level0 col13" >Mrs</th>        <th class="col_heading level0 col14" >Ms</th>        <th class="col_heading level0 col15" >Rev</th>        <th class="col_heading level0 col16" >Sir</th>    </tr>    <tr>        <th class="index_name level0" >Sex</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002level0_row0" class="row_heading level0 row0" >female</th>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col0" class="data row0 col0" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col1" class="data row0 col1" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col2" class="data row0 col2" >1</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col3" class="data row0 col3" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col4" class="data row0 col4" >1</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col5" class="data row0 col5" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col6" class="data row0 col6" >1</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col7" class="data row0 col7" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col8" class="data row0 col8" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col9" class="data row0 col9" >182</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col10" class="data row0 col10" >2</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col11" class="data row0 col11" >1</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col12" class="data row0 col12" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col13" class="data row0 col13" >125</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col14" class="data row0 col14" >1</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col15" class="data row0 col15" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row0_col16" class="data row0 col16" >0</td>
            </tr>
            <tr>
                        <th id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002level0_row1" class="row_heading level0 row1" >male</th>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col0" class="data row1 col0" >1</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col1" class="data row1 col1" >2</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col2" class="data row1 col2" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col3" class="data row1 col3" >1</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col4" class="data row1 col4" >6</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col5" class="data row1 col5" >1</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col6" class="data row1 col6" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col7" class="data row1 col7" >2</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col8" class="data row1 col8" >40</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col9" class="data row1 col9" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col10" class="data row1 col10" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col11" class="data row1 col11" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col12" class="data row1 col12" >517</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col13" class="data row1 col13" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col14" class="data row1 col14" >0</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col15" class="data row1 col15" >6</td>
                        <td id="T_392ab74e_1e4f_11eb_b25f_0242ac1c0002row1_col16" class="data row1 col16" >1</td>
            </tr>
    </tbody></table>



좋아, Mlle이나 Mme와 같은 철자가 틀린 이니셜이 있는데 Miss를 나타낸다. 나는 그것들을 미스나 다른 가치에 대해서도 같은 것으로 대체할 것이다.   
아래 코드 참조


```python
data['Initial'].replace(['Mlle','Mme','Ms','Dr','Major','Lady','Countess','Jonkheer','Col','Rev','Capt','Sir','Don'],['Miss','Miss','Miss','Mr','Mr','Mrs','Mrs','Other','Other','Other','Mr','Mr','Mr'],inplace=True)
```


```python
data.groupby('Initial')['Age'].mean() #이니셜별 평균 연령 확인
```




    Initial
    Master     4.574167
    Miss      21.860000
    Mr        32.739609
    Mrs       35.981818
    Other     45.888889
    Name: Age, dtype: float64



NaN 연령 채우기


```python
## 평균 연령의 Ceil 값에 NaN 값 할당
data.loc[(data.Age.isnull())&(data.Initial=='Mr'),'Age']=33
data.loc[(data.Age.isnull())&(data.Initial=='Mrs'),'Age']=36
data.loc[(data.Age.isnull())&(data.Initial=='Master'),'Age']=5
data.loc[(data.Age.isnull())&(data.Initial=='Miss'),'Age']=22
data.loc[(data.Age.isnull())&(data.Initial=='Other'),'Age']=46
```


```python
data.Age.isnull().any() #그래서 마침내 null 값이 남지 않게 되었다.
```




    False




```python
f,ax=plt.subplots(1,2,figsize=(20,10))
data[data['Survived']==0].Age.plot.hist(ax=ax[0],bins=20,edgecolor='black',color='red')
ax[0].set_title('Survived= 0')
x1=list(range(0,85,5))
ax[0].set_xticks(x1)
data[data['Survived']==1].Age.plot.hist(ax=ax[1],color='green',bins=20,edgecolor='black')
ax[1].set_title('Survived= 1')
x2=list(range(0,85,5))
ax[1].set_xticks(x2)
plt.show()
```


![png](/images/titanic/output_55_0.png)


관측치:  
1)아기들 (<5)은 대량으로 생존되었다.

2)가장 나이가 많은 승객은 생존했다(80년).

3)최대 사망자는 30~40세였다.


```python
sns.factorplot('Pclass','Survived',col='Initial',data=data)
plt.show()
```


![png](/images/titanic/output_57_0.png)


따라서 부녀자 우선 정책은 계층에 관계없이 적용된다.

### 승선 --> 범주형 값


```python
pd.crosstab([data.Embarked,data.Pclass],[data.Sex,data.Survived],margins=True).style.background_gradient(cmap='summer_r')
```



<div style = overflow:scroll;>
<style  type="text/css" >
#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col0,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col2{
            background-color:  #fcfe66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col1{
            background-color:  #d2e866;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col2{
            background-color:  #f2f866;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col3{
            background-color:  #d8ec66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col4,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col3{
            background-color:  #e8f466;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col0,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col0,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col1,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col2,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col3,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col4,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col0,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col2,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col3,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col4{
            background-color:  #ffff66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col1,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col0{
            background-color:  #f9fc66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col3,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col4{
            background-color:  #fbfd66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col0,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col1{
            background-color:  #e6f266;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col1{
            background-color:  #f0f866;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col2{
            background-color:  #eef666;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col4,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col0{
            background-color:  #edf666;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col1{
            background-color:  #fefe66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col0{
            background-color:  #e3f166;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col2{
            background-color:  #ecf666;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col3{
            background-color:  #f8fc66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col4{
            background-color:  #ebf566;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col1{
            background-color:  #cde666;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col2{
            background-color:  #e4f266;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col3{
            background-color:  #bede66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col4{
            background-color:  #dbed66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col1{
            background-color:  #bdde66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col2{
            background-color:  #d3e966;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col3,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col1{
            background-color:  #dcee66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col4{
            background-color:  #d1e866;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col0{
            background-color:  #52a866;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col2{
            background-color:  #81c066;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col3{
            background-color:  #b0d866;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col4{
            background-color:  #9acc66;
            color:  #000000;
        }#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col0,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col1,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col2,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col3,#T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col4{
            background-color:  #008066;
            color:  #f1f1f1;
        }</style><table id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002" ><thead>    <tr>        <th class="blank" ></th>        <th class="index_name level0" >Sex</th>        <th class="col_heading level0 col0" colspan=2>female</th>        <th class="col_heading level0 col2" colspan=2>male</th>        <th class="col_heading level0 col4" >All</th>    </tr>    <tr>        <th class="blank" ></th>        <th class="index_name level1" >Survived</th>        <th class="col_heading level1 col0" >0</th>        <th class="col_heading level1 col1" >1</th>        <th class="col_heading level1 col2" >0</th>        <th class="col_heading level1 col3" >1</th>        <th class="col_heading level1 col4" ></th>    </tr>    <tr>        <th class="index_name level0" >Embarked</th>        <th class="index_name level1" >Pclass</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level0_row0" class="row_heading level0 row0" rowspan=3>C</th>
                        <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row0" class="row_heading level1 row0" >1</th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col0" class="data row0 col0" >1</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col1" class="data row0 col1" >42</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col2" class="data row0 col2" >25</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col3" class="data row0 col3" >17</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row0_col4" class="data row0 col4" >85</td>
            </tr>
            <tr>
                                <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row1" class="row_heading level1 row1" >2</th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col0" class="data row1 col0" >0</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col1" class="data row1 col1" >7</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col2" class="data row1 col2" >8</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col3" class="data row1 col3" >2</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row1_col4" class="data row1 col4" >17</td>
            </tr>
            <tr>
                                <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row2" class="row_heading level1 row2" >3</th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col0" class="data row2 col0" >8</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col1" class="data row2 col1" >15</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col2" class="data row2 col2" >33</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col3" class="data row2 col3" >10</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row2_col4" class="data row2 col4" >66</td>
            </tr>
            <tr>
                        <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level0_row3" class="row_heading level0 row3" rowspan=3>Q</th>
                        <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row3" class="row_heading level1 row3" >1</th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col0" class="data row3 col0" >0</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col1" class="data row3 col1" >1</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col2" class="data row3 col2" >1</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col3" class="data row3 col3" >0</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row3_col4" class="data row3 col4" >2</td>
            </tr>
            <tr>
                                <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row4" class="row_heading level1 row4" >2</th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col0" class="data row4 col0" >0</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col1" class="data row4 col1" >2</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col2" class="data row4 col2" >1</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col3" class="data row4 col3" >0</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row4_col4" class="data row4 col4" >3</td>
            </tr>
            <tr>
                                <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row5" class="row_heading level1 row5" >3</th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col0" class="data row5 col0" >9</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col1" class="data row5 col1" >24</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col2" class="data row5 col2" >36</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col3" class="data row5 col3" >3</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row5_col4" class="data row5 col4" >72</td>
            </tr>
            <tr>
                        <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level0_row6" class="row_heading level0 row6" rowspan=3>S</th>
                        <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row6" class="row_heading level1 row6" >1</th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col0" class="data row6 col0" >2</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col1" class="data row6 col1" >46</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col2" class="data row6 col2" >51</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col3" class="data row6 col3" >28</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row6_col4" class="data row6 col4" >127</td>
            </tr>
            <tr>
                                <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row7" class="row_heading level1 row7" >2</th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col0" class="data row7 col0" >6</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col1" class="data row7 col1" >61</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col2" class="data row7 col2" >82</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col3" class="data row7 col3" >15</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row7_col4" class="data row7 col4" >164</td>
            </tr>
            <tr>
                                <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row8" class="row_heading level1 row8" >3</th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col0" class="data row8 col0" >55</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col1" class="data row8 col1" >33</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col2" class="data row8 col2" >231</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col3" class="data row8 col3" >34</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row8_col4" class="data row8 col4" >353</td>
            </tr>
            <tr>
                        <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level0_row9" class="row_heading level0 row9" >All</th>
                        <th id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002level1_row9" class="row_heading level1 row9" ></th>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col0" class="data row9 col0" >81</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col1" class="data row9 col1" >231</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col2" class="data row9 col2" >468</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col3" class="data row9 col3" >109</td>
                        <td id="T_40b4596e_1e5b_11eb_b25f_0242ac1c0002row9_col4" class="data row9 col4" >889</td>
            </tr>
    </tbody></table>



항구별 생존 가능성


```python
sns.factorplot('Embarked','Survived',data=data)
fig=plt.gcf()
fig.set_size_inches(5,3)
plt.show()
```


![png](/images/titanic/output_62_0.png)


포트 C의 생존 가능성은 0.55 전후로 가장 높은 반면 S의 생존 가능성은 가장 낮다.


```python
f,ax=plt.subplots(2,2,figsize=(20,15))
sns.countplot('Embarked',data=data,ax=ax[0,0]) #sns = seaborn
ax[0,0].set_title('No. Of Passengers Boarded')
sns.countplot('Embarked',hue='Sex',data=data,ax=ax[0,1])
ax[0,1].set_title('Male-Female Split for Embarked')
sns.countplot('Embarked',hue='Survived',data=data,ax=ax[1,0])
ax[1,0].set_title('Embarked vs Survived')
sns.countplot('Embarked',hue='Pclass',data=data,ax=ax[1,1])
ax[1,1].set_title('Embarked vs Pclass')
plt.subplots_adjust(wspace=0.2,hspace=0.5)
plt.show()
```


![png](/images/titanic/output_64_0.png)


관측치:
1)S에서 탑승한 최대 탑승객. 그들 대부분은 Pclass3 출신이다.

2)C에서 온 승객들은 상당부분 살아남은 것으로 보아 운이 좋은 것으로 보인다. 그 이유는 아마도 모든 Pclass1과 Pclass2 승객을 구조했을 것이다.

3)승객 S는 부자들의 대다수가 탑승한 항구를 바라본다. 여전히 생존 가능성은 낮은데, 그것은 81% 정도 되는 Pclass3의 많은 승객들이 살아남지금은 Pclass3의 많은 승객들이 살아남지 못했기 때문이다.

4)항구 Q의 탑승객은 거의 95%가 Pclass3 출신이었다.


```python
sns.factorplot('Pclass','Survived',hue='Sex',col='Embarked',data=data)
plt.show()
```


![png](/images/titanic/output_66_0.png)


관측치:
1)Pclass1과 Pclass2의 여성은 Pclass와 관계없이 생존 확률은 거의 1이다.

2)남녀 모두의 생존율이 매우 낮기 때문에 Pclass3 Passenger에게는 포트S가 매우 불행해 보인다.(돈 문제)

3)포트 Q는 거의 모두가 Pclass 3에서 온 것처럼 남자에게는 가장 어울리지 않는 것 같다.

채우기 시작 NaN  
우리는 최대 승객들이 S항에서 탑승하는 것을 보았듯이 NaN을 S로 대체한다.


```python
data['Embarked'].fillna('S',inplace=True)
```


```python
data.Embarked.isnull().any()# Finally No NaN values
```




    False



### SibSip-->구체적 특징
이 특징은 사람이 혼자 있는지 가족과 함께 있는지 여부를 나타낸다.

형제 = 형제, 자매, 의붓동생, 의붓동생, 의붓동생

배우자 = 남편, 아내


```python
pd.crosstab([data.SibSp],data.Survived).style.background_gradient(cmap='summer_r')
```



<div style = overflow:scroll;>
<style  type="text/css" >
#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row0_col0,#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row0_col1{
            background-color:  #008066;
            color:  #f1f1f1;
        }#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row1_col0{
            background-color:  #c4e266;
            color:  #000000;
        }#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row1_col1{
            background-color:  #77bb66;
            color:  #000000;
        }#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row2_col0,#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row4_col0{
            background-color:  #f9fc66;
            color:  #000000;
        }#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row2_col1{
            background-color:  #f0f866;
            color:  #000000;
        }#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row3_col0,#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row3_col1{
            background-color:  #fbfd66;
            color:  #000000;
        }#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row4_col1{
            background-color:  #fcfe66;
            color:  #000000;
        }#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row5_col0,#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row5_col1,#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row6_col1{
            background-color:  #ffff66;
            color:  #000000;
        }#T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row6_col0{
            background-color:  #fefe66;
            color:  #000000;
        }</style><table id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002" ><thead>    <tr>        <th class="index_name level0" >Survived</th>        <th class="col_heading level0 col0" >0</th>        <th class="col_heading level0 col1" >1</th>    </tr>    <tr>        <th class="index_name level0" >SibSp</th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row0_col0" class="data row0 col0" >398</td>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row0_col1" class="data row0 col1" >210</td>
            </tr>
            <tr>
                        <th id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row1_col0" class="data row1 col0" >97</td>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row1_col1" class="data row1 col1" >112</td>
            </tr>
            <tr>
                        <th id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row2_col0" class="data row2 col0" >15</td>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row2_col1" class="data row2 col1" >13</td>
            </tr>
            <tr>
                        <th id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row3_col0" class="data row3 col0" >12</td>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row3_col1" class="data row3 col1" >4</td>
            </tr>
            <tr>
                        <th id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row4_col0" class="data row4 col0" >15</td>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row4_col1" class="data row4 col1" >3</td>
            </tr>
            <tr>
                        <th id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row5_col0" class="data row5 col0" >5</td>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row5_col1" class="data row5 col1" >0</td>
            </tr>
            <tr>
                        <th id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002level0_row6" class="row_heading level0 row6" >8</th>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row6_col0" class="data row6 col0" >7</td>
                        <td id="T_728ddb78_1e5f_11eb_b25f_0242ac1c0002row6_col1" class="data row6 col1" >0</td>
            </tr>
    </tbody></table>




```python
f,ax=plt.subplots(1,2,figsize=(20,8))
sns.barplot('SibSp','Survived',data=data,ax=ax[0])
ax[0].set_title('SibSp vs Survived')
sns.factorplot('SibSp','Survived',data=data,ax=ax[1])
ax[1].set_title('SibSp vs Survived')
plt.close(2)
plt.show()
```


![png](/images/titanic/output_73_0.png)



```python
pd.crosstab(data.SibSp,data.Pclass).style.background_gradient(cmap='summer_r')
```



<div style = overflow:scroll;>
<style  type="text/css" >
#T_83313358_1e5f_11eb_b25f_0242ac1c0002row0_col0,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row0_col1,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row0_col2{
            background-color:  #008066;
            color:  #f1f1f1;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row1_col0{
            background-color:  #7bbd66;
            color:  #000000;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row1_col1{
            background-color:  #8ac466;
            color:  #000000;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row1_col2{
            background-color:  #c6e266;
            color:  #000000;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row2_col0,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row4_col2{
            background-color:  #f6fa66;
            color:  #000000;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row2_col1{
            background-color:  #eef666;
            color:  #000000;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row2_col2{
            background-color:  #f8fc66;
            color:  #000000;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row3_col0,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row3_col2{
            background-color:  #fafc66;
            color:  #000000;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row3_col1{
            background-color:  #fdfe66;
            color:  #000000;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row4_col0,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row4_col1,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row5_col0,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row5_col1,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row5_col2,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row6_col0,#T_83313358_1e5f_11eb_b25f_0242ac1c0002row6_col1{
            background-color:  #ffff66;
            color:  #000000;
        }#T_83313358_1e5f_11eb_b25f_0242ac1c0002row6_col2{
            background-color:  #fefe66;
            color:  #000000;
        }</style><table id="T_83313358_1e5f_11eb_b25f_0242ac1c0002" ><thead>    <tr>        <th class="index_name level0" >Pclass</th>        <th class="col_heading level0 col0" >1</th>        <th class="col_heading level0 col1" >2</th>        <th class="col_heading level0 col2" >3</th>    </tr>    <tr>        <th class="index_name level0" >SibSp</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_83313358_1e5f_11eb_b25f_0242ac1c0002level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row0_col0" class="data row0 col0" >137</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row0_col1" class="data row0 col1" >120</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row0_col2" class="data row0 col2" >351</td>
            </tr>
            <tr>
                        <th id="T_83313358_1e5f_11eb_b25f_0242ac1c0002level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row1_col0" class="data row1 col0" >71</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row1_col1" class="data row1 col1" >55</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row1_col2" class="data row1 col2" >83</td>
            </tr>
            <tr>
                        <th id="T_83313358_1e5f_11eb_b25f_0242ac1c0002level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row2_col0" class="data row2 col0" >5</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row2_col1" class="data row2 col1" >8</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row2_col2" class="data row2 col2" >15</td>
            </tr>
            <tr>
                        <th id="T_83313358_1e5f_11eb_b25f_0242ac1c0002level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row3_col0" class="data row3 col0" >3</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row3_col1" class="data row3 col1" >1</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row3_col2" class="data row3 col2" >12</td>
            </tr>
            <tr>
                        <th id="T_83313358_1e5f_11eb_b25f_0242ac1c0002level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row4_col0" class="data row4 col0" >0</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row4_col1" class="data row4 col1" >0</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row4_col2" class="data row4 col2" >18</td>
            </tr>
            <tr>
                        <th id="T_83313358_1e5f_11eb_b25f_0242ac1c0002level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row5_col0" class="data row5 col0" >0</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row5_col1" class="data row5 col1" >0</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row5_col2" class="data row5 col2" >5</td>
            </tr>
            <tr>
                        <th id="T_83313358_1e5f_11eb_b25f_0242ac1c0002level0_row6" class="row_heading level0 row6" >8</th>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row6_col0" class="data row6 col0" >0</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row6_col1" class="data row6 col1" >0</td>
                        <td id="T_83313358_1e5f_11eb_b25f_0242ac1c0002row6_col2" class="data row6 col2" >7</td>
            </tr>
    </tbody></table>



관측치:
막대 그래프와 요인 그림은 승객이 형제 없이 혼자 탑승한 경우 생존율이 34.5%라는 것을 보여준다. 형제자매 수가 증가하면 그래프는 대략 감소한다. 이게 말이 되네. 즉, 만약 내가 승선하고 있는 가족이 있다면, 나는 먼저 나 자신을 구하지 않고 그들을 구하려고 노력할 것이다. 놀랍게도 5~8인 가족의 생존율은 0%이다. 이유는 Pclass일 수도 있다?

그 이유는 Pclass이다. 십자표는 SibSp>3을 가진 사람이 모두 Pclass3에 있었다는 것을 보여준다. Pclass3(>>3)의 대가족이 모두 사망하는 일이 임박했다.

### Parch


```python
pd.crosstab(data.Parch,data.Pclass).style.background_gradient(cmap='summer_r')
```



<div style = overflow:scroll;>
<style  type="text/css" >
#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row0_col0,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row0_col1,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row0_col2{
            background-color:  #008066;
            color:  #f1f1f1;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row1_col0{
            background-color:  #cfe766;
            color:  #000000;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row1_col1{
            background-color:  #c2e066;
            color:  #000000;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row1_col2{
            background-color:  #dbed66;
            color:  #000000;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row2_col0{
            background-color:  #dfef66;
            color:  #000000;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row2_col1{
            background-color:  #e1f066;
            color:  #000000;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row2_col2{
            background-color:  #e3f166;
            color:  #000000;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row3_col0,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row4_col1,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row5_col0,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row5_col1,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row6_col0,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row6_col1,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row6_col2{
            background-color:  #ffff66;
            color:  #000000;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row3_col1{
            background-color:  #fcfe66;
            color:  #000000;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row3_col2,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row4_col0,#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row4_col2{
            background-color:  #fefe66;
            color:  #000000;
        }#T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row5_col2{
            background-color:  #fdfe66;
            color:  #000000;
        }</style><table id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002" ><thead>    <tr>        <th class="index_name level0" >Pclass</th>        <th class="col_heading level0 col0" >1</th>        <th class="col_heading level0 col1" >2</th>        <th class="col_heading level0 col2" >3</th>    </tr>    <tr>        <th class="index_name level0" >Parch</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row0_col0" class="data row0 col0" >163</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row0_col1" class="data row0 col1" >134</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row0_col2" class="data row0 col2" >381</td>
            </tr>
            <tr>
                        <th id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row1_col0" class="data row1 col0" >31</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row1_col1" class="data row1 col1" >32</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row1_col2" class="data row1 col2" >55</td>
            </tr>
            <tr>
                        <th id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row2_col0" class="data row2 col0" >21</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row2_col1" class="data row2 col1" >16</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row2_col2" class="data row2 col2" >43</td>
            </tr>
            <tr>
                        <th id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row3_col0" class="data row3 col0" >0</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row3_col1" class="data row3 col1" >2</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row3_col2" class="data row3 col2" >3</td>
            </tr>
            <tr>
                        <th id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row4_col0" class="data row4 col0" >1</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row4_col1" class="data row4 col1" >0</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row4_col2" class="data row4 col2" >3</td>
            </tr>
            <tr>
                        <th id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row5_col0" class="data row5 col0" >0</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row5_col1" class="data row5 col1" >0</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row5_col2" class="data row5 col2" >5</td>
            </tr>
            <tr>
                        <th id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002level0_row6" class="row_heading level0 row6" >6</th>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row6_col0" class="data row6 col0" >0</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row6_col1" class="data row6 col1" >0</td>
                        <td id="T_ccb5b4d6_1e5f_11eb_b25f_0242ac1c0002row6_col2" class="data row6 col2" >1</td>
            </tr>
    </tbody></table>



크로스탭은 다시 더 큰 가족이 Pclass3에 있었다는 것을 보여준다.


```python
f,ax=plt.subplots(1,2,figsize=(20,8))
sns.barplot('Parch','Survived',data=data,ax=ax[0])
ax[0].set_title('Parch vs Survived')
sns.factorplot('Parch','Survived',data=data,ax=ax[1])
ax[1].set_title('Parch vs Survived')
plt.close(2)
plt.show()
```


![png](/images/titanic/output_79_0.png)


관측치:
여기에서도 결과는 꽤 비슷하다. 부모를 동반한 승객은 생존 가능성이 더 크다. 하지만 숫자가 늘어날수록 줄어든다.

생존 가능성은 배 안에 1-3명의 부모를 둔 사람에게 좋다. 혼자라는 것은 또한 치명적이고 누군가가 배에 4명 이상의 부모를 두고 있을 때 생존 가능성이 줄어든다는 것을 증명한다.

### 운임--> 지속적 특징


```python
print('Highest Fare was:',data['Fare'].max()) #최고 요금
print('Lowest Fare was:',data['Fare'].min()) #최저 요금
print('Average Fare was:',data['Fare'].mean()) #평균 요금
```

    Highest Fare was: 512.3292
    Lowest Fare was: 0.0
    Average Fare was: 32.2042079685746
    


```python
f,ax=plt.subplots(1,3,figsize=(20,8))
sns.distplot(data[data['Pclass']==1].Fare,ax=ax[0])
ax[0].set_title('Fares in Pclass 1')
sns.distplot(data[data['Pclass']==2].Fare,ax=ax[1])
ax[1].set_title('Fares in Pclass 2')
sns.distplot(data[data['Pclass']==3].Fare,ax=ax[2])
ax[2].set_title('Fares in Pclass 3')
plt.show()
```


![png](/images/titanic/output_83_0.png)


Pclass1의 승객 요금에는 큰 배분이 있을 것으로 보이며, 이 배분은 기준이 감소함에 따라 계속 감소하고 있다. 이것 또한 지속적이기 때문에 우리는 바이닝을 사용하여 이산값으로 변환할 수 있다.

### 모든 형상에 대한 간단한 관측치:
성=남성에 비해 여성의 생존 가능성은 높다.

Pclass:일등석 승객이 되면 생존 가능성이 더 높아진다는 눈에 띄는 추세가 있다. Pclass3의 생존율은 매우 낮다. 여성의 경우 Pclass1에서 생존할 확률은 거의 1이며 Pclass2에서 생존할 확률도 높다. 돈이 이긴다!!!

나이: 5~10세 미만의 어린이들은 생존 확률이 높다. 15세에서 35세 사이의 승객들이 많이 죽었다.

시작됨: 이것은 매우 흥미로운 특징이다. Pclass1 승객의 대다수가 S. Q. 승객들이 모두 Pclass3 출신이었음에도 불구하고 C에서 생존할 가능성은 더 좋아 보인다.

Parch+SibSp: 1-2명의 형제자매가 있고, 기내에 스파우스를 두거나, 1-3명의 부모가 혼자 있거나, 대가족이 당신과 함께 여행하는 것보다 가능성이 더 높다.

### 특색 간의 상관 관계


```python
sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',linewidths=0.2) #data.corr()-->상관 행렬
fig=plt.gcf()
fig.set_size_inches(10,8)
plt.show()
```


![png](/images/titanic/output_87_0.png)

