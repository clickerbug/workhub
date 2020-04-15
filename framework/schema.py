import graphene
from user.schema import Query as UserQueries, Mutation as UserMutations


class Mutation(
    UserMutations,
    graphene.ObjectType
):
    pass


class Query(
    UserQueries,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)
