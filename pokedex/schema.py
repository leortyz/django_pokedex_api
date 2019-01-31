from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from pokedex.nodes import PokemonNode


class Query(object):
    pokemon = relay.Node.Field(PokemonNode)
    pokemons = DjangoFilterConnectionField(PokemonNode)


class Mutation(object):
    pass
