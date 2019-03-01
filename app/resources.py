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

# Define your own resources here
