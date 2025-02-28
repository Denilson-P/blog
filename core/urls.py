from rest_framework.routers import SimpleRouter

from .views import (
    UserViewSet,
    PostViewSet,
    CategoryViewSet,
    CommentViewSet,
    LikeViewSet,
)

router = SimpleRouter()
router.register("users", UserViewSet)
router.register("posts", PostViewSet)
router.register("categories", CategoryViewSet)
router.register("comments", CommentViewSet)
router.register("likes", LikeViewSet)
