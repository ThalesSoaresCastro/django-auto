from django.conf.urls import url 
from . import views 
 
urlpatterns = [ 
    url(r'^product/all', views.product_list),
    url(r'^product/create', views.product_create),
    url(r'^product/(?P<id>[0-9]+)$', views.product_detail),
    url(r'^product/(?P<id>[0-9]+)/delete', views.product_delete),
    url(r'^product/(?P<id>[0-9]+)/change', views.product_change),
]