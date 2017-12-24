from django.conf.urls import url
from . import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /ans/question/1
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # /ans/question/userid
    url(r'^question/user/(?P<userid>[0-9]+)/$', views.asked_by_me, name='asked_by_me'),

    # /ans/answer/username
    url(r'^answer/user/(?P<userid>[0-9]+)/$', views.answered_by_me, name='answered_by_me'),


    url(r'^upvote/user/(?P<userid>[0-9]+)/$', views.upvoted_by_me, name='upvoted_by_me'),

    # /question/hour
    url(r'^question/hour/$', views.question_of_hour, name='question_of_hour'),
    url(r'^question/site/$', views.question_of_the_site, name='question_of_site'),

    # url(r'^answer/(?P<answer_id>[0-9]+)/votes$', views.vote, name='vote'),

]
