import unittest
import xmlrunner
import app
import re

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):

        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

        # searching for <h1> tag in the application data using regex

        message = rv.data.decode()
        start = re.search("<h1>",message).start()
        end = re.search("</h1>",message).start()
        message = message[start+4:end]

        self.assertEqual(message, "hello brother, Lets have some fun!!")

    def test_name(self):

        name = 'alice'
        rv = self.app.get(f'/{name}')
        self.assertEqual(rv.status, '200 OK')

        # searching for <h1> tag in the application data using regex

        message = rv.data.decode()
        start = re.search("<h1>",message).start()
        end = re.search("</h1>",message).start()
        message = message[start+4:end]

        self.assertEqual(message, "alice: A nerd")

if __name__ == '__main__':

    ############# To Generate Test Reports  #############
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    #####################################################
    unittest.main()