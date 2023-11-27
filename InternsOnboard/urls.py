from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from userRegister import views as user_views
# from coordinatorPortal import views as coordinator_views
from django.conf import settings
from studentPortal import views as student_views
from  django.conf.urls.static import static #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user_views.register,name="Register"),
    path('register/', user_views.register,name="Register"),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='userRegister/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userRegister/logout.html'), name='logout'),
    path('', include('InternsOnboardMain.urls')),
    path('', include('coordinatorPortal.urls')),
    # path('api/posts/', include('coordinatorPortal.urls')),
    path('apply/',student_views.apply,name='student-apply'),
    # path('accept/', coordinator_views.accept, name="internship-accept"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)