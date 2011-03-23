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

import config
import urllib, hashlib

class UserData:
  """This class will hold the user's information"""
  my_image_url = ""
  my_full_name = ""
  my_contact_info = ""
  my_cv = ""
  my_interests = ""
  google_analytics_id = ""
  google_analytics_domain = ""
  
  def __init__(self):
    if config.is_gravatar_email_hashed:
      user_hashed_email = config.my_gravatar_email
    else:
      user_hashed_email = hashlib.md5(config.my_gravatar_email.lower()).hexdigest()
	
    self.my_image_url = self.getMyImageUrl(user_hashed_email)
    self.my_full_name = self.getMyFullName()
    self.my_contact_info = self.getMyContactInfo()
    self.my_cv = self.getMyCV()
    self.my_interests = self.getMyInterests()
    self.google_analytics_id = config.analytics_id
    self.google_analytics_domain = config.analytics_domain
	
  def getMyImageUrl(self, user_hashed_email):
    return "http://www.gravatar.com/avatar/" + user_hashed_email
  
  def getMyFullName(self):
    return config.my_name
	
  def getMyContactInfo(self):
    return config.my_contact_info
	
  def getMyCV(self):
    return config.my_cv

  def getMyInterests(self):
    return config.my_interests