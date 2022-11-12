from django import forms

from regions.models import LinksList


class LinksListForm(forms.ModelForm):
    class Meta:
        model = LinksList
        fields = '__all__'
