from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/vijayadr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Doctor(db.Model):
    drid = db.Column('drid', db.Integer(), primary_key=True)
    name = db.Column('name', db.String(50))
    contact = db.Column('contact', db.BigInteger())
    specialization = db.Column("specialization",db.String(50))
    hospitalcontact = db.Column("hospitalcontact",db.BigInteger())
    hospitaladdress = db.Column("hospitaladdress",db.String(50))
    hospitaltiming = db.Column("hospitaltiming",db.String(50))

    @staticmethod
    def dummy_doctor():
        return Doctor(drid=0, name='', contact='',specialization='',hospitalcontact='',hospitaladdress='',hospitaltiming='')


db.create_all()

