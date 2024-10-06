from django.urls import path,include
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path ("news/",views.news,name="news"),
    path("shelter_info/<id>",views.info,name="info"),
    path("register/<id>",views.dec,name="register"),
]