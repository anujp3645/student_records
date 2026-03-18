"""
URL configuration for student_records project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login', login, name='login'),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('adminhome', adminhome, name='adminhome'),
    path('add_stu', add_stu, name="add_stu"),
    path('view_student', view_stu, name="view_stu"),
    path('del_stu/<int:id>', del_stu, name="del_stu"),
    path('edit_stu/<int:id>', edit_stu, name="edit_stu"),
    path('search', search_stu, name='search_stu'),
    path('change_pass', change_pass, name="change_pass"),
    path('feedback/', feedback, name='feedback'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
