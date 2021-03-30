from ipo_app import db

class Users(db.Model): #사람들이 검색해본 데이터
    __tablename__ = 'users'
  #  __table_args__ = {"schema":"users"}#{'extend_existing': True}

    
    id = db.Column(db.Integer,primary_key=True)
    #회사명, 종목코드, 상장일, 상장유형, 증권구분, 상장주선인, 액면가, 공모가,공모금액, 최초상장주식수
    companyname = db.Column(db.String(64)) #회사명
    prediction_year = db.Column(db.String(64))

    def __repr__(self):
        return f"Users {self.companyname}, {self.prediction_year}"


