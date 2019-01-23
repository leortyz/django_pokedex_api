from django.db import models


class Type(models.Model):
    name = models.CharField(
        max_length=15,
        unique=True
    )

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return '{name} Type'.format(
            name=self.name
        )


class Pokemon(models.Model):
    number = models.PositiveIntegerField(
        unique=True
    )
    name = models.CharField(
        max_length=30
    )
    height = models.FloatField(
        null=True,
        blank=True
    )
    weight = models.FloatField(
        null=True,
        blank=True
    )
    evolve_from = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="evolve_to",
        null=True,
        blank=True
    )
    type_1 = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        related_name="pokemon_type_1"
    )
    type_2 = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        related_name="pokemon_type_2",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemon'

    def __str__(self):
        return '{number}: {name}'.format(
            number=self.number,
            name=self.name
        )
