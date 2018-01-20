from django.conf.urls import url
from . import views

urlpatterns = [
    # /msgboard/
    url(r'^$', views.index, name='index'),

    # /msgboard/3/
    url(r'^(?P<board_id>[0-9]+)/$', views.topics, name='topics'),
]