from django.test import TestCase
from time import strftime

class HelloClientTest(TestCase):
    def test_hello_001(self):
        response = self.client.get('/hello/')
        self.assertContains(response, 'Hello World!')

    def test_hello_002(self):
        response = self.client.get('/hello/template/')
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, '<title>変数の練習</title>', html=True)
        self.assertContains(response, '{}時です。'.format(strftime('%H')))
        self.assertContains(response, 'Sample message')
        self.assertContains(response, 'hello_world')
        self.assertContains(response, 'template')
        self.assertContains(response, 'if')
        self.assertContains(response, 'for')

    def test_hello_003(self):
        response = self.client.get('/hello/if/')
        self.assertTemplateUsed(response, 'if.html')
        self.assertContains(response, 'is_visibleがFalseなので表示します。')
        self.assertContains(response, 'empty_strが空です。')

    def test_hello_005(self):
        response = self.client.get('/hello/for/')
        self.assertTemplateUsed(response, 'for.html')
        self.assertContains(response, 0)
        self.assertContains(response, 1)
        self.assertContains(response, 2)
        self.assertContains(response, 3)
        self.assertContains(response, 4)
        self.assertContains(response, 5)
        self.assertContains(response, 6)
        self.assertContains(response, 7)
        self.assertContains(response, 8)
        self.assertContains(response, 9)
        

    def test_hello_006(self):
        response = self.client.get('/hello/get/')
        assert response.status_code == 200

    def test_hello_007(self):
        response = self.client.get('/hello/forms/')
        assert response.status_code == 200

    def test_hello_008(self):
        response = self.client.get('/hello/forms_sample/')
        assert response.status_code == 200

    def test_hello_009(self):
        response = self.client.get('/hello/models/')
        assert response.status_code == 200