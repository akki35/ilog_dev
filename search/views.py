from django.shortcuts import render,redirect
from django.db.models import Q
from enterprise.models import Product, Asset, Enterprise
from accounts.models import MyUser
from nodes.models import Node




def search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()
        if len(querystring) == 0:
            return redirect('/search/')
        # try:
        #     search_type = request.GET.get('type')
        #     if search_type not in ['people', 'nodes', 'enterprise', 'products']:
        #         search_type = 'enterprise'
        # except Exception as e:
        #     search_type = 'enterprise'

        count = {}
        results = {}

        resultsp = results['people'] = MyUser.objects.filter(Q(first_name__icontains=querystring)
                                                  | Q(last_name__icontains=querystring)
                                                  | Q(email__icontains=querystring))
        resultsn = results['nodes'] = Node.objects.filter(Q(title__icontains=querystring) | Q(post__icontains=querystring))
        resultse = results['enterprise'] = Enterprise.objects.filter(enterprise__icontains=querystring)

        resultspr = results['products'] = Product.objects.filter(name__icontains=querystring)

        count['people'] = results['people'].count()
        count['nodes'] = results['enterprise'].count()
        count['enterprise'] = results['nodes'].count()
        count['products'] = results['products'].count()

        return render(request, 'search/results.html', {
            'hide_search': True,
            'querystring': querystring,
            # 'active': search_type,
            'count': count,
            'resultse': resultse,
            'resultsp': resultsp,
            'resultsn': resultsn,
            'resultspr': resultspr})
    else:
        return render(request, 'search/search.html', { 'hide_search': True })

# Create your views here.
