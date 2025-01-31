from django.urls import path
from . import views
from .views import SearchResultsView

app_name = 'newsapp2'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news-detail/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('skincare/', views.SkinCareView.as_view(), name='skincare'),
    path('coordination_list/', views.CoordinationListView.as_view(), name='coordination_list'),
    path('horror_list/', views.HorrorListView.as_view(), name='horror_list'),
    path('lifehack_list/', views.LifehackListView.as_view(), name='lifehack_list'),
    path('skincare_list/', views.SkinCareListView.as_view(), name='skincare_list'),
    path('sweets_list/', views.SweetsListView.as_view(), name='sweets_list'),
    path('zoo_list/', views.ZooListView.as_view(), name='zoo_list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
