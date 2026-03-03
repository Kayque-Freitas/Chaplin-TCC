from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('docs/', views.docs_view, name='docs'),
    path('demo/', views.demo_view, name='demo'),
    path('slides/', views.slides_view, name='slides'),
    path('resources/', views.resources_view, name='resources'),
    path('sitemap/', views.sitemap_view, name='sitemap'),
]
