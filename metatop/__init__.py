# -*- coding: utf-8 -*-
""" metatop web app """
from flask import Flask
from flask_restful import Api
from metatop.resources.games import Games

app = Flask('metatop')
api = Api(app, catch_all_404s=True)
api.add_resource(Games, '/games', '/games/<string:game_title>')
