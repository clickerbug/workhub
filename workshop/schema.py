import graphene
from graphql_jwt.decorators import login_required

from workshop.models import Workshop, Topic


class TopicObj(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    slug = graphene.String()


class WorkshopObj(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    topics = graphene.List(TopicObj)

    def resolve_topics(self, info):
        return self.topics.all()


class Query(graphene.ObjectType):
    getTopics = graphene.List(TopicObj)
    getWorkshops = graphene.List(WorkshopObj)
    getRecommendedWorkshops = graphene.List(WorkshopObj)

    def resolve_getTopics(self, info):
        return Topic.objects.all()

    def resolve_getWorkshops(self, info):
        return Workshop.objects.all()

    @login_required
    def resolve_getRecommendedWorkshops(self, info):
        user = info.context.user
        topics = user.interestedTopics.all()
        if len(topics) > 0:
            return Workshop.objects.filter(topics__in=topics).distinct()
        else:
            return Workshop.objects.all()
