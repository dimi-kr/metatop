# -*- coding: utf-8 -*-
"""
Tests for metatop web app
"""
import json
import unittest2 as unittest
import metatop

#import requests

'''
class TestMetaTopFlaskUsingRequests(unittest.TestCase):
    # requests testing

    def test_games_resource(self):
        # resource /games should return 200
        response = requests.get('http://localhost:5000/games')
        self.assertEqual(response.status_code, 200)
'''

class TestMetaTopFlask(unittest.TestCase):
    ''' Tests class for metatop web app '''
    metatop.app.testing = True
    metatop.app.debug = True

    def setUp(self):
        self.app = metatop.app.test_client()
        self.api = metatop.api
        #self.api.add_resource(metatop.Games, '/games', '/games/<string:game_title>')

    def test_getroot(self):
        ''' GET / should be 404 '''
        result = self.app.get('/')
        assert result.status_code == 404

    def test_postroot(self):
        ''' POST / should be 404 '''
        result = self.app.post('/')
        assert result.status_code == 404

    def test_games(self):
        ''' GET /games should be 200 with content '''
        result = self.app.get('/games')
        assert result.status_code == 200

    def test_games_content(self):
        ''' GET /games should be with content '''
        result = self.app.get('/games')
        result_dict = json.loads(result.data.decode())
        assert result_dict

    def test_post_not_allowed_games(self):
        ''' POST on /games should be 405 Not Allowed Method '''
        result = self.app.post('/games')
        assert result.status_code == 405

    def test_put_not_allowed_games(self):
        ''' PUT on /games should be 405 Not Allowed Method '''
        result = self.app.put('/games')
        assert result.status_code == 405

    def test_delete_not_allowed_games(self):
        ''' DELETE on /games should be 405 Not Allowed Method '''
        result = self.app.delete('/games')
        assert result.status_code == 405

    def test_non_existing_game(self):
        ''' Non existing game should return 404 '''
        result = self.app.get('/games/Final Fantasy XLVII')
        assert result.status_code == 404

    def test_games_resource_with_game(self):
        ''' Existing game should return 200 with content '''
        result = self.app.get('/games')
        result_dict = json.loads(result.data.decode())
        result = self.app.get('/games/%s'%result_dict[0][u'title'])
        assert result.status_code == 200
        