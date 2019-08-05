from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from InternsOnboardMain import views

urlpatterns = [
    path('', include('InternsOnboardMain.urls')),
    path('', include('studentPortal.urls')),
    path('admin/', admin.site.urls),
    path('api/',views.internshipPostList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
