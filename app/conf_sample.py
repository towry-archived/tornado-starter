# -*- coding: utf-8 -*-

import tornado
import tornado.template
import os
import sys
from tornado.options import define, options

# Make filepaths relative to settings.
path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path(ROOT, 'app'))

define("port", default=9010, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=True, help="debug mode")
tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, "views")

settings = {}
settings['debug'] = True
settings['static_path'] = MEDIA_ROOT
settings['static_domain'] = ""
settings['cookie_secret'] = "s5lwetoKJoe2323dfadcx_$tutru"
settings['xsrf_cookies'] = False
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
settings['template_path'] = TEMPLATE_ROOT

if options.config:
    tornado.options.parse_config_file(options.config)
