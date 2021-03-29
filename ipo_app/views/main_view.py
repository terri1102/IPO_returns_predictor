from flask import Blueprint, render_template, request, url_for
#from twit_app.utils import main_funcs
#from twit_app.services.tweepy_api import get_user
from ipo_app import db
from ipo_app.services.data_reader_api import get_return
from ipo_app.models.company_model import Company  #임포트를 안해서 undetected되었음
from ipo_app.models.user_model import User
from ipo_app.models.stock_model import Stock
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
    #if request.method == 'POST':
     #   re_company = request.form['content']
      #  comp_data = Company(companyname = re_company)

     #   try:
      #      db.session.add(comp_data)
       #     db.session.commit()
        #    return redirect('company.html') #원래 redirect('/') 였음
     #   except:
      #      return "오류가 있었습니다."
    return render_template('index.html')


@bp.route('/company', methods=['GET','POST'])
def read_data():
    """
    데이터 조회하는 페이지
    """
    if request.method == "GET":
        return render_template("company.html")
  
    compname = request.form['existing_company']
    if not compname:
        return "회사명을 검색해주세요."
    query_comp = Company.query.filter(companyname=compname).first()
   
    if not query_comp:
        return "2009년 1월 1일 ~ 2020년 3월 1일 사이의 데이터를 검색해주세요."

    #db.session.add(users)
    if request.method == 'POST':
            
        comp_list = []
        
        for company in query_comp:
            com = {"회사명" : company['companyname'], "종목코드": company["stockcode"], "상장일": company["ipodate"], "공모가": company["price"], "1년후종가": company["year_later"]}
            comp_list.append(com)
        return render_template('company.html', comp_list=comp_list)    
    

    
    
@bp.route('/intro')
def intro_page():
    return render_template('intro.html')


@bp.route('/predict', methods=['GET','POST'])
def prediction_data():
    if request.method == "GET":
        return render_template('predict.html'), 200
    if request.method == "POST":
        try:
            post_predict = request.form['companyname']
            print(post_predict) #post_predict에 값 제대로 들어감
            
            from ipo_app import app
            #path = url_for('services', filename='test_data.xlsx')
            filename = os.path.join(app.instance_path, 'services', 'test_data.xlsx')
            df = pd.read_excel(path, converters={'종목코드': str}) 
            print(df.head())
            data = df[df['회사명']== post_predict]
            #sk_bio = raw_data[raw_data['회사명'] == 'SK바이오사이언스']
            data['상장일'] = data['상장일'].replace('-','').astype(int) 

           #predict
            from sklearn.externals import joblib
            model = os.path.join(app.instance_path, 'utils', 'lgb.pkl')
            price_predict = model.predict(data)
            predictions = [] 
            predict_list = User.query.all()
            for p in predict_list:  
                prediction = {"name": name, "returns": 100 * price_predict}
            predictions.append(prediction)
            query_object = User(prediction['name'], prediction['returns'])
            db.session.add(query_object)
            db.session.commit()
            return render_template('predict.html', predictions = predictions), 200
        except:
           return "2020년 3월 1일 ~ 2021년 3월 26일 사이의 데이터를 검색해주세요"
        
               
            
       
           # return render_template('predict.html', company_name = company_name), 200
        
'''
@bp.route('/compare', methods=["GET", "POST"])
def compare_index():
    """
    users 에 유저들을 담아 넘겨주세요. 각 유저 항목은 다음과 같은 딕셔너리
    형태로 넘겨주셔야 합니다.
     -  {
            "id" : "유저의 아이디 값이 담긴 숫자",
            "companyname" : "유저의 유저이름 (username) 이 담긴 문자열"
        }

    prediction 은 다음과 같은 딕셔너리 형태로 넘겨주셔야 합니다:
     -   {
             "result" : "예측 결과를 담은 문자열입니다",
             "compare_text" : "사용자가 넘겨준 비교 문장을 담은 문자열입니다"
         }
    """
    """
    json = request.get_json(force=True) #request.form.get('username') 이러 것과 차이
    #https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
    username1 = json['user_1']
    username2 = json['user_2']

    data1 = get_user(username1)
    data2 = get_user(username2)
    #query1 = User.query.filter_by(username=json['user_1']).first()
    #query2 = User.query.filter_by(username=json['user_2']).first()
    
    users = [{"id" : data1.id, "username": data1.username },{"id" : data2.id, "username": data2.username }]
    """
    #로지스틱 모델 내가 구현할 필요가 없었구나...ㅎ
    user1 = request.form.get('user_1')
    user2 = request.form.get('user_2')
    compare_text = request.form.get('compare_text')

    if request.method == "GET":
        return render_template('compare_user.html'), 200

    if request.method == "POST":
        #폼 데이터를 받아온다.
        #해당 유저들을 조회
        #해당 유저들의 트윗 -> 벡터화된 트윗 조회
        #비교 문장 -> 벡터화

        #모델을 여기서 해도 되고 다른 파일로 해도 됨
        #예측
        query1 = User.query.filter_by(user_id=user1).first()
        query2 = User.query.filter_by(user_id=user2).first()
        users = [query1, query2]
        
        logistic = main_funcs.predict_text(users, compare_text)   
        prediction = {"result": logistic, "compare_text": compare_text}   
        return render_template('compare_user.html', users=users, prediction=prediction), 200
       

def user_index():
    """
    user_list 에 유저들을 담아 템플렛 파일에 넘겨주세요
    """

    msg_code = request.args.get('msg_code', None)
    
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None
    user_list = []
    users = User.query.all()

    for user in users:
        user_id = {"id" : user["id"], "username" : user['username'], "full_name": user["full_name"]}
        user_list.append(user_id)
    
    return render_template('user.html', alert_msg=alert_msg, user_list=user_list)
'''