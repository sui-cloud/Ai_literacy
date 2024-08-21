
import pandas as pd
import matplotlib.pyplot as plt #피벗테이블 차트 그리기 
#import pandas as pd #피벗테이블 차트 그리기 
import seaborn as sns

def merchain():
       #파일 불러오기
       df = pd.read_csv('data/Europe Hotel Booking Satisfaction Score.csv')

       # 결측치 개수 확인 
       df.isnull().sum()

       #호텔 와이파이 서비스 항목 설문조사 빈도수 구하기
       sns.countplot(x='Hotel wifi service', data=df) # 시본 카운트플랏 피벗테이블 없어도 차트 가능
       plt.show()


       #상관관계 파악하기
       plt. figure(figsize=(10,8))
       sns. heatmap(df.corr(numeric_only = True), annot=True,  cmap='Blues')
       plt. show()

       #피처 데이터
       X = df[['Hotel wifi service',
              'Departure/Arrival  convenience', 'Ease of Online booking',
              'Hotel location', 'Food and drink', 'Stay comfort',
              'Common Room entertainment', 'Checkin/Checkout service',
              'Other service', 'Cleanliness']]

       # 타켓 데이터
       y= df['satisfaction']       

