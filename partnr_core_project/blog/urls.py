from django.urls import path, include
from .models import *
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('blogs', BlogViewset, basename='blog' )

urlpatterns = [
    path('', include(router.urls)),
    path('comment/', CommentView.as_view(), name="comment"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('token/', views.obtain_auth_token),

]