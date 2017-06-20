from django.conf.urls import url 
from library import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 
	url(r'^$', views.index, name='index'),
	url(r'^browse', views.browse, name='browse'),	
	url(r'^checked_out', views.checked_out, name='checked_out'),
	url(r'^add_user/$', views.add_user, name='add_user'),
	url(r'^add_item/$', views.add_item, name='add_item'),
	url(r'^search/$', views.search, name='search'),
	url(r'^item/(?P<item_name_slug>[\w\-]+)/$', views.show_item, name='show_item'),
	url(r'^check_out/(?P<item_name_slug>[\w\-]+)/$', views.check_out, name='check_out'),
	url(r'^check_in/(?P<item_name_slug>[\w\-]+)/$', views.check_in, name='check_in'),
]
