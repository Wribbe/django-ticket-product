from django.conf.urls import url

from . import views

urlpatterns = [
        #url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^$', views.test, name='test'),
        ]

app_name = 'polls'
urlpatterns = [
        #url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^$', views.test, name='test'),
        url(r'name$', views.get_name, name='name'),
        url(r'test$', views.test, name='test'),
        url(r'your-name/$', views.get_name, name='your-name'),
        url(r'names_and_files$', views.get_name_and_file, name='Name and file'),
#        url(r'thanks/$', views.thanks, name='thanks'),
        url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        ]
#urlpatterns = [
#        url(r'^$', views.index, name = 'index'),
#        url(r'^(?P<question_id>[0-9]+)/$', views.detail,
#            name='detail'),
#        url(r'^(?P<question_id>[0-9]+)/results/$', views.results,
#            name='results'),
#        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote,
#            name='vote'),
#        ]
