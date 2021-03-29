from rest_framework import routers
from accounts.viewsets import CustomUserViewsSets
from events.viewsets import EventsViewSets

router = routers.DefaultRouter()
router.register(r'customuser', CustomUserViewsSets)
router.register(r'events', EventsViewSets)