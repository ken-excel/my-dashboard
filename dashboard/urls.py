from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.PCMonitorView.as_view(), name='pcmonitor'),
    path('pcmonitor/', views.PCMonitorView.as_view(), name='pcmonitor'),
    path('crypto/', views.CryptoView.as_view(), name="crypto"),
    path('spotify/', views.SpotifyView.as_view(), name="spotify")
]