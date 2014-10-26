from flask.ext import restful

class Consumer(restful.Resource):
    def post(self):
        return {'hello': 'world'}
