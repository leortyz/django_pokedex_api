from graphene import relay
from graphene_django import DjangoObjectType

from pokedex.models import Pokemon, Type


class PokemonNode(DjangoObjectType):
    class Meta:
        model = Pokemon
        interfaces = (relay.Node, )
        filter_fields = {
            'number': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'name': ['exact', 'icontains', ]
        }


class TypeNode(DjangoObjectType):
    class Meta:
        model = Type
        interfaces = (relay.Node, )
        filter_fields = {
            'name': ['exact', ]
        }
