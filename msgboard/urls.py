from django.conf.urls import url
from . import views

app_name = 'msgboard'

urlpatterns = [
    # /msgboard/
    url(r'^$', views.index, name='index'),

    # /msgboard/3/
    url(r'^(?P<board_id>[0-9]+)/$', views.topics, name='topics'),

    # /msgboard/3/1
    url(r'^(?P<board_id>[0-9]+)/(?P<topic_id>[0-9]+)/$', views.messages, name='messages'),
]