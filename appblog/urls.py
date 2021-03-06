from django.urls import path
from .views import *

app_name = 'appblog'
urlpatterns = [
    path('' , home , name = 'list'),
    path('create' , create , name = 'create'),
    path('update/<id>' , update , name = 'update'), 
    path('delete/<id>' , delete , name = 'delete'),
    path('detail/<id>' , detail , name = 'detail'),
    path('like/<id>' , like , name = 'like'),
    path('unlike/<id>' , unlike , name = 'unlike'),
    path('likes' , likes , name = 'likes'),
    path('saved/<id>' , saved , name = 'saved'),
    path('unsaved/<id>' , unsaved , name = 'unsaved'),
    path('saveds' , saveds , name = 'saveds'),
]