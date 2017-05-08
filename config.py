# 配置文件 储存配置文件

import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = 'hard to guess string' or os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/test'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FLASK_MAIL_SUBJECT_PREFIX = '[FLASK]'
    FLASK_MAIL_SENDER = 'Flasky Admin<820850938@qq.com>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
    @staticmethod
    def init_app(app):   # 类方法，参数是程序实例 可以执行对当前环境的配置初始化
        pass
# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    # app.config['MAIL_USE_TLS'] = True
    MAIL_USE_SSL = True
    MAIL_USENAME = os.environ.get('MAIL_USENAME')
    MAIL_PASSWORD = 'izwbqnbcqhqubbej'  # os.environ.get('MAIL_PASSWORD') # izwbqnbcqhqubbej bwj1836 ekqsvjeqsodpbbbh
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/test' or os.environ.get('DEV_DATABASE_URI')
#测试环境
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/test' or os.environ.get('TEST_DATABASE_URI')
# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/test' or os.environ.get('DATABASE_URI')

config = {
          'development': DevelopmentConfig,
          'testing': TestConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig
          }