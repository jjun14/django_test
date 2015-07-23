from django.conf.urls import patterns, url
from apps.products import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^add_product', views.add, name='add'),
    url(r'^delete_product/(?P<product_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^update_product/$', views.update, name='update'),
)
