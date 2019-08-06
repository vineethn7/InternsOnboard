from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from userRegister import views as user_views
from coordinatorPortal import views as views_coordinatorPortal
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from InternsOnboardMain import views

urlpatterns = [
    path('', include('InternsOnboardMain.urls')),
    path('', include('studentPortal.urls')),
    path('admin/', admin.site.urls),
    path('api/',views.internshipPostList.as_view()),
    path('signup/', user_views.register,name="Register"),
    path('register/', user_views.register,name="Register"),
    path('profile/', user_views.profile, name='profile'),
    path('post/', views_coordinatorPortal.post, name="Test-Post"),
    path('login/', auth_views.LoginView.as_view(template_name='userRegister/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userRegister/logout.html'), name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
