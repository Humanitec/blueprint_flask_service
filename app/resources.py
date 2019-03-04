from flask import current_app as app
from flask_restplus import Api, Resource

from .models import db

api = Api(
    doc='/docs/',
    title='Service API'
)


@api.route('/health_check/', doc=False)
class Health(Resource):

    def get(self):
        is_database_working, output = True, 'database is ok'
        try:
            db.engine.execute('SELECT 1')
        except Exception as e:
            is_database_working, output = False, str(e)

        return {'status': is_database_working, 'output': output}


@api.route('/docs/swagger.json', doc=False)
class Swagger(Resource):
    """
    Flask-Restplus has hardcoded "/swagger.json" URL, but we need to expose it as "/docs/swagger.json"
    """

    def get(self):
        return app.view_functions['specs']()


# Define your own resources here
