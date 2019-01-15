from flask import Flask
from flask_restful import Api, Resource

webapp = Flask(__name__)
api = Api(webapp)
@webapp.route("/hello")
def index(name):
    #@api.resource('/hello')
    
if __name__ == '__main__':
webapp. run(debug=True)