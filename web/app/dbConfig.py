class Config(object):
    '''
    Config Class
    '''
    # DB URL
#    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usr:Usr1@app_db:3306/app?charset=utf8'
    
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'user1',
        'password': 'User1',
        'host': 'my-mysql-container:3306',
        'db_name': 'app'
    })
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
#    SQLALCHEMY_ECHO = False

Config = Config