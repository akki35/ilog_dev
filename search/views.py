from django.shortcuts import render, redirect
from django.db.models import Q
from enterprise.models import *
from accounts.models import MyUser
from nodes.models import Node
from myuserprofile.models import MyUserProfile


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
            r = Product.objects.filter(name__icontains=term)

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


# def search(request):
#     if 'q' in request.GET:
#         querystring = request.GET.get('q')
#         terms = querystring.split()
#         if not terms:
#             return redirect('/search/')
#
#         c=d=e=f=g=h=None
#         cc=dc=ec=fc=gc=hc=0
#         for term in terms:
#             type = Type.objects.filter(name__icontains=term)
#             asset = Asset.objects.filter(name__icontains=term)
#             product = Product.objects.filter(name__icontains=term)
#             operation = Operation.objects.filter(name__icontains=term)
#             material = Material.objects.filter(name__icontains=term)
#
#             if type:
#                 for t in type:
#                     co = Enterprise.objects.filter(types=type)
#                     cc = co.count()
#
#                     if co is None:
#                         c = co
#                     else:
#                         c = c & co
#
#             if asset:
#                 do = Enterprise.objects.filter(assets=asset)
#                 dc = do.count()
#
#             if product:
#                 e = Enterprise.objects.filter(products=product)
#                 ec = e.count()
#
#             if operation:
#                 fo = Enterprise.objects.filter(operations=operation)
#                 ho = MyUserProfile.objects.filter(skillset=operation)
#                 fc = fo.count()
#                 hc = ho.count()
#
#             if material:
#                 go = Enterprise.objects.filter(materials=material)
#                 gc = go.count()
#
#
#
#             if do is None:
#                 d = do
#             else:
#                 d = d & do
#
#         return render(request, 'search/results2.html', {
#
#             'querystring': querystring,
#             'c': c, 'cc': cc,
#             'd': d, 'dc': dc,
#             'e': e, 'ec': ec,
#             'f': f, 'fc': fc,
#             'g': g, 'gc': gc,
#             'h': h, 'hc': hc})
#     else:
#         return render(request, 'search/search.html')
#
#



# def search(request):
#     if 'q' in request.GET:
#         querystring = request.GET.get('q').strip()
#         if len(querystring) == 0:
#             return redirect('/search/')
#         # try:
#         #     search_type = request.GET.get('type')
#         #     if search_type not in ['people', 'nodes', 'enterprise', 'products']:
#         #         search_type = 'enterprise'
#         # except Exception as e:
#         #     search_type = 'enterprise'
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
