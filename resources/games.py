# -*- coding: utf-8 -*-
"""
Games resource for metatop web app
"""
from __future__ import absolute_import
from flask_restful import Resource, abort
from pymetatop.top import MetaTop

class Games(Resource):
    """
    Flask app class for games resource
    """

    def __init__(self):
        self.ps4top = MetaTop()

    def get(self, game_title=None):
        """
        Method GET for games resource

        Keyword arguments:
        game_title -- if defined returns game object (JSON encoded) only
        """
        try:
            self.ps4top.fetch(use_cache=True)
        except(MetaTop.FetchError, MetaTop.ParseError):
            return abort(500, message='Datasource problem', error=True, code=500)

        if game_title is None:
            return self.ps4top.top
        else:
            for game in self.ps4top.top:
                if game["title"] == game_title:
                    return game
            return abort(404, message='Game not found in the top', error=True, code=404)
        return
