from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError


from application.models import Cheeses

class CheeseCheck:
    def __init__(self,message):
        self.message = message
        
    def __call__(self, form, field):
        cheese_total = Cheeses.query.all()
        for cheese in cheese_total:
            if Cheeses.cheese_name == field.data:
                raise ValidationError(self.message)

class CheeseForm(FlaskForm):
    cheese_name=StringField('cheese_name',
            validators=[
                DataRequired(),
                CheeseCheck(message=" You already have that cheese")
                ]
            )
    cheese_texture=StringField('cheese_texture')
    cheese_origin=StringField('cheese_origin')
    cheese_aroma=StringField('cheese_aroma')
    cheese_taste=StringField('cheese_taste')

    submit = SubmitField('Submit')

####################################################################################################################################################################

from application.models import Wines
class WineForm(FlaskForm):
    wine_name=StringField('wine_name',
            validators=[
                DataRequired(),
                ]
            )
    wine_body=StringField('wine_body')
    wine_colour=StringField('wine_colour')
    wine_origin=StringField('wine_origin')
    wine_aroma=StringField('wine_aroma')
    wine_taste=StringField('wine_taste')

    submit = SubmitField('Submit')
    
    def validate_wine_name(self,wine_name):
        wines = Wines.query.all()
        for wine in wines:
            if wine.wine_name == wine_name.data:
                raise ValidationError("You've already added this Wine")

####################################################################################################################################################################

from application.models import Pairing
class PairForm(FlaskForm):
    cheese_id=SelectField('Choose Cheese', choices=[])
    
    wine_id=SelectField('Choose Wine', choices=[])

    submit = SubmitField('Submit')
    
    def validate_task(self,task):
        pairs = Pairing.query.all()
        for pair in pairs:
            if pair.cheese_id == cheese_id.data and pair.wine_id ==wine_id.data:
                raise ValidationError("You've already added this Pairing")

