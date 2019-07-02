from django.urls import path
from . import views

app_name='hello'
urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('template/', views.hello_template, name='hello_template'),
    path('if/', views.hello_if, name='hello_if'),
    path('for/', views.hello_for, name='hello_for'),
    path('get/', views.hello_get_query, name="hello_get_query"),
    path('forms/', views.hello_forms, name="hello_forms"),
    path('forms_sample/', views.hello_forms2, name="hello_forms2"),
    path('models/', views.hello_models, name="hello_models"),
]