from django.urls import path 
from . import views
app_name = "login"

urlpatterns = [
    path('' , views.signin , name="signin"),
    path('register/' ,  views.register , name="register"),
    path('profile/' , views.profile_page , name='profile'),
    path('logout/' , views.logout_page , name="logout"),
    path('update_profile' , views.update_profile , name='update')
]

