from ipo_app import db

class Stock(db.Model): #test 용 (2020년 3월 1일 이후)
    __tablename__ = 'stock'
    __table_args__ = {'extend_existing': True}

    
    id = db.Column(db.Integer,primary_key=True)
    #회사명, 종목코드, 상장일, 상장유형, 증권구분, 상장주선인, 액면가, 공모가,공모금액, 최초상장주식수
    companyname = db.Column(db.String(64)) #회사명
    stockcode = db.Column(db.String(64)) #종목코드
    ipodate = db.Column(db.DateTime()) #상장일
    ipotype = db.Column(db.String(40)) #상장유형
    stocktype = db.Column(db.String(40)) #증권구분
    bankers = db.Column(db.String(64)) #상장주선인
    bookvalue = db.Column(db.Integer) #액면가
    price = db.Column(db.Integer) #공모가
    total = db.Column(db.Integer) #공모금액
    stock_amount = db.Column(db.Integer) #최초상장주식수

    def __repr__(self):
        return f"Company {self.companyname}, {self.stockcode}, {self.ipodate},{self.price},{self.total}"

#from os.path import join, dirname, realpath

#UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads/..')
'''
from openpyxl import load_workbook
wb = load_workbook('sample_book.xlsx')
with open('test_data.xlsx', 'r') as f:
    reader = csv.reader(f) #reader 객체 상태: 이때 데이터는 보이지 않음
    row_list = []          #왠만하면 이렇게 리스트에 row를 넣는 식으로 하기!
    for row in reader:
        row_list.append(row)
    row_list = row_list[1:]
        
    for row in row_list:
        cursor.execute(
            "INSERT INTO passenger VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", row           #여기 뒤에 row 붙는 거 주의!!!!
        )
db.session.commit()
import pandas as pd
file_location = 'test_data.xlsx'
df = pd.read_excel(file_location, converters={'종목코드':str}) #csv는 앞의 0을 날려버려서 엑셀파일로 저장했음

row_list = []          #왠만하면 이렇게 리스트에 row를 넣는 식으로 하기!
for row in df:
    row_list.append(row)
row_list = row_list[1:]
    
for row in row_list:
    db.session.execute(
        "INSERT INTO test VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row           #여기 뒤에 row 붙는 거 주의!!!!
    )
db.session.commit()
'''