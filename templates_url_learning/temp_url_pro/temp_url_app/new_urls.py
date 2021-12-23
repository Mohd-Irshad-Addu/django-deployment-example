from django.conf.urls import url
from temp_url_app import views

#TEMPLATE TAG
app_name = 'temp_url_app' #this is the name of our Application

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    url(r'^thank_you/$',views.thank_you,name='thanks')
]
