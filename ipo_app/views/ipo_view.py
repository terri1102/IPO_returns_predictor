from flask import Blueprint, request, redirect, url_for, Response
#from twit_app.services import embedding_api
#from twit_app.services.tweepy_api import get_user, get_tweets
#from twit_app.models import tweet_model
#from twit_app.models.user_model import User
from ipo_app.models.company_model import Company
from ipo_app import db
from ipo_app.services.data_reader_api import get_return

bp = Blueprint('ipo', __name__)


@bp.route('/company', methods=['POST'])
def search_company():
    """
    요구사항:
      - HTTP Method: `POST`
      - Endpoint: `api/user`
      - 받는 JSON 데이터 형식 예시:
            ```json
            {
                "username":"업데이트할 유저의 username",
                "new_username":"새로 업데이트할 username" #불필요
            }
            ```

    상황별 요구사항:
      - 주어진 데이터에 `username` 키가 없는 경우:
        - 리턴값: "Needs username"
        - HTTP 상태코드: `400`
      - 주어진 데이터의 `username` 에 해당하는 유저가 트위터에 존재하지 않은 경우:
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `400`
     - 주어진 데이터의 `username` 을 가지고 있는 데이터가 이미 데이터베이스에 존재하는 경우:
        - 해당 유저의 트윗 값들을 업데이트 합니다.
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `200`
      - 정상적으로 주어진 `username` 을 트위터에서 가져오고 해당 유저의 트윗 또한 가져화 벡터화해서 데이터베이스에 기록한 경우:
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `200`
    """
   
    request_name = request.form['companyname']#request.form["username"]:존재확실 #request.form.get('username') #존재하지 않을 수도 있을 때

    if not request_name:
          return "기업명을 입력해주세요", 400

    try:

      company_name = get_return(name=request_name)
    except:
    
          return redirect(url_for('main.company'), code=400)  #이부분 문제 tweepy.error.TweepError: [{'code': 50, 'message': 'User not found.'}]
   
    tweepy_object = get_tweets(screen_name=twit_username)
    text_list = []
    for i in tweepy_object:
          text = i.full_text
          text_list.append(text)

    embedded = embedding_api.get_embeddings(text_list)
    
    db_tweet = Tweet.query.filter(User.username==request_name).first()
    if db_tweet:
      db_tweet.embedding = embedded
      
      db.session.add(db_tweet)
      db.session.commit()
      return redirect(url_for('main.user_index'), code=200) #main: 블루프린트 이름

    
    return redirect(url_for('main.user_index', msg_code=0), code=200)



@bp.route('/company/<int:company_id>')
def delete_company(company_id=None):
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
     #ㅜㅜ엔드포인트로 주어지는 값은 그냥 쓰는 것
    '''
    task_to_delete = Company.query.get_or_404(company_id)
    try: 
      db.session.delete(task_to_delete)
      db.session.commit()
      return redirect('/company')

    except:
      return "삭제하는 데 문제가 생겼습니다."
    '''
    if not company_id:
          return Response(status=400) #'', 400 이렇게 써도 됨

    
    db_id = Company.query.filter_by(id=company_id).first()
    if not db_id:
          return Response(status=404) #'', 404
    
    
    db.session.delete(db_id)
    db.session.commit()
    return redirect(url_for('main.company_index'))

    #오류의 원인이 임포트 안 해서였다니...ㅠㅠ
