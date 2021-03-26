from ipo_app import db

class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    시장구분 = db.Column(db.String(40))
    회사명 = db.Column(db.String(60))
    신고서제출일 = db.Column(db.DateTime())
    납입일 = db.Column(db.DateTime())
    확정공모가 = db.Column(db.Integer)
    공모금액 = db.Column(db.Integer)
    상장예정일 = db.Column(db.DateTime)
    상장주선인 = db.Column(db.String(50))
    종가 = db.Column(db.Integer, db.ForeignKey('Stock.close'))
    #stock_code = db.relationship

    def __repr__(self):
        return f"Company {self.회사명}"



'''

class Tweet(db.Model):
    __tablename__ = 'tweet'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    embedding = db.Column(db.PickleType)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    
    def __repr__(self):
        return f"Tweet {self.id}"
'''