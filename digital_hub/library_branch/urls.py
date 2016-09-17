from django.conf.urls import url
from library_branch import views

urlpatterns = [
    url(r'^branches$', views.branches),
    url(r'^$', views.index, name='index'),
]
