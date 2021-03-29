import pandas_datareader.data as web
from datetime import datetime
import os

#import csv
import pandas as pd
'''
with open('ipo_final.csv', 'r', encoding='UTF8') as f:
    reader = csv.reader(f) #reader 객체 상태: 이때 데이터는 보이지 않음 #아..converters 못쓰네
    next(reader, None)
    row_list = []          #왠만하면 이렇게 리스트에 row를 넣는 식으로 하기!
    for row in reader:
        row_list.append(row)
    row_list = row_list[1:]
'''

#filename = os.path.join(app.instance_path, 'services', 'final_dataset.xlsx')
#df = pd.read_excel(filename, converters={'종목코드': str})     


#name = '메디톡스'
#print('{}의 1년 후 수익률은 {}% 입니다.'.format(name, 100 *get_return(name)))


def dates(name):
  from datetime import datetime
  from datetime import timedelta
  import pandas as pd
  from ipo_app.views.main_view import app
  filename = os.path.join(app.instance_path, 'services', 'final_dataset.xlsx')
  df = pd.read_excel(filename, converters={'종목코드': str})   
  start = df.loc[df['회사명'] == name, '상장일'].item()
  start = start + timedelta(days=365)
  end = start + timedelta(days=7) #만약 start날이 공휴일이거나 했을 때->원래 3일로 두고 했는데 자꾸 오류 나서 숫자 계속 올림
  start = start.strftime('%y-%m-%d %I:%M:%S')
  end = end.strftime('%y-%m-%d %I:%M:%S')  
  start = start[:8]
  start = '20' + start
  end = end[:8]
  end = '20' + end
  return start, end


def price1(name, start, end):
      #from services.dart_api import dart
  import pandas as pd
  from ipo_app.views.main_view import app
  filename = os.path.join(app.instance_path, 'services', 'final_dataset.xlsx')
  df = pd.read_excel(filename, converters={'종목코드': str})   
  stock_code = df.loc[df['회사명'] == name, '종목코드'] #ipo_data -> df
  stock_code = stock_code.to_string(index=False).lstrip()
  prices = web.DataReader(stock_code,'naver', start=start, end=end)
  price_close = prices['Close']
  return price_close[0]

def a_year_later_price(name):
      #import dates, price
  start, end = dates(name)
  if not price1(name, start, end):
        return 0
  else:  
    final_price = price1(name, start, end)
    return final_price



def get_return(name):
      import pandas as pd
      from ipo_app.views.main_view import app
      filename = os.path.join(app.instance_path, 'services', 'final_dataset.xlsx')
      df = pd.read_excel(filename, converters={'종목코드': str})    
      #df = pd.read_excel('final_dataset.xlsx', converters={'종목코드': str})      
      year_later_return = df[df['회사명'] == name]['수익률']
      return (year_later_return.values[0].round(3))