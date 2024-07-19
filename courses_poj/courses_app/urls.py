from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('add_courses',views.add_courses),
    path('coursers/<int:id>/destroy',views.review_course),
    path('coursers/destroy', views.remove_course),
    path('course/<int:id>/comment/',views.comment),
    path('add_comment/<int:id>',views.add_comment)
]

