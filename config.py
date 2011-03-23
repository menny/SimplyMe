import logging

# Your gravatar email 
# This application will use the Gravatar system to pull information about yourself.
#(see http://www.gravatar.com for more information)
my_gravatar_email = 'fffa64472512e3e9df3519c06428224b'
# It could be safer to store your email in a hashed format, especially if the config.py file is store in a public place (like Github).
is_gravatar_email_hashed = True
#I'm going to pull your image from Gravatar
my_name = "Menny Even Danan"


# Selects the theme to use. Theme names correspond to directories under
# the 'themes' directory, containing templates and static content.
theme = 'raised_clips'
mobile_theme ='raised_clips_mobile'

# Links to External Services on which the User has an Account.
# This will be listed in a theme-specific way.
my_cv = [
   { 'title' : 'AnySoftKeyboard', 'url' : 'http://softkeyboard.googlecode.com', 'description' : 'highly customizable, <a href="https://market.android.com/search?q=anysoftkeyboard&c=apps">plugins</a> based virtual keyboard for the Android OS.' },
   { 'title' : 'SpeakingPal', 'url' : 'http://www.speakingpal.com' , 'description' : 'an mLearning startup.'},
   { 'title' : 'Blog', 'url' : 'http://blog.evendanan.net' , 'description' : 'a pretty static system and software blog.'},
]

my_contact_info = [
   { 'title' : 'email', 'url' : 'mailto://menny@evendanan.net' },
   { 'title' : 'linkedin', 'url' : 'http://il.linkedin.com/in/menny' },
   { 'title' : 'my place', 'url' : 'http://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=Alterman+14,+Tel+Aviv,+Israel&sll=37.0625,-95.677068&sspn=45.418852,93.076172&ie=UTF8&hq=&hnear=Alterman+14,+Tel+Aviv-Yafo,+Israel&t=h&z=16' }
]

my_interests = [
   { 'title' : 'Reader', 'url' : 'http://www.google.com/reader/shared/mennyed', 'description' : 'articles from the web.' },
   { 'title' : 'Picasa', 'url' : 'http://picasaweb.google.com/mennyed', 'description' : 'photos from the world.' },
   { 'title' : 'Forrst', 'url' : 'http://forrst.com/people/menny/posts', 'description' : 'snippets from me and others.' },
]

# If you want to use Google Analytics, enter your 'web property id' here
analytics_id = 'UA-19733018-1'
analytics_domain = '.evendanan.net'
