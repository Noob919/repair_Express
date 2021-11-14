from core import db
from core.forms import RepairmentForm

class Repair(db.Model):
    __tablename__ = 'Repairment_table'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False, unique = False) 
    email_address = db.Column(db.String(length = 30), nullable = False, unique = True) 
    phone_model = db.Column(db.String(length = 30), nullable = False) 
    warrenty = db.Column(db.String(length = 3), nullable = False)
    desc_Repair = db.Column(db.String(length = 600), nullable = False) 
    address = db.Column(db.String(length = 30), nullable = False)
     
     