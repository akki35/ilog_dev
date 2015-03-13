from django.shortcuts import render, redirect
from enterprise.forms import EnterpriseRegistrationForm, ProductForm
from enterprise.models import Enterprise, EnterpriseProduct, Product
from nodes.models import Node
from accounts.models import MyUser
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = EnterpriseRegistrationForm(request.POST)
        if not form.is_valid():
            print("form invalid")
            render(request, 'enterprise/register.html', {'form': form})
        else:
            enterprise = form.cleaned_data.get('enterprise')
            types = form.cleaned_data.get('types')
            assets = form.cleaned_data.get('assets')
            products = form.cleaned_data.get('products')
            operations = form.cleaned_data.get('operations')
            materials = form.cleaned_data.get('materials')
            er = Enterprise.objects.create(enterprise=enterprise,) # types=types, assets=assets,
                                                # operations=operations, products=products, materials=materials)
            er.types = types
            er.assets = assets
            er.operations = operations
            er.materials = materials
            # er.products.add(products)
            welcome = u'{0} is now in the network, have a look at its profile.'.format(enterprise)
            node = Node(myuser=MyUser.objects.get(pk=1), post=welcome)
            node.save()

            return redirect('/accounts/register')
    else:
        return render(request, 'enterprise/register.html', {'form': EnterpriseRegistrationForm()})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        enterprise = request.user.enterprise
        if not form.is_valid():
            print('yups')
            render(request, 'products/add_product.html', {'form': form})
        else:
            print('kya hai bhai')
            product = form.cleaned_data.get('prod')
            description = form.cleaned_data.get('description')
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')

            p, created = Product.objects.get_or_create(name=product)

            ep = EnterpriseProduct.objects.create(product=p, enterprise=enterprise, description=description, caption=caption, product_image=image)

            return redirect('/products/add_product/')
    else:
        return render(request, 'products/add_product.html', {'form': ProductForm()})




# Create your views here.
