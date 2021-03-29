from ipo_app import db

class User(db.Model): #사람들이 검색해본 데이터
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    
    id = db.Column(db.Integer,primary_key=True)
    #회사명, 종목코드, 상장일, 상장유형, 증권구분, 상장주선인, 액면가, 공모가,공모금액, 최초상장주식수
    companyname = db.Column(db.String(64)) #회사명
    prediction_year = db.Column(db.Integer)

    def __repr__(self):
        return f"Company {self.companyname}, {self.prediction_year}"


#with open('C:/Users/Boyoon Jang/section3/project/test_data.xlsx', 'r') as f:
   # reader = csv.reader(f) #reader 객체 상태: 이때 데이터는 보이지 않음
   # row_list = []          #왠만하면 이렇게 리스트에 row를 넣는 식으로 하기!
   # for row in reader:
   #     row_list.append(row)
   # row_list = row_list[1:]
        
  #  for row in row_list:
   #     cursor.execute(
    #        "INSERT INTO passenger VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", row           #여기 뒤에 row 붙는 거 주의!!!!
     #   )
#db.session.commit()