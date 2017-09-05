import requests
from bs4 import BeautifulSoup

class MetaTop:
    base_url = 'http://www.metacritic.com/game/playstation-4'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    top = []
    # TODO: SESSION FOR REQUESTS
    # RETRIES
    # TIMEOUTS
    # ETC

    class FetchError(Exception):
        pass
    
    class ParseError(Exception):
        pass

    def fetch_top(self, use_cache = False):
        if use_cache and len(self.top) > 0:
            return
        try:
            result = requests.get(self.base_url, headers = self.user_agent)
        except(requests.Timeout, requests.ConnectionError, requests.TooManyRedirects):
            raise PS4Metatop.FetchError('Error fetching metacritic site')
        
        parsed_html = BeautifulSoup(result.text, 'html.parser')
        games = parsed_html.body.findAll('div', attrs={'class':'wrap product_wrap'})
        if len(games) == 0:
            raise PS4Metatop.ParseError('Top structure not found')

        self.top = []
        for game in games:
            try:
                title_raw = game.find('h3', attrs={'class':'product_title'})
                score_raw = game.find('span', attrs={'class':'metascore_w medium game positive'})
                if title_raw == None or score_raw == None:
                    raise PS4Metatop.ParseError('Top structure is not correct')
            except:
                raise

            if not score_raw.text.isdigit():
                raise PS4Metatop.ParseError('Unknown type of score')

            self.top.append({u'title': title_raw.text, u'score': int(score_raw.text)})





