from backend.app import db
from sqlalchemy import Column


class DustInfos(db.Model):
    __tablename__ = 'dust_infos'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    city = Column(db.String(25), nullable=False)
    pm2 = Column(db.String(10), nullable=True)
    pm10 = Column(db.String(10), nullable=True)
    date_time = Column(db.DateTime)