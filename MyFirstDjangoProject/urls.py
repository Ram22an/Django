"""
URL configuration for MyFirstDjangoProject project.

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
from . import views  # Importing views from the current directory

from django.conf import settings
from django.conf.urls.static import static
# **this is the importing of static files and urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home) ,

    # ⬆️mean this is what we will see as default

    # path('home/',views.home)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# **adding this line ⬆️ we can access the media files


# urls stands for universal resource locator
# it contain all the endpoints that we should have in our website
# it is used to provide address of the resources (images, web pages, websites)
# it tell django if a user comes with this specific url direct them to the particular resource

