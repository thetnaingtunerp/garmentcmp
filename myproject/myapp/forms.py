from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

class EditOrderQtyForm(forms.ModelForm):
    class Meta:
        model = OrderQty
        fields =['style','making_charge','import_export_charge','box_charge','poly_bag','sewing_thread']
        widgets = {
            'style': forms.TextInput(attrs={'class': 'form-control col-md-6','readonly':'True'}),
            'making_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'import_export_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'box_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'poly_bag': forms.NumberInput(attrs={'class': 'form-control'}),
            'sewing_thread': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class OrderDeliveryForm(forms.ModelForm):
    class Meta:
        model = OrderQty
        fields = ['delivery']

class OrderETAForm(forms.ModelForm):
    class Meta:
        model = OrderQty
        fields = ['id','fabricETA','accETA']



class ProductionLineForm(forms.ModelForm):
    class Meta:
        model = ProductionLine
        fields = '__all__'
        widgets = {
            'ProductionLine': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class AccInventoyForm(forms.ModelForm):

    class Meta:
        model = AccInventoy
        fields = ['supplier_name','buyer_name','po_style_no','receive_qty','sku','receive_date','warehouse']
        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
            'buyer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'po_style_no': forms.TextInput(attrs={'class': 'form-control'}),
            'receive_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'warehouse': forms.Select(attrs={'class': 'form-control'}),
            'receive_date': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),


        }

class ImageForm(forms.ModelForm):

    class Meta:
        model = AccImage
        fields = '__all__'

class VariantForm(forms.ModelForm):

    class Meta:
        model = AccVariant
        fields = ['size','quantity','remark']
        widgets = {
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),

        }



VariantFormSet = inlineformset_factory(
    AccInventoy, AccVariant, form=VariantForm,
    extra=1, can_delete=True,
    can_delete_extra=True
)
ImageFormSet = inlineformset_factory(
    AccInventoy, AccImage, form=ImageForm,
    extra=1, can_delete=True,
    can_delete_extra=True
)






