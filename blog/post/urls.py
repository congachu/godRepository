from django.urls import path, include
from .views import PostView, CommentView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostView, basename='')
router.register(r'comment', CommentView, basename='comment')

urlpatterns = [
    path("", include(router.urls)),
]


