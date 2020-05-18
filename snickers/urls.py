from django.urls import path
from .views import HomeView, AboutView, TestView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('test/', TestView.as_view(), name = 'test'),

]
