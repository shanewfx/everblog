# coding=utf-8
"""
    everblog
    ~~~~~~~~
    Everblog is named after Evernote, you can publish your Evernote notes to Everblog as blog entries.
"""
from flask import Flask
from werkzeug.routing import BaseConverter
from quick_orm.core import Database
from toolkit_library.encryption import Encryption


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter
app.config.update(
    DEBUG = True,
    SECRET_KEY = Encryption.generate_random_string(),

    CONNECTION_STRING = 'sqlite:///everblog.db'
)

db = Database(app.config['CONNECTION_STRING'])

import everblog.blueprints
