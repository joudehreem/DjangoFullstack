from django.urls import path
from . import views
urlpatterns = [
    path('',views.redirect_shows),
    path('shows/',views.index),
    # path('shows/new/',views.new_show),
    path('shows/create',views.create_show,),
    path('shows/<int:id>/',views.tv_show),  
    path('shows/<int:id>/edit/',views.edit),
    path('shows/<int:id>/update/', views.update_show),
    path('shows/<int:id>/destroy/',views.destroy)


]