"""
URL configuration for HCI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from home.views import home_view
from login.views import login_view, postsign_view
from projects.views import all_view, id_view, loginView, registrationView, logoutView

urlpatterns = [
    path('', home_view, name='home'),

    # path('login/', login_view, name='login'),
    # path('postsign/', postsign_view, name='postsign'),

    path('register/', registrationView, name='registration'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),

    path('gallery/', all_view, name='gal'),
    path('gallery/<int:gal_id>/', id_view, name='idv'),
    # path('gallery/<int:gal_id>/u/<int:user_id>', id_view_logged, name='idvl'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    