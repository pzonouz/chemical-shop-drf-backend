from users.models import CustomUser, UserProfile
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from users.serializers import CustomUserSerializer


def update_user_social_data(strategy, *args, **kwargs):
    if kwargs["is_new"]:
        response = kwargs["response"]
        user = kwargs["user"]
        if response["picture"]:
            url = response["picture"]
            userProfile_obj, created = UserProfile.objects.get_or_create(user=user)
            userProfile_obj.image = url
            userProfile_obj.save()


class UserAdminViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def update(self, request, *args, **kwargs):
        # instance = self.get_object()
        # serializer = self.get_serializer(instance, data=request.data)
        data = request.data
        profile_data = data["profile"]
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        profile = UserProfile.objects.get(id=request.user.profile.id)
        profile.first_name = profile_data["first_name"]
        profile.last_name = profile_data["last_name"]
        profile.address = profile_data["address"]
        profile.mobile = profile_data["mobile"]
        profile.save()
        return Response(status=status.HTTP_201_CREATED)
