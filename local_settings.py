'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
#ACCOUNT_SID = "ACxxxxxxxxxxxxx" 
#AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
#RAMONES_APP_SID = "APzzzzzzzzz"
#RAMONES_CALLER_ID = "+17778889999"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ.get['ACCOUNT_SID']
AUTH_TOKEN = os.environ.get['AUTH_TOKEN']
SONYA_APP_SID = os.environ.get['SONYA_APP_SID']
SONYA_CALLER_ID = os.environ.get['SONYA_CALLER_ID']
