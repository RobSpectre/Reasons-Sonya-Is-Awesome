from flask import Flask
from flask import request
from flask import render_template
from twilio import twiml
import os
from random import choice


app = Flask(__name__)


@app.route('/')
def index():
    return str("Sonya is awesome!") 


@app.route('/voice', methods=['POST'])
def voice():
    r = twiml.Response()
    r.say('Hello Sonya.  Here are some reasons why you are awesome.')
    reason = reasonSonyaIsAwesome()
    r.say(reason)
    with r.gather(action='/gather', numDigits='1') as g:
        g.say('Press 1 if you would like to hear another message.  Press 2 or ' \
        'if you are finished.')
    r.pause()
    r.redirect('/voice')
    return str(r)


@app.route('/gather', methods=['POST'])
def repeat():
    r = twiml.Response()
    if request.form['Digits'] == '1':
        reason = reasonSonyaIsAwesome()
        r.say(reason)
    elif request.form['Digits'] == '2':
        r.say('Bye Sonya!')
        r.hangup()
    else:
        r.say('I did not understand your input.')
    r.say('Press 1 if you would like to hear another message.  Press 2 or ' \
        'if you are finished.')
    return str(r)


@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    reason = reasonSonyaIsAwesome()
    if request.form['Body'].upper() == "HELP":
        r.sms("Welcome to the Reasons Sonya Is Awesome Hotline.  Text GIMME " \
                "to get a reason Sonya is awesome.")
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
            'Alex: You have a great waist.']
    return choice(reasons)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
