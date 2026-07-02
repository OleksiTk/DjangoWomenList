from django.urls import include, path
from . import views
urlpatterns = [
 
    path('', views.index, name='home'),
    path('cats/<slug:cat_slug>/', views.cats, name='cats')
]