from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import UserProfile
from users.serializers import UserProfileSerializer


def update_user_social_data(**kwargs):
    if kwargs["is_new"]:
        response = kwargs["response"]
        user = kwargs["user"]
        if response["picture"]:
            url = response["picture"]
            user_profile_obj, _ = UserProfile.objects.get_or_create(user=user)
            user_profile_obj.image = url
            user_profile_obj.save()


class UserProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


class UserProfileAdminViewSet(ModelViewSet):
    # def get_queryset(self):
    #     return UserProfile.objects.filter(user_id=self.kwargs["pk"])

    permission_classes = [IsAdminUser]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
