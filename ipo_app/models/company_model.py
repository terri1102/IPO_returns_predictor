from ipo_app import db
import psycopg2



class Company(db.Model):   #2009년 1월 1일 부터 2020년 2월 까지
    __tablename__ = 'company'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    #회사명, 종목코드, 상장일, 상장유형, 증권구분, 상장주선인, 액면가, 공모가,공모금액, 최초상장주식수
    companyname = db.Column(db.String(64)) #회사명
    stockcode = db.Column(db.String(64)) #종목코드
    ipodate = db.Column(db.DateTime()) #상장일
    ipotype = db.Column(db.String(64)) #상장유형
    stocktype = db.Column(db.String(64)) #증권구분
    bankers = db.Column(db.String(64)) #상장주선인
    bookvalue = db.Column(db.Integer) #액면가
    price = db.Column(db.Integer) #공모가
    total = db.Column(db.Integer) #공모금액
    stock_amount = db.Column(db.Integer) #최초상장주식수
    year_later = db.Column(db.Integer)
    #stock_code = db.relationship

    def __init__(self, companyname, stockcode, ipodate, price, total):
        self.companyname = companynaself.companyname
        self.stockcode = stockcode
        self.ipodate = ipodate
        self.price = price
        self.total = total

    def __repr__(self):
        return f"Company {self.companyname}, {self.stockcode}, {self.ipodate},{self.price},{self.total}"

"""
with app.app_context():
    import csv
    import pandas as pd
    with open('ipo_final.csv', 'r', encoding='UTF8') as f:
        reader = csv.reader(f) #reader 객체 상태: 이때 데이터는 보이지 않음 #아..converters 못쓰네
        next(reader, None)
        row_list = []          #왠만하면 이렇게 리스트에 row를 넣는 식으로 하기!
        for row in reader:
            row_list.append(row)
        row_list = row_list[1:]
            
        for row in row_list:
        # with app.app_context():
            db.session.execute(
                "INSERT INTO company VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row           #여기 뒤에 row 붙는 거 주의!!!!
            )
    db.session.commit()
"""