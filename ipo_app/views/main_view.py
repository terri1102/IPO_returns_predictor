from flask import Blueprint, render_template, request
#from twit_app.utils import main_funcs
#from twit_app.services.tweepy_api import get_user
from ipo_app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/company')
def read_data():
    """
    데이터 조회하는 페이지
    """
    #ipo_company = Company.query.all()
    #company_list = []
    #company_data = {}
    #for company in ipo_company:
     #   company_data["name"] = company["name"]
      #  company_list.append(company_data)
    #return render_template('company.html', company_list=company_list)
    return render_template('company.html')

'''
@bp.route('/compare', methods=["GET", "POST"])
def compare_index():
    """
    users 에 유저들을 담아 넘겨주세요. 각 유저 항목은 다음과 같은 딕셔너리
    형태로 넘겨주셔야 합니다.
     -  {
            "id" : "유저의 아이디 값이 담긴 숫자",
            "username" : "유저의 유저이름 (username) 이 담긴 문자열"
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