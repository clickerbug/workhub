import graphene
from graphql_jwt.decorators import login_required


class UserObj(graphene.ObjectType):
    username = graphene.String()
    firstName = graphene.String()
    lastName = graphene.String()
    name = graphene.String()
    email = graphene.String()

    def resolve_firstName(self, info):
        return self.first_name

    def resolve_lastName(self, info):
        return self.last_name

    def resolve_name(self, info):
        return self.first_name + ' ' + self.last_name

    # only logged in users can view email
    @login_required
    def resolve_email(self, info):
        return self.email
