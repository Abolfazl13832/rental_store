from django import forms
from tools.models import Tool


class AddToBasketForm(forms.Form):
    tool = forms.ModelChoiceField(queryset=Tool.default_manager.all(),widget=forms.HiddenInput)
    quantity = forms.IntegerField()

    def save(self,basket):
        basket.add(
            tool=self.cleaned_data.get('tool'),
            quantity=self.cleaned_data.get('quantity')
        )
        return basket