# Pandas 10분 완성
## 목차
- Object Creation (객체 생성)
- Viewing Data (데이터 확인하기)
- Selection (선택)
- Missing Data (결측치)
- Operation (연산)
- Merge (병합)
- Grouping (그룹화)
- Reshaping (변형)
- Time Series (시계열)
- Categoricals (범주화)
- Plotting (그래프)
- Getting Data In / Out (데이터 입 / 출력)
- Gotchas (잡았다!)

일반적으로 각 패캐지는 pd, np, plt라는 이름으로 불러옵니다.

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

### 1. Object Creation (객체 생성)

데이터 구조 소개 섹션을 참조하세요.

Pandas는 값을 가지고 있는 리스트를 통해 Series를 만들고, 정수로 만들어진 인덱스를 기본값으로 불러올 것입니다.
```
s = pd.Series([1,3,5,np.nan,6,8])
```
```
s
```
```
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```

datetime 인덱스와 레이블이 있는 열을 가지고 있는 numpy 배열을 전달하여 데이터프레임을 만듭니다.
```
dates = pd.date_range('20130101', periods=6)
```
```
dates
```
```
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
```

```
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
```
```
df
```

![1](https://user-images.githubusercontent.com/72365762/97937617-82c8f100-1dc2-11eb-8834-319ab7112777.png)

Series와 같은 것으로 변환될 수 있는 객체들의 dict로 구성된 데이터프레임을 만듭니다.

```
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })
```
```
df2
```

![2](https://user-images.githubusercontent.com/72365762/97937717-c58ac900-1dc2-11eb-9ef6-1408c5b26096.png)

```
df2.dtype
```
```
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```
IPython을 이용하고 계시다면 (공용 속성을 포함한) 열 이름에 대한 Tap 자동완성 기능이 자동으로 활성화 됩니다. 다음은 완성될 속성에 대한 부분집합 (subset)입니다.

역자 주 : 아래 제시된 코드의 경우, IPython이 아닌 환경 (Google Colaboratory, Jupyter 등)에서는 사용이 불가능한 코드인 점에 주의하세요.

```
# df2.<TAB>
```
역자 주 : IPython에서 실행하면 다음과 같은 결과값이 나옵니다.
```
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.clip_lower
df2.align              df2.clip_upper
df2.all                df2.columns
df2.any                df2.combine
df2.append             df2.combine_first
df2.apply              df2.compound
df2.applymap           df2.consolidate
df2.D

```

보시다시피 A, B, C, D열이 탭 자동완성 기능으로 실행됩니다. 물론 E도 있습니다. 나머지 속성들은 간결하게 잘라 버렸습니다.

### 2. Viewing Data (데이터 확인하기)
Basic Section을 참조하세요.

데이터프레임의 가장 윗 줄과 마지막 줄을 확인하고 싶을 때에 사용하는 방법은 다음과 같습니다.

역자 주: 괄호() 안에는 숫자가 들어갈 수도 있고 안 들어갈 수도 있습니다. 숫자가 들어간다면, 윗 / 마지막 줄의 특정 줄을 불러올 수 있습니다. 숫자가 들어가지 않다면, 기본값인 5로 처리됩니다.

예시

```
df.tail(3)  # 끝에서 마지막 3줄을 불러옴
df.tail()  # 끝에서 마지막 5줄 불러옴
```

```
df.head()
```
![3](https://user-images.githubusercontent.com/72365762/97937964-801acb80-1dc3-11eb-8630-5ee40cd11bb9.png)

```
df.tail(3)
```
![4](https://user-images.githubusercontent.com/72365762/97937978-8c9f2400-1dc3-11eb-8a16-2963df292c05.png)

인덱스 (index), 열 (column) 그리고 numpy 데이터에 대한 세부 정보를 봅니다.
```
df.index
```
```
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
```
```
df.columns
```
```
Index(['A', 'B', 'C', 'D'], dtype='object')
```
```
df.values
```
```
array([[ 1.20366414,  0.03519932, -0.51651206, -1.65195383],
       [-0.93589333,  0.85494382, -0.81497074, -0.33344655],
       [-2.36422326, -2.18746816,  1.01892836,  1.25290739],
       [-2.21401998,  0.36188549, -0.390074  , -0.49700376],
       [ 1.38734459, -0.44310022, -0.54067692, -0.37018639],
       [ 0.22299798, -1.30886252,  0.43343249,  0.40940659]])
```
describe()는 데이터의 대략적인 통계적 정보 요약을 보여줍니다.

```
df.describe()
```
![5](https://user-images.githubusercontent.com/72365762/97938103-e43d8f80-1dc3-11eb-8a43-b429698ff68d.png)

데이터를 전치합니다.

```
df.T
```



