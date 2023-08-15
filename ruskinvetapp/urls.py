from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
  #  path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('integration/',views.integration,name='integration'),
    path('pets/',views.pets,name='pets'),
    path('calendar/',views.calendar,name='calendar'),
    path('pet_parents/',views.pet_parents,name='pet_parents'),
    path('visit/<int:pk>',views.customer_visit,name='visit'),
    path('visit_home/',views.visit_home,name='visit_home'),
    path('api', views.api_call, name='api-call'),
]