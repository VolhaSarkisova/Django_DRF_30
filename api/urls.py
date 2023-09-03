from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import *

# router = SimpleRouter()
# router.register('products', ProductViewSet)

urlpatterns = [
    path('products/', ProductApiView.as_view()),
    path('categories/', CategoryApiView.as_view()),
    path('ratings/', RatingApiView.as_view()),
    path('comments/', CommentApiView.as_view()),
    path('select/', RatingCommentApiView.as_view())
]
              # + router.urls