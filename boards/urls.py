from django.conf.urls import patterns, url

from boards import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.org_staff, name='staff'),
    url(r'^person/(\d+)/$', views.member_of, name='memberships'),
    url(r'^ajah/', views.ajah_staff, name='ajah'),
)