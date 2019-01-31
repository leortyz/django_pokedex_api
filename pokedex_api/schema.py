from graphene import Schema, ObjectType, Field
from graphene_django.debug import DjangoDebug


class Query(ObjectType):
    debug = Field(DjangoDebug, name='__debug')


class Mutation(ObjectType):
    debug = Field(DjangoDebug, name='__debug')


schema = Schema(
    query=Query,
    mutation=Mutation
)
