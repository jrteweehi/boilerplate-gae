#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from webapp2_extras import sessions
from google.appengine.api import users

from basehandler import Handler
from models import models as m
import formhandlers as f


class MainPage(Handler):
    def get(self):
        self.render('index.html')

webapp2_config = {}
webapp2_config['webapp2_extras.sessions'] = {
        'secret_key': 'aldfnv;ladnfv:_+%^&!()HUTD<><><ndflsfnvl;dsfnvskdfnvfd',
    }

app = webapp2.WSGIApplication([
    ('/', MainPage),
], config=webapp2_config, debug=True)
