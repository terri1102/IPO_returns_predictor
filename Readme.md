
---
https://img.shields.io/badge/python-3.8.8-brightgreen
https://img.shields.io/badge/%09SQLAlchemy-1.3.23-yellowgreen
https://img.shields.io/badge/Flask-1.1.2-red
https://img.shields.io/badge/scikit--learn-0.24.1-blue

## 사이트 주소

[https://my-ipo-predictor.herokuapp.com](https://my-ipo-predictor.herokuapp.com/)

## 프로젝트 소개
기존 상장된 기업들의 상장 후 1년 수익률을 조회하고, 새로 상장되는 기업의 1년 후 수익률을 예측하는 사이트입니다.

기업의 상장일, 상장주관사, 액면가, 공모가, 공모금액 등 기업 공개 전에 신고하는 증권신고서에 나오는 정보들을 이용해서 1년 후 상장 직후 주식의 수익률이 평균 수익률(약 16%)을 상회할지 예측하는 사이트입니다. 상장을 준비하면서 기업에게 내려진 여러가지 평가가 상장 당시 이 기업의 밸류에이션을 나타내는 정보들이라고 생각해서, 증권 신고서가 제출된 새로 상장되는 기업의 수익률을 예측하는데 도움이 될 것이라 생각해서 분석을 진행하였습니다. 정확한 수익률 예측은 정확도가 떨어져서 평균 수익률을 구하고 그 수익률 보다 높을지, 적을지만 예측하는 모델로 만들어 보았습니다.

## 데이터
DART API

KIND https://kind.krx.co.kr/main.do?method=loadInitPage&scrnmode=1

네이버 금융https://finance.naver.com

## 모델
lightgbm을 이용해서 평균 수익률 이상/이하를 예측하는 이진 분류 모델입니다. 

## 스키마

[![image](https://user-images.githubusercontent.com/73813367/112963439-569f7980-9182-11eb-996c-f7aab901c505.png)](https://user-images.githubusercontent.com/73813367/112963439-569f7980-9182-11eb-996c-f7aab901c505.png)

api로 바로바로 증권신고서 데이터 받아오는 게 불안정해서 엑셀파일로 데이터를 다운받은 후에 스키마 두 개를 한 테이블로 합쳤습니다. 테이블 company와 users는 데이터 시기가 다르기에 관련이 없지만, company 테이블에 상장된지 1년이 되지 않은 기업도 추가하게 되면 스키마를 업데이트할 예정입니다.
