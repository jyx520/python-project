from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/list/', views.product_list, name='product_list'),
    url(r'^product/detail/(?P<pk>\S+)/$', views.product_detail, name='product_detail'),
]


