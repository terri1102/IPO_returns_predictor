from lightgbm import LGBMClassifier
from category_encoders import OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.externals import joblib


"""
def lightgbm(name):
    pipe = make_pipeline(
    OrdinalEncoder(),

        LGBMClassifier(n_estimators=1000
                    , random_state=2
                    , n_jobs=-1
                    , max_depth=5
            ,learning_rate = 0.2
                    )
    )

    pipe.fit(X_train, y_train)
    return pipe
"""
sk_bio = raw_data[raw_data['회사명'] == 'SK바이오사이언스']
sk_bio['상장일'] = sk_bio['상장일'].replace('-','').astype(int) 
  
def predict(name):
    from lightgbm import LGBMClassifier
    from category_encoders import OrdinalEncoder
    from sklearn.pipeline import make_pipeline
    from sklearn.externals import joblib
    filename = os.path.join(app.instance_path, 'utils', 'lgb.pkl')
    model = joblib.load(filename)    
    x_test = Company.query.filter_by(companyname=name)
    prediction = model.predict(X_test)
    return prediction