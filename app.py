from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from twilio import twiml
from twilio.util import TwilioCapability
import os
from random import choice
from local_settings import *


# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config['ACCOUNT_SID'] = ACCOUNT_SID
app.config['AUTH_TOKEN'] = AUTH_TOKEN
app.config['SONYA_APP_SID'] = SONYA_APP_SID
app.config['SONYA_CALLER_ID'] = SONYA_CALLER_ID


@app.route('/')
def index():
    reason = reasonSonyaIsAwesome()
    capability = TwilioCapability(app.config['ACCOUNT_SID'],
        app.config['AUTH_TOKEN'])
    capability.allow_client_outgoing(app.config['SONYA_APP_SID'])
    token = capability.generate()
    return render_template('index.html', token=token, reason=reason)


@app.route('/voice', methods=['POST'])
def voice():
    r = twiml.Response()
    r.say('Hello Sonya.  Here is a reason why you are awesome.')
    reason = reasonSonyaIsAwesome()
    reason.replace(':', '.')
    reason = "This one is from %s" % reason
    r.say(reason)
    with r.gather(action='/gather', numDigits='1') as g:
        g.say('Press 1 if you would like to hear another reason.  Press 2 or ' \
        'hangup if you are finished.')
    r.pause()
    r.redirect('/voice')
    return str(r)


@app.route('/gather', methods=['POST'])
def repeat():
    r = twiml.Response()
    if request.form['Digits'] == '1':
        reason = reasonSonyaIsAwesome()
        reason.replace(':', '.')
        reason = "This one is from %s" % reason
        r.say(reason)
    elif request.form['Digits'] == '2':
        r.say('Bye Sonya!')
        r.hangup()
    else:
        r.say('I did not understand your input.')
    with r.gather(action='/gather', numDigits='1') as g:
        g.say('Press 1 if you would like to hear another reason.  Press 2 or ' \
        'hangup if you are finished.')
    r.pause()
    r.redirect('/voice')
    return str(r)


@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    reason = reasonSonyaIsAwesome()
    if request.form['Body'].upper() == "HELP":
        r.sms("Welcome to the Reasons Sonya Is Awesome Hotline.  Text GIMME " \
                "to get one random reason Sonya is awesome.")
    else:
        r.sms(reason)
    return str(r)


def reasonSonyaIsAwesome():
    reasons = [
            'Alex: You hate the Giants.',
            'Alex: You can make a mean clafuti.',
            'Alex: You are an Excel master.',
            'Alex: You hate Apple.',
            'Alex: You are a beer snob.',
            'Alex: You are a great mother.',
            'Alex: You are a very smart woman.',
            'Alex: You are the neck of our family.',
            'Alex: You have a great waist.',
            'Kent: You are have very intelligent discussions.',
            'Kent: You have a great sense of humor.',
            'Ellen: Your brain is is awesome.',
            'Becca: You are a good listener and has a fantastic perspective.',
            'Becca: You accomplished everything you hoped to before 30.',
            'Becca: You were in every Las Vegas casino before she was 18.',
            'Becca: You can be counted on to be an emergency contact for '\
                'friends who don\'t have family in NYC.',
            'Becca: You were at bars in Williamsburg even when you were ' \
                'super pregnant.',
            'Becca: You like both opera and ska music.',
            'Rob: You are one of the most fiercely loyal people in New York.',
            'Rob: The scope of your intellect is matched only by the size ' \
                    'of your heart',
            'Rob: You remember where you came from and are grateful for ' \
                    'the journey.',
            'Rob: You and Alex form my ideal of matrimony.',
            'Rob: Your family comes first.',
            'Rob: You do not front.']
    return choice(reasons)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
