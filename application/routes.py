from flask import render_template,redirect,url_for 
from applciation import db, app
from application.models import Cheeses, Wines, Pairing
from application.forms import CheeseForm, WineForm, PairForm, OrderCheese, OrderWine, OrderPairing

@app.route('/', methods=['POST', 'GET' ])
def index():
    cheese = Cheeses.query.all()
    wine = Wines.query.all()
    pair = Pairing.query.all()
    return render_template('index.html', title='Wine and Cheese Board', cheese=cheese, wine=wine, pair=pair)

####################################################################################################################################################################

@app.route('/addcheese', methods=['POST','GET'])
def addcheese():
    form = CheeseForm()
    if form.validate_on_submit():
        cheese= Cheeses(
                task = form.task.data
                )
        db.session.add(cheese)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addcheese.html', title= "Add a Cheese",cheese=cheese,form=form)

####################################################################################################################################################################
@app.route('/addwine', methods=['POST','GET'])
def addwine():
    form = WinesForm()
    if form.validate_on_submit():
        wine= Wines(
                task = form.task.data
                )
        db.session.add(wine)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addwine.html', title= "Add a Wine",wine=wine,form=form)

####################################################################################################################################################################

@app.route('/addpair', methods=['POST','GET'])
def addpair():
    form = PairForm()
    if form.validate_on_submit():
       pair = Pairing(
                task = form.task.data
                )
        db.session.add(pair)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addpair.html', title= "Add a Pairing",pair=pair,form=form)

####################################################################################################################################################################

@app.route('/updatecheese/<int:id>', methods=['GET','POST'])
def updatecheese(id):
    form = CheeseForm()
    cheese = Cheeses.query.get.(id)
      if form.validate_on_submit():
        cheese.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = cheese.task
        return render_template('update.html', title='Update your Cheeses',form=form)

##################################################################################################################################################################

@app.route('/updatewine/<int:id>', methods=['GET','POST'])
def updatewine(id):
    form = WineForm()
    wine = Wines.query.get.(id)
      if form.validate_on_submit():
        wine.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = wine.task
        return render_template('update.html', title='Update your Wines',form=form)

##################################################################################################################################################################

@app.route('/updatepair/<int:id>', methods=['GET','POST'])
def updatepair(id):
    form = PairForm()
    pairs = Pairing.query.get.(id)
      if form.validate_on_submit():
        pair.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = pair.task
        return render_template('update.html', title='Update your Pairings',form=form)

#################################################################################################################################################################

@app.route('/delete/<int:id>')
def delete(id):
    currentcheese = Cheeses.query.get(id)
    currentwine = Wines.query.get(id)
    currentpair = Pairing.query.get(id)
    db.session.delete(currentwine)
    db.session.delete(currentpair)
    db.session.delete(currentcheese)
    db.session.commit()
    return(redirect(url_for('index')))
