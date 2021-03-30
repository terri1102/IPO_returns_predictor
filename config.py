class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://kvxwhfps:UOsl6O51bAazg_amBZsp_-dBPyUX9_5J@arjuna.db.elephantsql.com:5432/kvxwhfps' 


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://kvxwhfps:UOsl6O51bAazg_amBZsp_-dBPyUX9_5J@arjuna.db.elephantsql.com:5432/kvxwhfps'
