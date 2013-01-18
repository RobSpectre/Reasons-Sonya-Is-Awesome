# Reasons Sonya Is Awesome

A web, voice and SMS app delivering random reasons why my friend Sonya is
awesome.

Delivered for her birthday, January 2012.


## Summary

Happy birthday Sonya!  I cut you some codez.

Text or call (718)285-0684 to use the mobile experience.

## Getting Started

Feel free to personalize this project for the special people in your life. 

1. Create a Twilio account if you do not already have one. 
2. Buy a phone number 
3. Create a TwIML application. Associate your phone number with this appliation. 
4. In local_settings.py uncomment lines 8-11. Changes the variables to the ones you have set up on your Twilio account. You will see your Account SID and your Auth Tokin on the top of your Twilio account Dashboard. The APP SID is the name of your TwIML applicarion. 

<<<<<<< HEAD
	Uncommet to configure in file.  
	ACCOUNT_SID = "ACxxxxxxxxxxxxx"  
	AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
	SONYA_APP_SID = "APzzzzzzzzz"
	SONYA_CALLER_ID = "+17778889999" 
	
=======
```python
Uncommet to configure in file.  
ACCOUNT_SID = "ACxxxxxxxxxxxxx"  
AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
SONYA_APP_SID = "APzzzzzzzzz"
SONYA_CALLER_ID = "+17778889999" 
```	
>>>>>>> userdoc
	
5. Set you your Voice Request URL for your Twilio number to Application_url/voice

For example

	http://immense-oasis-2092.herokuapp.com/voice

And your SMS Request URL to Application_url/sms

For example

	http://immense-oasis-2092.herokuapp.com/sms


## Technology

I'm using a bunch of fun stuff here:

* [Flask](http://flask.pocoo.org/)
* [Heroku](http://www.heroku.com)
* [Twilio](http://www.twilio.com)
* [Skeleton](http://www.getskeleton.com)


## Credits
* Authors: [Rob Spectre](http://www.brooklynhacker.com) and [Alex 
  Aizenberg](http://www.build-a-beard.com)
* Artist: [Brendan O'Brien](http://partoftheprocess.ca)
* License: [Mozilla Public License](http://www.mozilla.org/MPL/)
* Ruby / Sinatra Port: [Steven Chau](https://github.com/whereisciao/Reasons-Sonya-Is-Awesome)
