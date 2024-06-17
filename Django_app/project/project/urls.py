from django.contrib import admin
from django.urls import path, include
from HelloWorld import views # u can import views from app level to not use include()
#http request and response are handled at urls at project level
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.Hello),
    path('page/', views.page)  
]

# to access each url u can <ip address>/hello/
