import graphene
from user.schema import Query as UserQueries, Mutation as UserMutations
from workshop.schema import Query as WorkshopQueries


class Mutation(
    UserMutations,
    graphene.ObjectType
):
    pass


class Query(
    UserQueries,
    WorkshopQueries,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)
