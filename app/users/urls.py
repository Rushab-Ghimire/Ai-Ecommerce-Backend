from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.api_root),
    path('register/', views.RegisterView.as_view(), name='sign-up'),
    path('me/',views.ProfileView.as_view(), name='user-profile'),
    path('api-auth/', include('rest_framework.urls')),

]