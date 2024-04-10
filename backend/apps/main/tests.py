from django.contrib.auth import get_user_model

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from django.contrib.auth.models import User
from .models import (
    Category,
    Thing,
    Image,
    UserProfile,
    Trade,
    Feedback,
)

from ...api.main.views import (
    UserViewSet,
    CategoryViewSet,
    ThingViewSet,
    UserProfileViewSet,
    TradeViewSet,
    FeedbackViewSet,
    ImageViewSet
)

User = get_user_model()
User.objects.filter(username="admin").exists() or User.objects.create_superuser(
    "admin", "admin@example.com", "admin"
)

factory = APIRequestFactory()
user = User.objects.get(username="admin")
view = ThingViewSet.as_view()

# Make an authenticated request to the view...
request = factory.get("/api/v1/thing")
force_authenticate(request, user=user)
response = view(request)
