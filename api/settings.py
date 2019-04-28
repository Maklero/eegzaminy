from data import data


class Settings(object):
    DEBUG = True

    HOST = '0.0.0.0'
    PORT = 8080

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(user=data['user'], password=data['passwd'], host=data['host'], database=data['database'])

    JWT_SECRET_KEY = 'jwt-secret-string'

    CORS_RESOURCES = {
        r"/v1/*": {
            "origins": [
                "http://localhost",
                "http://127.0.0.1:*",
                "http://192.168.8.*",
                "http://192.168.8.*:*",
                "https://localhost",
                "https://*.eegzaminy.pl",
                "http://test.eegzaminy.pl/",
                "*",
            ]
        }
    }
