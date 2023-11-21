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
# from login.views import login_view, postsign_view
from projects.views import sdc_all_view, pd_all_view, at_all_view, sdc_id_view, pd_id_view, at_id_view, sdc_toggle_like, pd_toggle_like, at_toggle_like, loginView, registrationView, logoutView

urlpatterns = [
    path('', home_view, name='home'),

    # path('login/', login_view, name='login'),
    # path('postsign/', postsign_view, name='postsign'),

    path('register/', registrationView, name='registration'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),

    path('gallery/sdc', sdc_all_view, name='gal'),
    path('gallery/pd', pd_all_view, name='gal'),
    path('gallery/at', at_all_view, name='gal'),

    path('gallery/sdc/<int:gal_id>/', sdc_id_view, name='idv'),
    path('like/sdc/<int:gal_id>', sdc_toggle_like, name="like"),
    
    path('gallery/pd/<int:gal_id>/', pd_id_view, name='idv'),
    path('like/pd/<int:gal_id>', pd_toggle_like, name="like"),
    
    path('gallery/at/<int:gal_id>/', at_id_view, name='idv'),
    path('like/at/<int:gal_id>', at_toggle_like, name="like"),
    
    # path('gallery/<int:gal_id>/u/<int:user_id>', id_view_logged, name='idvl'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    