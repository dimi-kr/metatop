## About

`metatop` is REST api application for showing Top Playstation 4 Games (By Metascore) using [metacritic](http://www.metacritic.com/game/playstation-4) as a source of data


## Dependencies and Requirements

* Python >= 2.7 (`tox` information below)
* pip

### Python libraries
[flask-restful](http://flask-restful.readthedocs.io)

[requests](http://docs.python-requests.org/en/master/)

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Installation

```bash
$ pip install -r requirements.txt
```

### Run tests

```bash
$ nose2 -C -v
```
### Testing on different environments
```bash
$ tox
```

`tox` default environments are: `py3`, `py35`, `py37`, `py27`. So should be available in a system. 

## Run

```bash
python run.py
```
Web application will be available on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) (dev mode)

## Limitations

The app should run in production with handling concurrent requests on WSGI server side only

## TODO
* ~~Requests tune~~
* ~~HTTP codes REST~~
* ~~Documentation of code~~
* ~~Unit Tests for module~~
* ~~Unit Tests for web app~~
* Test Coverage
* Cache 
* Optimising search in array for huge TOPs
* Implement for all TOPs on [metacritic](http://www.metacritic.com/)
* Dockerfile and server configuration files
