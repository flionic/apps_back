from django.utils import timezone
from django.db import models


class LinksList(models.Model):
    import json
    regions_file = open('regions/countries.json')
    REGIONS = ((i['code'], i['name']) for i in json.load(regions_file))

    name = models.CharField(max_length=128, verbose_name='Friendly name')
    url = models.URLField(max_length=512, verbose_name='Aff link')
    country = models.CharField(max_length=64, choices=REGIONS, verbose_name='Country', unique=True)
    counter = models.IntegerField(verbose_name='Opens counter', default=0)
    date_time = models.DateTimeField(default=timezone.now, verbose_name="Date added")

    class Meta:
        verbose_name = 'Geo link'
        verbose_name_plural = 'Geo Links'

    def __str__(self):
        return f'[{self.country}] {self.name}'
