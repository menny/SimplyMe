#!/usr/bin/env python
#
# Copyright 2011 Menny Even Danan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.dist import use_library
use_library('django', '0.96')

import os

try:
  from django import v0_96
except ImportError:
  pass
import django

import django.conf
try:
  django.conf.settings.configure(
    DEBUG=False,
    TEMPLATE_DEBUG=False,
    TEMPLATE_LOADERS=(
      'django.template.loaders.filesystem.load_template_source',
    ),
  )
except (EnvironmentError, RuntimeError):
  pass
import django.template
import django.template.loader

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import config

BASE_DIR = os.path.dirname(__file__)

if isinstance(config.theme, (list, tuple)):
  TEMPLATE_DIRS = config.theme
else:
  TEMPLATE_DIRS = [os.path.abspath(os.path.join(BASE_DIR, 'themes/default'))]
  if config.theme and config.theme != 'default':
    TEMPLATE_DIRS.insert(0, os.path.abspath(os.path.join(BASE_DIR, 'themes', config.theme)))

def _swap_settings(new):
  """Swap in selected Django settings, returning old settings.

  Example:
    save = _swap_settings({'X': 1, 'Y': 2})
    try:
      ...new settings for X and Y are in effect here...
    finally:
      _swap_settings(save)

  Args:
    new: A dict containing settings to change; the keys should
      be setting names and the values settings values.

  Returns:
    Another dict structured the same was as the argument containing
    the original settings.  Original settings that were not set at all
    are returned as None, and will be restored as None by the
    'finally' clause in the example above.  This shouldn't matter; we
    can't delete settings that are given as None, since None is also a
    legitimate value for some settings.  Creating a separate flag value
    for 'unset' settings seems overkill as there is no known use case.
  """
  settings = django.conf.settings
  old = {}
  for key, value in new.iteritems():
    old[key] = getattr(settings, key, None)
    setattr(settings, key, value)
  return old

  
def render_template(template_name):
  old_settings = _swap_settings({'TEMPLATE_DIRS': TEMPLATE_DIRS})
  try:
    tpl = django.template.loader.get_template(template_name)
  finally:
    _swap_settings(old_settings)
	
  template_vals = {}
  template_vals.update({'config': config})
  template_vals.update({'theme_path' : '/static/'+config.theme})
  template_vals.update({'template_name': template_name})
  
  return tpl.render(django.template.Context(template_vals))
  
class MainHandler(webapp.RequestHandler):
    def get(self):
		self.response.out.write(render_template("index.html"));

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
