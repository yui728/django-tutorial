from django.db import models

class Customer(models.Model):
    # id = AutoField(primary_key = True) # 自動的に追加されるので定義不要
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=255, unique=True)
    memo = models.TextField(null=True)

class Hello(models.Model):
    your_name = models.CharField(max_length=10)

    def __str__(self):
        return '<0>'.format(self.your_name)
