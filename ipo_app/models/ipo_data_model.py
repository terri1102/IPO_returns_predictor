from ipo_app import db

class IPO(db.Model):
    __tablename__ = 'ipo'

    id = db.Column(db.Integer, primary_key=True)
    회사명 = db.Column(db.String(60))
    증권수량 = db.Column(db.Integer)
    액면가액 = db.Column(db.Integer)
    #stock_code = db.relationship

    def __repr__(self):
        return f"Company {self.회사명}, {self.증권수량}"