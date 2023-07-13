from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservations_eq/', views.reservations_eq, name='reservations_eq'),
    path('reservations_eq_date/', views.reservations_eq_date, name='reservations_eq_date'),
    path('reservations_eq_finalize/', views.reservations_eq_finalize, name='reservations_eq_finalize'),
    path('reservations_tracks/', views.reservations_tracks, name='reservations_tracks'),
    path('reservations_tracks_date/', views.reservations_tracks_date, name='reservations_tracks_date'),
    path('reservations_tracks_finalize/', views.reservations_tracks_finalize, name='reservations_tracks_finalize'),
    path('reservations_show_all/', views.reservations_show_all, name='reservations_show_all'),
    path('reservations_show_user/', views.reservations_show_user, name='reservations_show_user'),
    path('reservations_tracks_add/', views.reservations_tracks_add, name='reservations_tracks_add'),
    path('work/', views.work, name='work'),
    path('storage/', views.storage, name='storage'),
    path('work_show/', views.work_show, name='work_show'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.account, name='account'),
    path('account_change_password/', views.account_change_password, name='account_change_password'),
    path('account_change_email/', views.account_change_email, name='account_change_email'),
]


