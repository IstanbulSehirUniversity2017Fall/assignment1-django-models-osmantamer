from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.main_page, name='index'),
    url(r'^(?P<mycar>[a-z]+)/$', views.my_details, name='index'),
]
