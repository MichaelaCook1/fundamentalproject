import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Cheeses, Wines, Pairing

# Create the base class for cheese table
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        db.create_all()
        cheese_name1 = Cheeses(cheese_name='Cheddar')
        cheese_texture1 = Cheeses(cheese_texture = 'Hard')
        cheese_origin1 = Cheeses(cheese_origin = 'United Kingdom')
        cheese_aroma1 = Cheeses(cheese_aroma = 'Strong')
        cheese_taste1 = Cheeses(cheese_taste = 'Mature')
        db.session.add(cheese_name1)
        db.session.add(cheese_texture1)
        db.session.add(cheese_origin1)
        db.session.add(cheese_aroma1)
        db.session.add(cheese_taste1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# Create Test of index page
class TestViews(TestBase):

    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_addcheese_get(self):
        response = self.client.get(url_for('addcheese', cheese_id='1'))
        self.assertEqual(response.status_code,200)

    def test_delete_get(self):
        response = self.client.get(url_for('deletecheese', cheese_id='1'))
        self.assertEqual(response.status_code,302)

# Test adding 
class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('addcheese'),
            data = dict(cheese_name='Cheddar')
            )
        self.assertIn(b'Cheddar',response.data)


# Test Deleting

class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(
                url_for('deletecheese', cheese_id='1'),
            data = dict(cheese_name='Cheddar'),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,405)
