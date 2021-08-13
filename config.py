import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        '9Ghy648FibRfcgQIvl4ckso7odiHwrbY0DsdGmMx7OEtIK1tr1qgoAxdTFB2Bra'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db', 'app.db')
    SAML_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'saml')
