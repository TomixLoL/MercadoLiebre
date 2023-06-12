from django import forms

from .models import Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ["producto", "cantidad"]
        widgets = {
            "producto": forms.Select(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control"}),
        }
