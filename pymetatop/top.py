# -*- coding: utf-8 -*-
"""
top submodule of pymetatop

"""
import requests
from bs4 import BeautifulSoup


class MetaTop(object):
    """
    Class for metascore games top parsing
    Arguments:
        game_title -- if defined returns game object (JSON encoded) only
    """

    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

    def __init__(self, base_url=None):
        self.top = []
        self.base_url = base_url
        if base_url is None:
            self.base_url = 'http://www.metacritic.com/game/playstation-4'

    class FetchError(Exception):
        """Class of network exceptions."""
        pass

    class ParseError(Exception):
        """Class of HTML parsing exceptions."""
        pass

    def clean(self):
        """
        Clean fetched top
        """
        self.top = []

    def fetch(self, use_cache=False):
        """Fetch PS4 metacritic top
        Arguments:
        use_cache -- if true doesn't fetch top again
        """

        if use_cache and self.top:
            return
        try:
            adapter = requests.adapters.HTTPAdapter(max_retries=10)
            session = requests.Session()
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            result = session.get(
                self.base_url, headers=self.headers, timeout=10)
        except(requests.Timeout, requests.ConnectionError, requests.TooManyRedirects):
            raise self.FetchError('Error fetching metacritic site')

        parsed_html = BeautifulSoup(result.text, 'html.parser')
        games = parsed_html.body.findAll(
            'div', attrs={'class': 'wrap product_wrap'})
        if not games:
            raise self.ParseError('Top structure not found')

        self.top = []
        for game in games:
            try:
                title_raw = game.find('h3', attrs={'class': 'product_title'})
                score_raw = game.find(
                    'span', attrs={'class': 'metascore_w medium game positive'})
                if title_raw is None or score_raw is None:
                    raise self.ParseError('Top structure is not correct')
            except:
                raise

            if not score_raw.text.isdigit():
                raise self.ParseError('Unknown type of score')

            self.top.append({u'title': title_raw.text,
                             u'score': int(score_raw.text)})
