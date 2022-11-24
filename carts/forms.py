from django import forms
from django.utils.translation import gettext_lazy as _
from shop.models import Product


class CartAddProductForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        self.fields['quantity'] = forms.IntegerField( max_value=args[0].get("product").stock,min_value=0)

    quantity = forms.IntegerField()
    product = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), to_field_name="id")
    



    # print(dir(), quantity)
    # update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
