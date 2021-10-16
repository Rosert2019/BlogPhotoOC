from django.urls import path
import authentication.views

urlpatterns = [
   
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('profile-photo/', authentication.views.upload_profile_photo,
         name='upload_profile_photo'),
]