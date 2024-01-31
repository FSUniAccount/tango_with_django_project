from django.contrib import admin
from django.urls import include, path
from  . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]