from django.test import TestCase
from time import strftime
from hello.models import Hello

class HelloClientTest(TestCase):
    fixtures = ['hello_test_data.json']

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
        

    def test_hello_006_01(self):
        response = self.client.get('/hello/get/')
        self.assertTemplateUsed(response, 'get_query.html')
        self.assertNotContains(response, 'さん、こんにちは。')

    def test_hello_006_02(self):
        response = self.client.get('/hello/get/', {'your_name': 'Tommy'})
        self.assertTemplateUsed(response, 'get_query.html')
        self.assertContains(response, 'Tommyさん、こんにちは。')

    def test_hello_007_01(self):
        response = self.client.get('/hello/forms/')
        self.assertTemplateUsed(response, 'forms.html')
        self.assertContains(response, 'データ検証に失敗しました')

    def test_hello_007_02(self):
        response = self.client.get('/hello/forms/', {'your_name': ""})
        self.assertTemplateUsed(response, 'forms.html')
        self.assertContains(response, 'データ検証に失敗しました')
        self.assertFormError(response, 'form', 'your_name', 'このフィールドは必須です。')

    def test_hello_007_03(self):
        response = self.client.get('/hello/forms/', {'your_name': "Tommy"})
        self.assertTemplateUsed(response, 'forms.html')
        self.assertNotContains(response, 'データ検証に失敗しました')
        self.assertContains(response, 'データ検証に成功しました')
        self.assertFormError(response, 'form', 'your_name', None)

    def test_hello_008_01(self):
        response = self.client.get('/hello/forms_sample/')
        self.assertTemplateUsed(response, 'form_samples.html')
        self.assertFormError(response, 'form', 'age', None)
        self.assertFormError(response, "form", "birthday", None)
        self.assertFormError(response, "form", "send_message", None)
        self.assertFormError(response, "form", "gender_r", None)
        self.assertFormError(response, "form", "gender_s", None)
        self.assertFormError(response, "form", "food_s", None)
        self.assertFormError(response, "form", "food_c", None)

    def test_hello_009_01(self):
        response = self.client.get('/hello/models/')
        self.assertTemplateUsed(response, 'models.html')
        self.assertFormError(response, 'form', 'your_name', None)
        self.assertContains(response, "Becky")
        self.assertContains(response, "Paul")

    def test_hello_009_02(self):
        response = self.client.post(
            '/hello/models/',
            {
                "your_name": ""
            }
        )
        self.assertTemplateUsed(response, 'models.html')
        self.assertFormError(response, 'form', 'your_name', "このフィールドは必須です。")

    def test_hello_009_03(self):
        response = self.client.post(
            '/hello/models/',
            {
                "your_name": "Peddy"
            }
        )
        self.assertRedirects(response, '/hello/models/')

        response2 = self.client.get('/hello/models/')
        self.assertContains(response2, "Becky")
        self.assertContains(response2, "Paul")
        self.assertContains(response2, "Peddy")
