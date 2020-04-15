import graphene
import graphql_jwt

from user.api.user.objects import UserObj
from user.api.user.query import Query as UserQueries
from user.api.user.mutations import Mutation as UserMutations


class ObtainJSONWebToken(graphql_jwt.relay.JSONWebTokenMutation):
    user = graphene.Field(UserObj)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class Mutation(
    UserMutations,
    graphene.ObjectType
):
    tokenAuth = ObtainJSONWebToken.Field()
    verifyToken = graphql_jwt.Verify.Field()
    refreshToken = graphql_jwt.Refresh.Field()


class Query(
    UserQueries,
    graphene.ObjectType
):
    pass
