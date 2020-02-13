from django.urls import path
from .views import HomeView, GetNewsView, HelpView

urlpatterns = [
    path('', HomeView.home),
    path('home', HomeView.home),
    path('get_news', GetNewsView.get_news),
    path('help', HelpView.help_),
]