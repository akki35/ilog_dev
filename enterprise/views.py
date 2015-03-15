from django.shortcuts import render, redirect, get_object_or_404
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

            operations = form.cleaned_data.get('operations')
            materials = form.cleaned_data.get('materials')
            er = Enterprise.objects.create(enterprise=enterprise,)
            er.types = types
            er.assets = assets
            er.operations = operations
            er.materials = materials

            welcome = u'{0} is now in the network, have a look at its profile.'.format(enterprise)
            node = Node(myuser=MyUser.objects.get(pk=1), post=welcome)
            node.save()

            return redirect('/accounts/signup')
    else:
        return render(request, 'enterprise/register.html', {'form': EnterpriseRegistrationForm()})

@login_required
def add_product(request):
    enterprise = request.user.enterprise
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if not form.is_valid():

            render(request, 'products/add_product.html', {'form': form})
        else:

            product = form.cleaned_data.get('prod')
            description = form.cleaned_data.get('description')
            product_image = form.cleaned_data.get('product_image')
            caption = form.cleaned_data.get('caption')

            p, created = Product.objects.get_or_create(name=product)

            ep = EnterpriseProduct.objects.create(product=p, enterprise=enterprise, description=description,
                                                  caption=caption, product_image=product_image)

            return redirect('/enterprise/products/add_product')
    else:
        return render(request, 'products/add_product.html', {'form': ProductForm()})

def product(request, slug):
    page_enterprise = get_object_or_404(Enterprise, slug=slug)
    products = EnterpriseProduct.objects.filter(enterprise=page_enterprise)

    return render(request, 'products/products.html', {
        'page_enterprise': page_enterprise,
        'products': products,
        # 'image': product_image,


        })



# Create your views here.
