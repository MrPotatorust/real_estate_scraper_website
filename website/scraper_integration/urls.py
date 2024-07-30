from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'scraper_integration'
urlpatterns=[
    path('', views.main_page, name='main_page'),
    path('registration', views.registration, name='registration'),
    path('scraper', views.scraper, name='scraper'),
    path('logout', LogoutView.as_view(next_page='scraper_integration:main_page'), name='logout'),
]