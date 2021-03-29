from rest_framework import routers
from accounts.viewsets import CustomUserViewsSets
from events.viewsets import EventsViewSets
from payment.viewsets import PaymentViewSets

router = routers.DefaultRouter()
router.register(r'customuser', CustomUserViewsSets)
router.register(r'events', EventsViewSets)
router.register(r'payment', PaymentViewSets)