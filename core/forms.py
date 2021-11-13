from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import Length,Email, DataRequired 

 

class RepairmentForm(FlaskForm):
    name = StringField(label = 'name', validators = [Length(min=2, max=20), DataRequired()])
    email_address  = StringField(label = 'email_address', validators = [Email(), DataRequired()])
    phone_model = StringField(label = 'phone_model', validators = [Length(min = 5, max= 20), DataRequired()] ) 
    warrenty = BooleanField(label = 'warrenty', validators = [DataRequired()]) 
    desc_Repair = StringField(label = 'desc_Repair', validators = [Length(min = 5, max= 20), DataRequired()] ) 
    address = StringField(label = 'address', validators = [Length(min = 5, max= 20), DataRequired()] ) 
    submit = SubmitField(label = 'Form Submitt')

