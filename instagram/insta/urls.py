from django.conf.urls import url
from . import views
from .views import IndexView

app_name = 'insta'

# add app urls here
urlpatterns =[
    url(r'^$', IndexView.as_view(), name ='index'),
    
]
