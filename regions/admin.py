from django.contrib import admin

from regions.models import LinksList
from regions.admin_forms import LinksListForm


@admin.register(LinksList)
class SliderImageAdmin(admin.ModelAdmin):
    form = LinksListForm
    readonly_fields = ('date_time', 'counter')
