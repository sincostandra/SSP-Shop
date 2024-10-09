from typing import Any
from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'pack_category', 'level_category', 'description']

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_pack_category(self):
        pack_category = self.cleaned_data["pack_category"]
        return strip_tags(pack_category)
    
    def clean_level_category(self):
        level_category = self.cleaned_data["level_category"]
        return strip_tags(level_category)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    