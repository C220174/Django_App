from django.contrib import admin
from django.urls import path, include
from . import views as project_views
from HelloWorld import views as hello_views# u can import views from app level to not use include()
#http request and response are handled at urls at project level
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_views.Hello),
    path('page/', hello_views.page)  ,
    path('bye/', project_views.Bye) ,
]

# to access each url u can <ip address>/hello/
