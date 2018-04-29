from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('', views.text, name="text"),
    url('contact/', views.contact, name="contact"),
]
