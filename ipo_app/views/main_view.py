from flask import Blueprint, render_template, request, url_for, redirect
#from twit_app.utils import main_funcs
#from twit_app.services.tweepy_api import get_user
from ipo_app import db
from ipo_app.models.company_model import Company  #임포트를 안해서 undetected되었음
from ipo_app.models.user_model import Users
from datetime import date
import os

        #path = url_for('services', filename='test_data.xlsx')

bp = Blueprint('main', __name__)

import pandas as pd
#df = pd.read_excel(r'services/test_data.xlsx')
#print(df.head())
#from ipo_app import app
#filename = os.path.join(app.instance_path, 'services', 'test_data.xlsx')
#df = pd.read_excel(path, converters={'종목코드': str}) 


@bp.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


comp_list = []
companies = pd.read_excel('ipo_app/views/final_dataset.xlsx', converters={'종목코드': str})
@bp.route('/company', methods=['GET','POST'])
def read_data():
    """
    데이터 조회하는 페이지
    """
    if request.method == "GET":
        return render_template("company.html")

    if request.method == "POST":
        compname = request.form['existing_company']
        if not compname:
            return "회사명을 검색해주세요."
    #query_comp = Company.query.filter(companyname=compname).first()
        try:
            comp_in_range = companies[companies['회사명'] == compname]
        except:
            return "2009년 1월 1일 ~ 2020년 3월 1일 사이의 데이터를 검색해주세요."
        else:
            ipo_date = str(pd.to_datetime(comp_in_range['상장일'].values[0]).date())
            print(ipo_date)
            #key는 영어로!!!
            com = {"companyname" : comp_in_range['회사명'].values[0], "stockcode": comp_in_range["종목코드"].values[0],\
                "ipodate": ipo_date, "price": comp_in_range["공모가(원)"].values[0],\
                    "total": comp_in_range['공모금액(천원)'].values[0],"stock_amount":comp_in_range['최초상장주식수(주)'].values[0],\
                        "year_later_price": comp_in_range["1년후종가"].values[0], "year_later_return": comp_in_range['수익률'].values[0].round(3)}
        
        
            
            comp_search = Company(companyname=comp_in_range['회사명'].values[0], stockcode=comp_in_range['종목코드'].values[0],\
                ipodate= ipo_date, price=comp_in_range['공모가(원)'].values[0].astype(float)\
                ,total=comp_in_range['공모금액(천원)'].values[0].astype(float), stock_amount=comp_in_range['최초상장주식수(주)'].values[0].astype(float),\
                    year_later_price=comp_in_range['1년후종가'].values[0].astype(float), year_later_return=comp_in_range['수익률'].values[0])
            
       
        new_data = Company.query.filter_by(companyname=com['companyname']).first()
        if not new_data: 
            try:
                db.session.add(comp_search)
                db.session.commit()
                comp_list = Company.query.all()
                return render_template('company.html', comp_list=comp_list)   
            except: 
                return "데이터베이스 반영에 문제가 생겼습니다."
         
    
@bp.route('/intro')
def intro_page():
    return render_template('intro.html')

    #안되는 거: /services/test_data.xlsx, test_data.xlsx
df = pd.read_excel('ipo_app/views/encoded_test.xlsx', converters={'종목코드': str})
#from sklearn.externals import joblib
import joblib
#model = joblib.load('lgb.pkl')
model = joblib.load('ipo_app/views/lgb.pkl')  
predictions = [] 
from datetime import date
#ipo_app/services/test_data.xlsx
@bp.route('/predict', methods=['GET','POST'])
def prediction_data():
    if request.method == "GET":
        return render_template('predict.html'), 200
    if request.method == "POST":
        
        post_predict = request.form['companyname']
        
        data = df[df['회사명']== post_predict]
    
        #print(data) #data.iloc[0,0] 이런식으로 하면 string 값 나옴
        #predict   
        price_predict = model.predict(data)
        #print(price_predict)
        if price_predict[0] == 0:
            verdict = "평균이하"
        if price_predict[0] == 1:
            verdict = "평균이상"
        prediction = {"name": post_predict, "returns": verdict}
        
        query_object = Users(companyname=prediction['name'], prediction_year=verdict)
        
        db_query = Users.query.filter_by(companyname=prediction['name']).first()
        extra_info = {"price": data['공모가(원)'].values[0], "total": data['공모금액(천원)'].values[0]}
        
        if db_query:
            return "데이터가 이미 존재합니다."
        if not db_query:
            db.session.add(query_object)
            db.session.commit()
            predictions = Users.query.all()
            
            return render_template('predict.html', predictions = predictions, extra_info=extra_info), 200

        if not data:
            return "2020년 3월 1일 ~ 2021년 3월 26일 사이의 데이터를 검색해주세요"
        
               
            
       
           # return render_template('predict.html', company_name = company_name), 200

@bp.route('/delete/<int:id>')
def delete_company(id=None):
    """
    delete_company 함수는 `company_id` 를 엔드포인트 값으로 넘겨주면 해당 아이디 값을 가진 유저를 데이터베이스에서 제거해야 합니다.

    요구사항:
      - HTTP Method: `GET`
      - Endpoint: `api/user/<user_id>`

    상황별 요구사항:
      -  `user_id` 값이 주어지지 않은 경우:
        - 리턴값: 없음
        - HTTP 상태코드: `400`
      - `user_id` 가 주어졌지만 해당되는 유저가 데이터베이스에 없는 경우:
        - 리턴값: 없음
        - HTTP 상태코드: `404`
      - 주어진 `username` 값을 가진 유저를 정상적으로 데이터베이스에서 삭제한 경우:
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `200`
    """

    
    company_to_delete = Company.query.get(id) #계속 실패함
    #all_db = Company.query.all() 
    #comp_list 쓰면 됨
    #db_id = Company.query.filter_by(id=id).first()
    if not company_to_delete:
        return "이미 삭제된 정보입니다."

    try:
        db.session.delete(company_to_delete)
        db.session.commit()
        return redirect(url_for('main.read_data'))
    except:
        return "삭제하는 데 문제가 있었습니다."

    return render_template('company.html', comp_list=comp_list)

"""
    if not company_id:
          return Response(status=400) #'', 400 이렇게 써도 됨

    
    db_id = Company.query.filter_by(id=company_id).first()
    if not db_id:
          return Response(status=404) #'', 404
    
    
    db.session.delete(db_id)
    db.session.commit()
    return redirect(url_for('main.company_index'))
"""
@bp.route('/update/<int:id>', methods = ['GET',"POST"])
def update(id):
    company_update = Company.query.get_or_404(id)
    if request.method == 'POST':
        company_update.year_later_price = request.form['content']
        try:
            db.session.commit()
            return redirect('/company')
        except:
            return '업데이트를 하는 데 문제가 발생했습니다.'
    else:
        return render_template('update.html', company_update=company_update)