from django.urls import path
from django.conf.urls.static import static
import blog.views

urlpatterns = [
    path('', blog.views.home, name='home'),
    path('upload/', blog.views.photo_upload, name='photo_upload'),
    path('create/', blog.views.blog_and_photo_upload, name='blog_create'),
    path('<int:blog_id>/', blog.views.view_blog, name='view_blog'),
    path('posted/', blog.views.mes_postes, name='mes_postes'),
    path('<int:blog_id>/edit', blog.views.edit_blog, name='edit_blog'),
    path('upload-multiple/', blog.views.create_multiple_photos,name='create_multiple_photos'),
    path('follow-users/', blog.views.follow_users, name='follow_users'),


    ]