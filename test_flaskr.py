import os
import unittest
import json
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Plant


class PlanttestCase(unittest.TestCase):
    """This class represents the plant test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "session6_db_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
    'postgres', quote_plus(os.getenv('PASSWORD')), 'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        self.new_plant = {
            'name': 'Champignon vénimeux',
            'is_poisonous': True,
            'scientific_name': 'Champi - Kilo Adansonia DIGITATA',
            'primary_color': 'Green',
            'state': 'TOGO'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_all_plants(self):
        res = self.client().get('/plants')
        # ici on récupère les données provenant de la Response
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['plants'])
        self.assertEqual(data['totals_plants'],len(Plant.query.all()))

    # def test_paginate_plants(self):
    #     res = self.client().get('/plants')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['current_plants'])
    #     self.assertTrue(data['current_plants'])

    # def test_delete_plant(self):
    #     res=self.client().delete('/plants/101')
    #     data=json.loads(res.data)
    #     plant=Plant.query.filter(Plant.id == 101).one_or_none()
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], 101)
    #     self.assertTrue(data['plants'], True)
    #     self.assertTrue(data['totals_plants'])

    # def test_plant_which_does_not_exist(self):
    #     res=self.client().delete('/plants/1000')
    #     data=json.loads(res.data)
    #     plant=Plant.query.filter(Plant.id == 1000).one_or_none()
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')


    # def test_create_new_plant(self):
    #     res=self.client().post('/plants', json = self.new_plant)
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['success'], True)
    #     self.assertTrue(data['created'])
    #     self.assertTrue(data['plants'])
    #     self.assertEqual(len(data['plants']))

    # def test_404_requesting_beyond_the_value_page(self):
    #     res=self.client().get('/plants?page=1000')
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Not found')

    # def test_404_requesting_select_on_plant(self):
    #     res=self.client().get('/plants/1000')
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Not found')
    
    # def test_update_plant_primary_color(self):
    #     res=self.client().patch('/plants/102',json={'primary_color':'Gray'})
    #     data=json.loads(res.data)
    #     plant=Plant.query.filter(Plant.id == 102).one_or_none()
    #     self.assertEqual(res.status_code,200)
    #     self.assertEqual(data['success'],True)
    #     self.assertEqual(plant.format()['primary_color'],'Gray')

    


# # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()