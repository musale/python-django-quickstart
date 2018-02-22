from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from todos import views

urlpatterns = {
    url(r'^$', views.TodoList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.TodoDetail.as_view(), name='details'),
    url(r'^delete/$', views.TodosDeleteAll.as_view(), name='delete_all')
}

urlpatterns = format_suffix_patterns(urlpatterns)
