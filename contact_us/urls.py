from django.conf.urls import url
from contact_us import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^formpage/$', views.form_name_view, name='form_name')

]
