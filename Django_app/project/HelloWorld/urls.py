from django.urls import path
from . import views  # . means impprt from ur project/app

urlpatterns = [
    path('hello/',views.Hello),   # '' means is the home page and the url is app level
    path('page/', views.page)
]
