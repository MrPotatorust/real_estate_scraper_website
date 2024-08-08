from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'scraper_integration'
urlpatterns=[
    path('', views.main_page, name='main_page'),
    path('registration', views.registration, name='registration'),
    path('scraper', views.scraper, name='scraper'),
    path('results', views.results, name='results'),
    path('tables', views.view_tables, name='view_tables'),
    path('logout', LogoutView.as_view(next_page='scraper_integration:main_page'), name='logout'),
    path('password_reset', views.password_reset, name='password_reset'),
]