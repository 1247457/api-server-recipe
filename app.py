from flask import Flask,request
from http import HTTPStatus
from config.config import Config
from flask_restful import Api

app = Flask(__name__)

# 1. 환경변수 설정
app.config.from_object(Config)

# 2. api 설정
api = Api(app)

# 3. 경로(path)와 리소스(resource)를 연결한다.
# /recipes

from resources.recipe import RecipeListResource

api.add_resource( RecipeListResource, '/recipes' )

    

if __name__ == "__main__":
    app.run()