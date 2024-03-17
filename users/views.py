from users.models import CustomUser


def update_user_social_data(strategy, *args, **kwargs):
    # if kwargs["is_new"]:
    response = kwargs["response"]
    user = kwargs["user"]
    if response["picture"]:
        url = response["picture"]
        userProfile_obj = CustomUser.objects.get(pk=user.id)
        userProfile_obj.image = url
        userProfile_obj.save()
