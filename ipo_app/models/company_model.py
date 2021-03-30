from ipo_app import db
import psycopg2



class Company(db.Model):   #2009년 1월 1일 부터 2020년 2월 까지
    __tablename__ = 'company'
    #__table_args__ = {"schema":"company"} #{'extend_existing': True}
    

    id = db.Column(db.Integer, primary_key=True)
    #회사명, 종목코드, 상장일, 상장유형, 증권구분, 상장주선인, 액면가, 공모가,공모금액, 최초상장주식수
    companyname = db.Column(db.String(64)) #회사명
    stockcode = db.Column(db.String(64)) #종목코드
    ipodate = db.Column(db.DateTime()) #상장일

    price = db.Column(db.Integer) #공모가
    total = db.Column(db.Integer) #공모금액
    stock_amount = db.Column(db.Integer) #최초상장주식수
    year_later_price = db.Column(db.Integer) #1년후 종가
    year_later_return = db.Column(db.Float) #1년후 수익률
    #stock_code = db.relationship

    def __init__(self, companyname, stockcode, ipodate, price, total, stock_amount, year_later_price, year_later_return):
        self.companyname = companyname
        self.stockcode = stockcode
        self.ipodate = ipodate
        self.price = price
        self.total = total
        self.stock_amount = stock_amount
        self.year_later_price = year_later_price
        self.year_later_return = year_later_return

    def __repr__(self):
        return f"Company {self.companyname}, {self.stockcode}, {self.ipodate},{self.price},{self.total}, {self.stock_amount}, {self.year_later_price}, {self.year_later_return}"

