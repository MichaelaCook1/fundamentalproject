from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Cheeses

class CheeseForm(FlaskForm):
    task=StringField('Task',
            validators=[
                DataRequired(),
                ]
            )
    submit = SubmitField('Submit')

    def validate_task(self,task):
        cheeses = Cheeses.query.all()
        for cheese in cheeses:
            if cheese.task == task.data:
                raise ValidationError("You've already added this Cheese")

class OrderCheese(FlaskForm):
    order_with = SelectField('Order With',
            choices=[
                ("id","Recent"),
                ("old","Old")
                ]
            )
    submit = SubmitField('Order')

####################################################################################################################################################################

from application.models import Wines
class WineForm(FlaskForm):
    task=StringField('Task',
            validators=[
                DataRequired(),
                ]
            )
    submit = SubmitField('Submit')
    
    def validate_task(self,task):
        wines = Wines.query.all()
        for wine in wines:
            if wine.task == task.data:
                raise ValidationError("You've already added this Wine")
class OrderWine(FlaskForm):
    order_with = SelectField('Order With',
            choices=[
                ("id","Recent"),
                ("old","Old")
                ]
            )
    submit = SubmitField('Order')

####################################################################################################################################################################

from application.models import Pairing
class PairForm(FlaskForm):
    task=StringField('Task',
            validators=[
                DataRequired(),
                ]
            )
    submit = SubmitField('Submit')
    
    def validate_task(self,task):
        pairs = Pairing.query.all()
        for pair in pairs:
            if pair.task == task.data:
                raise ValidationError("You've already added this Pairing")
class OrderCheese(FlaskForm):
    order_with = SelectField('Order With',
            choices=[
                ("id","Recent"),
                ("old","Old")
                ]
            )
    submit = SubmitField('Order')
