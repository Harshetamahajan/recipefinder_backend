from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import db

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class UserManager(Resource):
    @staticmethod
    @cross_origin()
    def get():
        connection,cursor = db.create_connection()
        query = request.args['query']
        print(query)
        response = db.execute_query(connection=connection,cursor=cursor,query_param=query)
        print(response)
        return jsonify(response[0][2])


api.add_resource(UserManager, '/api/search')

if __name__ == '__main__':
    app.run(debug=True)
    
