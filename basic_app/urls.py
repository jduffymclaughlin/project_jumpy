from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^what_we_do/$', views.what_we_do, name='what_we_do'),
    url(r'^service_pricing/$', views.service_pricing, name='service_pricing'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact2/$', views.contact, name='contact2')
]
