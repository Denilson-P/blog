from rest_framework.routers import SimpleRouter

from .views import (
    UserViewSet,
    PostViewSet,
    ImageViewSet,
    CategoryViewSet,
    CommentViewSet,
    LikeViewSet,
)

router = SimpleRouter()
router.register("users", UserViewSet)
router.register("posts", PostViewSet)
router.register("images", ImageViewSet)
router.register("categories", CategoryViewSet)
router.register("comments", CommentViewSet)
router.register("likes", LikeViewSet)
