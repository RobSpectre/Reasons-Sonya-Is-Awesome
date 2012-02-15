import unittest
try:
    from app import app
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath('.'))
    from app import app


class WebTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.debug = True

    def assertTwiML(self, response):
        self.assertTrue("<Response>" in response.data, "Did not find " \
                "<Response>: %s" % response.data)
        self.assertTrue("</Response>" in response.data, "Did not find " \
                "</Response>: %s" % response.data)
        self.assertEqual("200 OK", response.status)

    def sms(self, body, path='/sms', number='+15555555555'):
        params = {
            'SmsSid': 'SMtesting',
            'AccountSid': 'ACtesting',
            'From': number,
            'To': '+16666666666',
            'Body': body,
            'ApiVersion': '2010-04-01',
            'Direction': 'inbound'}
        return self.app.post(path, data=params)

    def call(self, path='/voice', number='+15555555555', digits=None):
        params = {
            'CallSid': 'CAtesting',
            'AccountSid': 'ACtesting',
            'From': number,
            'To': '+16666666666',
            'CallStatus': 'ringing',
            'ApiVersion': '2010-04-01',
            'Direction': 'inbound'}
        if digits:
            params['Digits'] = digits
        return self.app.post(path, data=params)


class Test_Voice(WebTest):
    def test_voice(self):
        response = self.call()
        self.assertTwiML(response)
        self.assertTrue("<Say" in response.data, "Did not find " \
                "intro text in response: %s" % response.data)
        self.assertTrue("<Gather" in response.data, "Did not find " \
                "<Gather> in response: %s" % response.data)
        self.assertTrue("action=\"/gather\"" in response.data, "Did not find " \
                "action attribute in response: %s" % response.data)
        self.assertTrue("<Redirect" in response.data, "Did not find " \
                "<Redirect> in response: %s" % response.data)

    def test_repeat(self):
        response = self.call('/gather', digits='1')
        self.assertTwiML(response)
        self.assertTrue(':' in response.data, "Did not find " \
                "repeated reason in response: %s" % response.data)

    def test_repeatHangup(self):
        response = self.call('/gather', digits='2')
        self.assertTwiML(response)
        self.assertTrue('<Hangup' in response.data, "Did not find " \
                "<Hangup> in response: %s" % response.data)

    def test_songsWrongInput(self):
        for i in range(5, 10):
            response = self.call('/gather', digits=str(i))
            self.assertTwiML(response)
            self.assertTrue("<Say" in response.data, "Did not find " \
                    "<Say> in response: %s" % response.data)

    def test_songsWeirdInput(self):
        characters = ["#", "*"]
        for character in characters:
            response = self.call('/gather', digits=character)
            self.assertTwiML(response)
            self.assertTrue("<Say" in response.data, "Did not find " \
                    "<Say> in response: %s" % response.data)


class Test_Sms(WebTest):
    def test_sms(self):
        response = self.sms("Testing.")
        self.assertTwiML(response)
        self.assertTrue(":" in response.data, "Did not find " \
                "a preface colon in response: %s" % response.data)

    def test_smsHelp(self):
        response = self.sms("help")
        self.assertTwiML(response)
        self.assertTrue("GIMME" in response.data, "Did not find " \
                "GIMME in response: %s" % response.data)


class Test_Web(WebTest):
    def test_index(self):
        response = self.app.get('/')
        self.assertTrue("</html>" in response.data, "Did not find " \
                "html tag close in response: %s" % response.data)

    def test_reaction(self):
        response = self.app.get('/reaction')
        self.assertTrue("</html>" in response.data, "Did not find " \
                "html tag close in response: %s" % response.data)


if __name__ == '__main__':
    unittest.main()
