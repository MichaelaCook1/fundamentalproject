from application import db #imports database

class Cheeses(db.Model): #declares Cheese table as a class
    cheese_id = db.Column(db.Integer,primary_key=True)
    cheese_name = db.Column(db.String(50))
    cheese_texture = db.Column(db.String(50))
    cheese_origin = db.Column(db.String(50))
    cheese_aroma = db.Column(db.String(50))
    cheese_taste = db.Column(db.String(80))
    relationship = db.relationship("Pairing", backref="Cheeses") 


#################################################################################################################

class Wines(db.Model): #declares Wine table as a class
    wine_id = db.Column(db.Integer,primary_key=True)
    wine_name = db.Column(db.String(50))
    wine_body = db.Column(db.String(50))
    wine_colour = db.Column(db.String(50))
    wine_origin = db.Column(db.String(50))
    wine_aroma = db.Column(db.String(80))
    wine_taste = db.Column(db.String(80))
    relationship = db.relationship("Pairing", backref="Wines")

#################################################################################################################

class Pairing(db.Model): # declares Wine&Cheese Pariiing table as class
    pair_id = db.Column(db.Integer,primary_key=True)
    cheese_id = db.Column(db.Integer, db.ForeignKey('cheeses.cheese_id'))
    wine_id = db.Column(db.Integer, db.ForeignKey('wines.wine_id'))

