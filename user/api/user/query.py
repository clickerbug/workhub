import graphene
from graphql_jwt.decorators import login_required

from user.models import User
from workshop.schema import TopicObj


class Query(graphene.ObjectType):
    isUsernameAvailable = graphene.Boolean(username=graphene.String(required=True))
    myTopics = graphene.List(TopicObj)

    @staticmethod
    def resolve_isUsernameAvailable(self, info, **kwargs):
        username = kwargs.get('username')
        try:
            User.objects.get(username=username)
            return False
        except User.DoesNotExist:
            return True

    @login_required
    def resolve_myTopics(self, info):
        user = info.context.user
        return user.interestedTopics.all()