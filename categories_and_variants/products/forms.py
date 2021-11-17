from django import forms
from products.models import Product, VariantCategory, Variant
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet

VariantFormset = inlineformset_factory(VariantCategory, Variant, fields=('name','image'),extra=1)

class ProductForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre',
        error_messages={'required': 'Debe capturar el nombre'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    description = forms.CharField(
        label='Descripción',
        error_messages={'required': 'Debe capturar la descripción'},
        widget=forms.Textarea()
    )

    class Meta:
        model = Product
        fields = ('name', 'description')

class BaseVariantCategoryFormset(BaseInlineFormSet):
    
    def add_fields(self, form, index):
        super(BaseVariantCategoryFormset, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = VariantFormset(
                        instance=form.instance,
                        data=form.data if form.is_bound else None,
                        files=form.files if form.is_bound else None,
                        prefix='variants-%s-%s' % (
                            form.prefix,
                            VariantFormset.get_default_prefix()))
        
    def is_valid(self):
        result = super(BaseVariantCategoryFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    result = result and form.nested.is_valid()

        return result

    def save(self, commit=True):
    
        result = super(BaseVariantCategoryFormset, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result

VariantCategoryFormset = inlineformset_factory(Product,
                                        VariantCategory,
                                        fields=('name',),
                                        formset=BaseVariantCategoryFormset, extra=1)