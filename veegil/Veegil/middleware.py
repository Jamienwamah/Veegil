from django.utils.deprecation import MiddlewareMixin
from signin.models import AccessToken

class AccessTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            access_token_obj = AccessToken.objects.latest('created_at')
            access_token = access_token_obj.token
        except AccessToken.DoesNotExist:
            access_token = None

        if access_token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
