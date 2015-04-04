from django.shortcuts import render, redirect, get_object_or_404
from enterprise.forms import EnterpriseRegistrationForm, ProductForm, AssetForm
from enterprise.models import *
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
            # assets = form.cleaned_data.get('assets')

            operations = form.cleaned_data.get('operations')
            materials = form.cleaned_data.get('materials')

            # t, created= Type.objects.get_or_create(name=types)
            # a, creted = Asset.objects.get_or_create(name=assets)
            er = Enterprise.objects.create(enterprise=enterprise,)
            er.types = types
            # er.assets = assets
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
                                                  caption=caption, product_image=product_image,
                                                  product_image_thumbnail=product_image)

            return redirect('/enterprise/add_product')
    else:
        return render(request, 'products/add_product.html', {'form': ProductForm()})

@login_required
def add_asset(request):
    enterprise = request.user.enterprise
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)

        if not form.is_valid():

            render(request, 'asset/add_asset.html', {'form': form})  ##
        else:

            asset = form.cleaned_data.get('asse')
            description = form.cleaned_data.get('description')
            asset_image = form.cleaned_data.get('asset_image')
            caption = form.cleaned_data.get('caption')

            a, created = Asset.objects.get_or_create(name=asset)

            ep = EnterpriseAsset.objects.create(asset=a, enterprise=enterprise, description=description,
                                                  caption=caption, asset_image=asset_image,
                                                  asset_image_thumbnail=asset_image)

            return redirect('/enterprise/add_asset')
    else:
        return render(request, 'assets/add_asset.html', {'form': AssetForm()})


def product(request, slug):
    page_enterprise = get_object_or_404(Enterprise, slug=slug)
    products = EnterpriseProduct.objects.filter(enterprise=page_enterprise)

    return render(request, 'products/products.html', {
        'page_enterprise': page_enterprise,
        'products': products,
        # 'image': product_image,
        })


def people(request, slug):
    page_enterprise = get_object_or_404(Enterprise, slug=slug)
    members = MyUser.objects.filter(enterprise=page_enterprise)

    return render(request, 'products/people.html', {
        'page_enterprise': page_enterprise,
        'members': members,
        # 'image': product_image,
        })

def about(request, slug):
    page_enterprise = get_object_or_404(Enterprise, slug=slug)
    types = page_enterprise.types.all()
    about = page_enterprise.enterpriseprofile.about
    website = page_enterprise.enterpriseprofile.website

    return render(request, 'products/about.html', {
        'types': types,
        'about': about,
        'page_enterprise': page_enterprise,
        'website': website,
        })

def capability(request, slug):
    page_enterprise = get_object_or_404(Enterprise, slug=slug)
    assets = EnterpriseAsset.objects.filter(enterprise=page_enterprise)
    operations = page_enterprise.operations.all()

    return render(request, 'products/capability.html', {
        'assets': assets,
        'operations': operations,
        'page_enterprise': page_enterprise,

        })


# Create your views here.
