from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_homepage, name='home_page_path'),
    path('gallery', views.view_gallery_page, name='gallery_path'),
    path('<int:series_number>', views.redirect_series_number_handler),
    path('series', views.view_series_page, name='series_path'),
    path('<series_name>', views.series_description_page, name='series_name_path'),

]