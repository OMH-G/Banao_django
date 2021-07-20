from django.urls import path 
from . views import index,success,view
app_name='loginapp'
urlpatterns=[
    path('',index,name='sign'),
    path('check/',success,name='success'),
    path('view',view,name='view'),
]