from users.models import UserProfile
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated


from users.serializers import UserProfileSerializer


def update_user_social_data(strategy, *args, **kwargs):
    if kwargs["is_new"]:
        response = kwargs["response"]
        user = kwargs["user"]
        if response["picture"]:
            url = response["picture"]
            userProfile_obj, created = UserProfile.objects.get_or_create(user=user)
            userProfile_obj.image = url
            userProfile_obj.save()


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


class UserAdminViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    # queryset = CustomUser.objects.all()
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # def update(self, request, *args, **kwargs):
    #     data = request.data
    #     profile_data = data["profile"]
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     profile = UserProfile.objects.get(id=request.user.profile.id)
    #     profile.first_name = profile_data["first_name"]
    #     profile.last_name = profile_data["last_name"]
    #     profile.address = profile_data["address"]
    #     profile.mobile = profile_data["mobile"]
    #     profile.save()
    #     return Response(status=status.HTTP_201_CREATED)
