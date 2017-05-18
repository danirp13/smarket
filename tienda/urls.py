from django.conf.urls import  url
from tienda import views

urlpatterns =[


	#------------------------------------categoria-------------------------------------#
	url(r'^$', views.base, name='base'),
	url(r'^categoria/$', views.CategoriaListView.as_view(), name='categoria-list'),
	url(r'^categoria/(?P<pk>[0-9]+)/detail/$', views.CategoriaDetailView.as_view(), name='categoria-detail'),
	url(r'^categoria/(?P<pk>[0-9]+)/update/$', views.CategoriaUpdate.as_view(), name='categoria-update'),
	url(r'^categoria/(?P<pk>[0-9]+)/delete/$', views.CategoriaDelete.as_view(), name='categoria-delete'),
	url(r'^categoria/create/$', views.CategoriaCreate.as_view(), name='categoria-create'),

	#----------------------------------productos----------------------------------------#

	url(r'^producto/$', views.ProductoListView.as_view(), name='producto-list'),
	url(r'^producto/(?P<pk>[0-9]+)/detail/$', views.ProductoDetailView.as_view(), name='producto-detail'),

]	