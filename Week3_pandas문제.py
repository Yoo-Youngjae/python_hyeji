# 3-1) pandas 를 이용하여 lost colonies 를 내림 차순 정렬
import pandas as pd
from pandas import DataFrame
df = pd.read_csv("bee_data.csv")
df2 = df.sort_values("Lost Colonies", ascending=False) # csv파일 이미 내림차순으로 되어 있음
print(df2)

# 3-2) lost colonies 가 높은 상위 10개 row를 뽑기
df_high = df.head(10) # df[0:10]도 가능
print(df_high)

# 3-3) lost colonies 가 낮은 하위 10개 row를 뽑기
df_low = df.tail(10) # df[-10:]도 가능
print(df_low)

# 3-4) lost colonies 의 상위 10개와 하위 10개를 포함하는 row를 제외한 dataframe 를 ‘bee_data_crop.csv’ 라는 파일명으로 저장
df_middle = df[10:-10]
print(df_middle)
df_middle.to_csv('bee_data_crop.csv', index=False) # index 번호 제거

# 3-5) bee_data_crop.csv 파일을 열어 [period, state, pesticide, varroa, other pest, diseases] 를 포함하는 dataframe 변수 X과 ‘lost colonies’ 를 포함하는 series 변수 Y를 만들어 주세요
newdf = pd.read_csv('bee_data_crop.csv')
newdf.rename(columns = {'Period':'X', 'State':'X', 'Pesticide':'X', 'Varroa':'X', 'Otherpest':'X', 'Diseases':'X', 'Lost Colonies':'Y'}, inplace=True)
x_newdf = newdf.drop(['Other Factors', 'Y'], axis=1)
print(x_newdf)
y_newdf = newdf.drop(['Other Factors','X'], axis=1)
print(y_newdf)



