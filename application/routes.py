from flask import render_template,redirect,url_for 
from application import db, app
from application.models import Cheeses, Wines,  Pairing
from application.forms import CheeseForm, WineForm,  PairForm

@app.route('/', methods=['POST', 'GET' ])
def index():
    cheeses = Cheeses.query.all()
    wines = Wines.query.all()
    pairs = Pairing.query.all()
    return render_template('index.html', title='Wine and Cheese Board', cheeses=cheeses, wines=wines, pairs=pairs)

####################################################################################################################################################################

@app.route('/addcheese', methods=['POST','GET'])
def addcheese():
    form = CheeseForm()
    if form.validate_on_submit():
        cheese= Cheeses(
                cheese_name  = form.cheese_name.data,
                cheese_texture = form.cheese_texture.data,
                cheese_origin = form.cheese_origin.data,
                cheese_aroma = form.cheese_aroma.data,
                cheese_taste = form.cheese_taste.data,
                )
        db.session.add(cheese)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addcheese.html', title= "Add a Cheese",form=form)

####################################################################################################################################################################
@app.route('/addwine', methods=['POST','GET'])
def addwine():
    form = WineForm()
    if form.validate_on_submit():
        wine= Wines(
                wine_name = form.wine_name.data,
                wine_body = form.wine_body.data,
                wine_colour = form.wine_colour.data,
                wine_origin = form.wine_origin.data, 
                wine_aroma = form.wine_aroma.data,
                wine_taste = form.wine_taste.data,
                )
        db.session.add(wine)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addwine.html', title= "Add a Wine",form=form)

####################################################################################################################################################################

@app.route('/addpair', methods=['POST','GET'])
def addpair():
    form = PairForm()
    
    cheeses = Cheeses.query.all()
    choices = []
    for cheese in cheeses:
        choices.append((cheese.cheese_id, cheese.cheese_name))    
    form.cheese_id.choices=choices

    wines = Wines.query.all()
    choices = []
    for wine in wines:
        choices.append((wine.wine_id, wine.wine_name))
    form.wine_id.choices=choices
    if form.validate_on_submit():
        pair = Pairing(
                cheese_id = form.cheese_id.data,
                wine_id = form.wine_id.data
                )
        db.session.add(pair)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addpair.html', title= "Add a Pairing",form=form)

####################################################################################################################################################################

@app.route('/updatecheese/<int:cheese_id>', methods=['GET','POST'])
def updatecheese(cheese_id):
    form = CheeseForm()
    cheese = Cheeses.query.get(cheese_id)
    if form.validate_on_submit():
        cheese_update.cheese_name = form.cheese_name.data,
        cheese_update.cheese_texture = form.cheese_texture.data,
        cheese_update.cheese_origin = form.cheese_origin.data,
        cheese_update.cheese_aroma = form.cheese_aroma.data,
        cheese_update.cheese_taste = form.cheese_taste.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.cheese_name.data = cheese_update.cheese_name
        form.cheese_texture.data = cheese_update.cheese_texture
        form.cheese_origin.data = cheese_update.cheese_origin
        form.cheese_aroma.data = cheese_update.cheese_aroma
        form.cheese_taste.data = cheese_update.cheese_taste
        return render_template('update.html', title='Update your Cheeses',form=form)

##################################################################################################################################################################

@app.route('/updatewine/<int:wine_id>', methods=['GET','POST'])
def updatewine(wine_id):
    form = WineForm()
    wine = Wines.query.get(wine_id)
    if form.validate_on_submit():
        wine_update.wine_name = form.wine_name.data,
        wine_update.wine_body = form.wine_body.data,
        wine_update.wine_colour = form.wine_colour.data,
        wine_update.wine_origin = form.wine_origin.data,
        wine_update.wine_aroma = form.wine_aroma.data,
        wine_update.wine_taste = form.wine_taste.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.wine_name.data = wine_update.wine_name
        form.wine_body.data = wine_update.wine_body
        form.wine_colour.data = wine_update.wine_colour
        form.wine_origin.data = wine_update.wine_origin
        form.wine_aroma.data = wine_update.wine_aroma
        form.wine_taste.data = wine_update.wine_taste
        return render_template('update.html', title='Update your Wines',form=form)

##################################################################################################################################################################

@app.route('/updatepair/<int:pair_id>', methods=['GET','POST'])
def updatepair(pair_id):
    form = PairForm()
    pair_update = Pairing.query.get(pair_id)
    if form.validate_on_submit():
        pair_update.cheese_id = form.cheese_id.data
        pair_update.wine_id = form.wine_id.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.cheese_id.data = pair_update.cheese_id
        form.wine_id.data = pair_update.wine_id
        return render_template('updatepair.html', title='Update your Pairings',form=form)

#################################################################################################################################################################

@app.route('/deletecheese/<int:cheese_id>')
def deletecheese(cheese_id):
    currentcheese = Cheeses.query.get(cheese_id)
    db.session.delete(currentcheese)
    db.session.commit()
    return(redirect(url_for('index')))

@app.route('/deletewine/<int:wine_id>')
def deletewine(wine_id):
    currentwine = Wines.query.get(wine_id)
    db.session.delete(currentwine)
    db.session.commit()
    return(redirect(url_for('index')))
    
@app.route('/deletepair/<int:pair_id>')
def deletepair(pair_id):
    currentpair = Pairing.query.get(pair_id)
    db.session.delete(currentpair)
    db.session.commit()
    return(redirect(url_for('index')))
