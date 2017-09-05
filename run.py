# -*- coding: utf-8 -*-
"""
Main endpoint/runner for metatop
Todo:
    * Unit tests
    * app.py --help
    * Configuration (host/port/debug)
"""
from __future__ import absolute_import
from metatop import app

# app.config.from_object('config')

if __name__ == "__main__":
    app.run(debug=False, threaded=True)
