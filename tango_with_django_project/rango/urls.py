from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    # below is for adding a category
    url(r'add_category/$', views.add_category, name='add_category'),
    # below is for adding pages to a category
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),
    # below is for showing a category
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
]