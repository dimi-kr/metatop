from pymetacritic import top
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Games(Resource):
    
    
    def __init__(self):
        self.ps4top = top.MetaTop()  

    def get(self,game_title=None):
        self.ps4top.fetch_top(use_cache=True) 
        if game_title is None:
            return self.ps4top.top
        else:
            for game in self.ps4top.top:
                if game["title"] == game_title:
                    return game
        return 

api.add_resource(Games, '/games','/games/<string:game_title>')

if __name__ == "__main__":
    app.run(debug=False)
