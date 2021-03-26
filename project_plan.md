---
layout: default
title: Docker 정리
date: 2021-03-02
categories:
  - TIL
tags:
  - TIL
comments: true
nav_order: 6
parent: 
---



---

내가 생각하는 flask_app 파일 작성 순서

```python
$ tree

-flask_app
--__init__.py
->views
  |-main_view.py
  |-user_view.py
->models
  |-tweet_model.py
  |-user_model.py
 ->services
  |-api.py
->templates
  |-index.html
->static
  |-style.css
```

1) flask_app의 init.py 파일

2) view 폴더 안의 파일들(circular import 주의)

3) models 폴더 안의 파일들(class)

4) templates 폴더 안의 html

5) 그외 css나 services 폴더 안 api 파일



### init.py 파일 예시

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__) #flask_app 폴더의 이름
    app.config['SQLALCHEMY_DATABASE_UTI'] = "sqlite:///flask_db.sqlite3"
    #app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False  #deprecation warning 생략
    
    db.init_app(app) #함수 밖에 있던 app을 init함 ->import 문제 안 생김
    migrate.init_app(app, db)
    
   @app.route('/')
	def index():
        print('hello spongebob')
        return 'spongebob', 200
    
    from flask_app.views.main_view import main_bp
    app.register_blueprint(main_bp)
    
    return app
```



### view 폴더 안 main_view.py 예시

```python

```



### Flask-sqlalchemy와 sqlalchemy의 차이

1. Flask-SQLAlchemy 는 다음 사항들에 접근 가능하도록 해줍니다 :
   - `sqlalchemy` 와 `sqlalchemy.orm` 의 모든 함수 및 클래스
   - `session` 이라는 사전에 설정된 세션 객체
   - SQLAlchemy 의 엔진
   - `SQLAlchemy.create_all()` 과 `SQLAlchemy.drop_all()` 은 정의된 모델들을 기반으로 테이블을 생성 및 드롭합니다.
   - `Model` 이라는 declarative base 로 설정된 `baseclass`
2. `Model` 클래스는 파이썬의 일반 클래스와 동일하게 작동하고 `query` 라는 특성이 있어 모델로부터 쿼리를 할 수 있습니다.
3. 세션을 커밋해야 기록이 되지만 작업 뒤에는 Flask-SQLAlchemy 에서 자동으로 제거해주기 때문에 따로 제거하지 않아도 됩니다.

flask-sqlalchemy는 sessionmaker 없이 session 바로 생성, 엔진 자동 생성

sqlalchemy.create_all(), drop_all()사용 가능

model도 전달 model 클래스는 query라는 특성이 있음



설치시 유의사항:

sqlalchemy를 1.3버전으로 설치하기, 1.4로 사용시 flask-sqlalchemy 사용시 에러 발생 



flask_sqlalchemy의 db.Model 은 sqlalchemy의 Base다

```python
app = Flask(__name__)
db = SQLAlchemy(app) #flask_sqlalchemy와 sqlalchemy가 연동됨
```



www에서 요청시 gunicorn이 서버에 접속함. gunicorn이 알아서 요청을 여러 app에 나눠서 보낸다.

gunicorn: 서버 담당

flask: 웹 어플리케이션 담당





```python
class Tweet(db.Model):
    __tablename__ = "Tweet"
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.String)
    embedding = db.Column(db.PickleType)
    user_id = db.Column(db.BigInteger, db.ForeignKey("Users.id"))

    user = db.relationship("Users", foreign_keys = user_id, backref=db.backref('tweets', lazy=True))

    def __repr__(self):
        return f"<Tweet {self.id} {self.text}>"

    

def parse_records(db_records):
    parsed_list = []
    for record in db_records:
        parsed_record = record.__dict__
        print(parsed_record)
        del parsed_record["_sa_instance_state"]
        parsed_list.append(parsed_record)
    return parsed_list
```

