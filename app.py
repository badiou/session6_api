from flask import Flask, jsonify, request, abort
from models import setup_db, Plant
from flask_cors import CORS
import random

PLANTS_PER_PAGE = 10


def paginate_plants(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * PLANTS_PER_PAGE
    end = start + PLANTS_PER_PAGE
    plants = [plant.format() for plant in selection]
    current_plants = plants[start:end]
    return current_plants


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    #CORS(app, resources={r"/api/*": {'origins': '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/plants')
    def get_plants():
        plants = Plant.query.all()
        current_plants = paginate_plants(request, plants)
        if len(current_plants) == 0:
            abort(404)
        else:
            formatted_plants = current_plants
            return jsonify({
                'success': True,
                'plants': formatted_plants,
                'totals_plants': len(Plant.query.all())
            })

    @app.route('/plants/<int:plant_id>')
    def get_specific_plant(plant_id):
        plant = Plant.query.filter_by(id=plant_id).one_or_none()
        if plant is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'plant': plant.format()
            })

    @app.route('/plants/<int:plant_id>', methods=['DELETE'])
    def delete_plant(plant_id):
        try:
            plant = Plant.query.filter_by(id=plant_id).one_or_none()

            if plant is None:
                abort(404)
            else:
                plant.delete()
                totals_plants = Plant.query.all()
                return jsonify({
                    'success': True,
                    'deleted': plant_id,
                    'plants': paginate_plants(request, totals_plants),
                    'totals_plants': len(totals_plants)
                })
        except:
            abort(422)

    @app.route('/plants/<int:plant_id>', methods=['PATCH'])
    def update_plant(plant_id):
        # ici on récupère l'information passée dans le body
        body = request.get_json()
        try:
            plant = Plant.query.filter_by(id=plant_id).one_or_none()
            if plant is None:
                abort(404)
            else:
                if 'primary_color' in body:
                    plant.primary_color = body.get('primary_color')
                    plant.update()
                    return jsonify({
                        'success': True,
                        'id': plant.id,
                        'primary_color':plant.primary_color
                    })
        except:
            abort(400)

    @app.route('/plants', methods=['POST'])
    def create_plant():
        body = request.get_json()
        new_name = body.get('name', None)
        new_scientific_name = body.get('scientific_name', None)
        new_is_poisonous = body.get('is_poisonous', None)
        new_primary_color = body.get('primary_color', None)
        new_state = body.get('state', None)
        search = body.get('search', None)
        if new_name is None or new_is_poisonous is None:
            abort(400)

        #try:
        if search:
            plants = Plant.query.order_by(Plant.id).filter(
                Plant.name.ilike('%{}%'.format(search)))
            current_plants = paginate_plants(request, plants)
            return jsonify({
                'success': True,
                'plants': current_plants,
                'totals_plants': len(plants)
            })
        else:
            plant = Plant(name=new_name, scientific_name=new_scientific_name,
                        is_poisonous=new_is_poisonous, primary_color=new_primary_color,state=new_state)
            plant.insert()
            plants = Plant.query.order_by(Plant.id).all()
            current_plants = paginate_plants(request, plants)

            return jsonify({
                'success': True,
                'created': plant.id,
                'plants': current_plants,
                'totals_plants': len(Plant.query.all())
            })
        #except:
            #abort(422)
    
    @app.errorhandler(404)
    def not_found(error):
        return (jsonify({'success': False, 'error': 404,
                'message': 'Not found'}), 404)

    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({'success': False, 'error': 422,
                'message': 'unprocessable'}), 422)

    @app.errorhandler(400)
    def error_client(error):
        return (jsonify({'success': False, 'error': 400,
                'message': 'Bad request'}), 400)

    @app.errorhandler(500)
    def server_error(error):
        return (jsonify({'success': False, 'error': 500,
                'message': 'internal server error'}), 500)

    @app.errorhandler(405)
    def method_not_allowed(error):
        return (jsonify({'success': False, 'error': 405,
                'message': 'method not allowed'}), 405)
        
    if __name__ == "__main__":
        app.run(debug=True)
    return app