# from datetime import timedelta
from datetime import timedelta
from django.http import HttpResponse
import requests
from rest_framework.views import APIView
from rest_framework_simplejwt import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class AuthActivation(APIView):
    def get(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        if (result.ok):
            result = '''
            <html>
            <body>
            <a href='http://localhost:3000/auth/login'>فعالسازی شما با موفقیت انجام شد. برای ادامه کلیک کنید</a>
            </body>
            </html>'''
            return HttpResponse(result)
        return HttpResponse(result.text)


class LoginView(views.TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        data = serializer.validated_data
        response = Response(data,
                            status=status.HTTP_200_OK)
        response.set_cookie(
            key="access", value=data["access"], domain=None,
            path="/",
            expires=timedelta(days=1),
            secure=False,
            httponly=True,
            samesite=None,)

        return response
