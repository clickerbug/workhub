from graphene_django.views import GraphQLView as BaseGraphQLView
from user.models import User


class AuthEmailBackend:
    @staticmethod
    def authenticate(request, username=None, password=None, **kwargs):
        if username is not None:
            try:
                user = User.objects.get(email__iexact=username)
            except User.DoesNotExist:
                return None
            else:
                if user.check_password(password) and user.is_active:
                    return user
        return None


# Overrides default GraphQL view, and allows custom APIException to be raised
class GraphQLView(BaseGraphQLView):
    @staticmethod
    def format_error(error):
        formatted_error = super(GraphQLView, GraphQLView).format_error(error)
        del formatted_error['locations']
        del formatted_error['path']
        try:
            formatted_error['context'] = error.original_error.context
        except AttributeError:
            pass

        return formatted_error


# Implements support for custom APIExceptions
class APIException(Exception):
    def __init__(self, message, code=None):
        self.context = {}
        if code:
            self.context['code'] = code
        super().__init__(message)
