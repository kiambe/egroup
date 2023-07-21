from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetDoneView

urlpatterns = [
    path('',views.dashboard, name="dashboard"),
   # path('register/',views.SignupView,name="register"),
    #path('logout/',views.UserLogout.as_view(),name="logout"),
    #path('profile/',views.UserProfile,name="user_view"),

    # path('dash/<int:cid>/',views.dashboard_data,name = "dash-price-data")
  
    # path('logout/',a)
   
    
]





