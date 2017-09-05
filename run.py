# -*- coding: utf-8 -*-
"""
Main endpoint/runner for metatop
Todo:
    * Unit tests
    * app.py --help
    * Configuration (host/port/debug)
"""
from __future__ import absolute_import
from flask_restful import Api
from resources.games import Games
from flask import Flask

app = Flask('metatop')
# app.config.from_object('config')
api = Api(app)
api.add_resource(Games, '/games', '/games/<string:game_title>')

if __name__ == "__main__":
    app.run(debug=False, threaded=True)

