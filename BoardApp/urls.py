from django.conf.urls import url
from django.urls import path, include
from .views import  Board_View, board_topics, topic_posts, new_topic

urlpatterns = [
    path('', Board_View, name='board_index'),
    url(r'^(?P<pk>\d+)/topics/$', board_topics , name="board_topics"),
    url(r'^(?P<pk>\d+)/posts/$', topic_posts, name="topic_posts" ),
    url(r'^(?P<pk>\d+)/new_topic/', new_topic, name='new_topic'),
    # path('', Board_View.as_view(), name='view_index' ),
   # url(r'board/(?P<pk>\d+)', BoardDetailView.as_view(), name="board_detail")
]
