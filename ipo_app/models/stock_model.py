from ipo_app import db

class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    회사명 = db.Column(db.String(60))
    종가 = db.Column(db.Integer)
    #stock_code = db.relationship

    def __repr__(self):
        return f"Company {self.회사명}, {self.종가}"