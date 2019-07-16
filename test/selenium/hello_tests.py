from seleniumbase import BaseCase
import chromedriver_binary

class HelloTestClass(BaseCase):
    BASE_URL = 'http://127.0.0.1:8000/'

    def test_001_hello(self):
        self.open(self.BASE_URL + 'hello/')
        self.assert_text('Hello World!', 'body')