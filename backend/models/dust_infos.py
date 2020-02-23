from backend.app import db
from datetime import datetime


class DustInfos(db.Model):
    __tablename__ = 'dust_infos'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    city = db.Column(db.String(25), nullable=False)
    pm2 = db.Column(db.String(10), nullable=True)
    pm10 = db.Column(db.String(10), nullable=True)
    date_time = db.Column(db.String(30), nullable=False)

#     def __init__(self, id, city, pm2, pm10, date_time):
#         self._id = id
#         self._city = city
#         self._pm2 = pm2 if pm2 else None
#         self._pm10 = pm10 if pm10 else None
#         self._date_time = date_time
#
#
# def add(items):
#     if not isinstance(items, list):
#         items = [items]
#
#     for item in items:
#         event = DustInfos(id=item.get('id'),
#                           city=item.get('city'),
#                           pm2=item.get('pm2'),
#                           pm10=item.get('pm10'),
#                           date_time=datetime.now().strftime('%Y%m%d'))
#         db.session.add(event)
#         db.session.commit()
#
