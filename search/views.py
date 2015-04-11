from django.shortcuts import render, redirect
from django.db.models import Q
from enterprise.models import *
from accounts.models import MyUser
from nodes.models import Node
from myuserprofile.models import MyUserProfile
from enterprise_profile.models import EnterpriseProfile


def search(request):     # dynamic search on each page requested through ajax
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        terms = querystring.split()
        if not terms:
            return redirect('/search/')
        pquery = None
        qquery = None
        rquery = None
        for term in terms:

            q = MyUser.objects.filter(Q(first_name__icontains=term)
                                      | Q(last_name__icontains=term))
            p = Enterprise.objects.filter(enterprise__icontains=term)
            r = Q(Product.objects.filter(name__icontains=term))\
                | Q(EnterpriseProduct.objects.filter(caption__icontains=term))

            if pquery is None:
                pquery = p
            else:
                pquery = pquery & p


            if qquery is None:
                qquery = q
            else:
                qquery = qquery & q

            if rquery is None:
                rquery = r
            else:
                rquery = rquery & r



        return render(request, 'search/results.html', {

            'querystring': querystring,
            'qquery': qquery,
            'pquery': pquery,
            'rquery': rquery,
            't': terms})
    else:
        return render(request, 'search/search.html')


def search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        terms = querystring.split(' ')
        if not terms:
            return redirect('/search/')

        type=asset=product=operation=material=feed=myuser=enterprise=None
        c=d=e=f=g=h=None
        cc=dc=ec=fc=gc=hc=0
        for term in terms:
            typeo = Type.objects.filter(name__icontains=term)
            asseto = Asset.objects.filter(name__icontains=term)
            producto = Product.objects.filter(name__icontains=term)
            operationo = Operation.objects.filter(name__icontains=term)
            materialo = Material.objects.filter(name__icontains=term)

            feedo = Node.objects.filter(Q(title__icontains=term) | Q(post__icontains=term))
            myusero = MyUserProfile.objects.filter(Q(summary__icontains=term) | Q(experience__icontains=term))
            enterpriseo = EnterpriseProfile.objects.filter(Q(about__icontains=term) | Q(capabilities__icontains=term)
                                                           | Q(product_intro__icontains=term))


            if feed is None:
                feed = feedo
            else:
                feed = feed & feedo

            if myuser is None:
                myuser = myusero
            else:
                myuser = myuser & myusero

            if enterprise is None:
                enterprise = enterpriseo
            else:
                enterprise = enterprise & enterpriseo

            if type is None:
                type = typeo
            else:
                type = type | typeo

            if asset is None:
                asset = asseto
            else:
                asset = asset | asseto

            if product is None:
                product = producto
            else:
                product = product | producto

            if operation is None:
                operation = operationo
            else:
                operation = operation | operationo

            if material is None:
                material = materialo
            else:
                material = material | materialo

            if type:
                c = Enterprise.objects.filter(types=type)
                cc = c.count()

            if asset:
                d = Enterprise.objects.filter(assets=asset)
                dc = d.count()

            if product:
                e = Enterprise.objects.filter(products=product)
                ec = e.count()

            if operation:
                f = Enterprise.objects.filter(operations=operation)
                h = MyUserProfile.objects.filter(skillset=operation)
                fc = f.count()
                hc = h.count()

            if material:
                g = Enterprise.objects.filter(materials=material)
                gc = g.count()


        # return locals()

        return render(request, 'search/results2.html', locals()) # {

            # 'querystring': querystring,
            # 'c': c, 'cc': cc,
            # 'd': d, 'dc': dc,
            # 'e': e, 'ec': ec,
            # 'f': f, 'fc': fc,
            # 'g': g, 'gc': gc,
            # 'h': h, 'hc': hc})
    else:
        return render(request, 'search/search.html')





# def search(request):
#     if 'q' in request.GET:
#         querystring = request.GET.get('q').strip()
#         if len(querystring) == 0:
#             return redirect('/search/')
#
#         count = {}
#         results = {}
#
#         resultsp = results['people'] = MyUser.objects.filter(Q(first_name__icontains=querystring)
#                                                   | Q(last_name__icontains=querystring)
#                                                   | Q(email__icontains=querystring))
#         resultsn = results['nodes'] = Node.objects.filter(Q(title__icontains=querystring) | Q(post__icontains=querystring))
#         resultse = results['enterprise'] = Enterprise.objects.filter(enterprise__icontains=querystring)
#
#         resultspr = results['products'] = Product.objects.filter(name__icontains=querystring)
#
#         count['people'] = results['people'].count()
#         count['nodes'] = results['enterprise'].count()
#         count['enterprise'] = results['nodes'].count()
#         count['products'] = results['products'].count()
#
#         return render(request, 'search/results.html', {
#             'hide_search': True,
#             'querystring': querystring,
#             # 'active': search_type,
#             'count': count,
#             'resultse': resultse,
#             'resultsp': resultsp,
#             'resultsn': resultsn,
#             'resultspr': resultspr})
#     else:
#         return render(request, 'search/search.html', { 'hide_search': True })

# Create your views here.
