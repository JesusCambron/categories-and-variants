from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from products.models import Product, VariantCategory, Variant
from products.forms import ProductForm, VariantCategoryFormset

def list(request):
    context={}
    context['products_list'] = Product.objects.all()
    return render(request, 'products/list.html', context)

def create(request):
    product = Product()
    context = {}
    product_form = ProductForm()
    context['product'] = product
    context['product_form'] = product_form
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        
        if product_form.is_valid():
            product = product_form.save()

        formset = VariantCategoryFormset(request.POST,request.FILES, instance=product)
        if formset.is_valid():
            formset.save()
            return redirect('products:list-product')
    else:
        formset = VariantCategoryFormset(instance=product)
        context['variant_categories_formset'] = formset
    
    return render(request, 'products/create.html', context)

def edit(request, product_id):
    context = {}
    product = get_object_or_404(Product, id=product_id)
    product_form = ProductForm(instance = product)
    formset = VariantCategoryFormset(instance=product)
    print(formset.forms[0])
    context['product'] = product
    context['product_form'] = product_form
    context['variant_categories_formset'] = formset

    if request.method == 'POST':
        formset = VariantCategoryFormset(request.POST,request.FILES, instance=product)
        print(formset.data)
        if formset.is_valid():
            formset.save()
            return redirect('products:list-product')
    
    return render(request, 'products/create.html', context)

