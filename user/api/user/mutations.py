import graphene
from django.db.models import Q
from graphql_jwt.decorators import login_required

from framework.utils.graphql import APIException
from user.api.user.objects import UserObj
from user.models import User
from user.utils.generators import generate_username_from_email, generate_password
from workshop.models import Topic


class UserRegistrationObj(graphene.ObjectType):
    returning = graphene.Field(UserObj)
    status = graphene.Boolean()


class RegisterUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=False)
        username = graphene.String(required=False)
        firstName = graphene.String(required=False)
        lastName = graphene.String(required=False)

    Output = UserRegistrationObj

    @staticmethod
    def mutate(self, info, email, password=None, username=None, firstName=None, lastName=None):
        try:
            user = User.objects.get(Q(username=username) | Q(email=email))
            if user.username == username:
                raise APIException('Username already taken.', code='USERNAME_TAKEN')
            raise APIException('An account with this email already exist.', code='EMAIL_IN_USE')
        except User.DoesNotExist:
            name = username
            if name is None:
                name = generate_username_from_email(email)
            pwd = password
            if password is None:
                pwd = generate_password()
            fn = firstName
            if fn is None:
                fn = name
            ln = lastName
            if ln is None:
                ln = ''
            user = User(
                first_name=fn,
                last_name=ln,
                email=email,
                username=name,
            )
            user.set_password(pwd)
            user.save()
            return UserRegistrationObj(
                returning=user,
                status=True
            )


class AddUserTopics(graphene.Mutation):
    class Arguments:
        topicID = graphene.Int(required=True)

    Output = graphene.Boolean

    @login_required
    def mutate(self, info, topicID):
        user = info.context.user
        if user.is_authenticated:
            topic = Topic.objects.get(id=topicID)
            user.interestedTopics.add(topic)
            user.save()
            return True
        else:
            return False


class Mutation(object):
    registerUser = RegisterUser.Field()
    addUserTopics = AddUserTopics.Field()
