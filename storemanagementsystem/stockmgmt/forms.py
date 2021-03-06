from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

        def clean_category(self):
            category = self.cleaned_data.get('category')

            if not category:
                raise forms.ValidationError('This field is required')
                return category

        def clean_item_name(self):
            item_name = self.cleaned_data.get('item_name')

            if not item_name:
                raise forms.ValidationError('This field is required')
                return item_name