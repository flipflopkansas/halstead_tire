from django.conf.urls import url
from services_app import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
]
