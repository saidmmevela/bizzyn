"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from test_app.views import Sample,SampleGeneric,SampleGenericUpdate,SampleViewSet,UserGeneric,LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("simple-viewset",SampleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', Sample.as_view()),
    path('sample/<int:id>', Sample.as_view()),
    path('sample-generic', SampleGeneric.as_view()),
    path('register', UserGeneric.as_view()),
    path('login', LoginView.as_view()),
    path('sample-generic/<int:id>', SampleGenericUpdate.as_view()),
    path('', include(router.urls))
]
