from rest_framework import routers
from accounts.viewsets import CustomUserViewsSets

router = routers.DefaultRouter()
router.register(r'customuser', CustomUserViewsSets)