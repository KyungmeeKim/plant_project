from rest_framework import routers
from myapp import views
from django.urls import re_path, include,path
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'register', views.PostViewset)
router.register(r'profileimage', views.ImageViewset)
router.register(r'raspberry', views.PostViewset_raspberry)
router.register(r'waterdate', views.WaterViewset)




urlpatterns = [
    re_path(r'^',include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.Login),
    path('checkid/', views.CheckId),
    # path("profileimage/", views.post)
    path('userprofileimage/', views.UserProfileImage),
    path('', include('myapp.urls'))
    
    
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
